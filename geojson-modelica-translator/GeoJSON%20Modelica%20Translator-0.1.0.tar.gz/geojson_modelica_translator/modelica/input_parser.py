"""
****************************************************************************************************
:copyright (c) 2019-2020 URBANopt, Alliance for Sustainable Energy, LLC, and other contributors.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions
and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions
and the following disclaimer in the documentation and/or other materials provided with the
distribution.

Neither the name of the copyright holder nor the names of its contributors may be used to endorse
or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
****************************************************************************************************
"""

import os

from jinja2 import Environment, FileSystemLoader


class PackageParser(object):
    """
    Class to read and modify the package.mo and the package.order file
    """

    def __init__(self, path=None):
        """
        Create an instance to manage the package.mo/order file. If no path is provided then the user
        must add in their own package and order data. Or the user can load from the new_from_template
        class method.

        :param path: string, path to where the package.mo and package.order reside.
        """
        self.path = path
        self.order_data = None
        self.package_data = None
        self.load()

        self.template_env = Environment(
            loader=FileSystemLoader(
                searchpath=os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), "templates"
                )
            )
        )

    @classmethod
    def new_from_template(cls, path, name, order, within=None):
        """
        Create new package data based on the package.mo template. If within is not specified, then it is
        assumed that this is a top level package and will load from the package_base template.

        :param path: string, the path where the resulting files will be saved to.
        :param name: string, the name of the model
        :param order: list, ordered list of which models will be loaded (saved to package.order)
        :param within: string, (optional), name where this package is within.
        """
        klass = PackageParser(path)
        if within:
            template = klass.template_env.get_template("package.mot")
        else:
            template = klass.template_env.get_template("package_base.mot")

        klass.package_data = template.render(within=within, name=name, order=order)
        klass.order_data = "\n".join(order)
        klass.order_data += "\n"  # trailing line
        return klass

    def load(self):
        """
        Load the package.mo and package.mo data from the member variable path
        """
        filename = os.path.join(self.path, "package.mo")
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.package_data = f.read()

        filename = os.path.join(self.path, "package.order")
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.order_data = f.read()

    def save(self):
        """
        Save the updated files to the same location
        """
        with open(os.path.join(os.path.join(self.path, "package.mo")), "w") as f:
            f.write(self.package_data)

        with open(os.path.join(os.path.join(self.path, "package.order")), "w") as f:
            f.write(self.order_data)

    @property
    def order(self):
        """
        Return the order of the packages from the package.order file

        :return: list, list of the loaded models in the package.order file
        """
        return self.order_data.split("\n")

    def rename_model(self, old_model, new_model):
        """
        Rename the model name in the package.order file

        :param old_model: string, existing name
        :param new_model: string, new name
        """
        self.order_data = self.order_data.replace(old_model, new_model)


class InputParser(object):
    """
    Class to read in Modelica files (.mo) and provide basic operations.
    """

    def __init__(self, modelica_filename):
        if not os.path.exists(modelica_filename):
            raise Exception(f"Modelica file does not exist: {modelica_filename}")

        self.modelica_filename = modelica_filename
        self.init_vars()
        self.parse_mo()

    def init_vars(self):
        self.within = None
        self.model = {"name": None, "comment": None, "objects": []}
        self.connections = []
        self.equations = []

    def parse_mo(self):
        # eventually move this over to use token-based assessment of the files. Here is a list of some of the tokens
        # TODO: strip all spacing and reconstruct on export
        tokens = [
            "within",
            "block",
            "algorithm",
            "model",
            "equation",
            "protected",
            "package",
            "extends",
            "initial equation",
            "end",
        ]
        current_block = None
        obj_data = ""
        connect_data = ""
        with open(self.modelica_filename, "r") as f:
            for index, line in enumerate(f.readlines()):
                if line == "\n":
                    # Skip blank lines (for now?
                    continue
                elif line.startswith("within"):
                    # these lines typically only have a single line, so just persist it
                    if not self.within:
                        # remove the line feed and the trailing semicolon
                        self.within = line.split(" ")[1].rstrip().replace(";", "")
                    else:
                        raise Exception("More than one 'within' lines found")
                    continue
                elif line.startswith("model"):
                    # get the model name and save
                    self.model["name"] = line.split(" ")[1].rstrip()
                    current_block = "model"
                    continue
                elif line.startswith("equation"):
                    current_block = "equation"
                    continue
                elif line.startswith("end"):
                    current_block = "end"
                else:
                    # check if any other tokens are triggered and throw a 'not-supported' message
                    for t in tokens:
                        if line.startswith(t):
                            raise Exception(
                                f"Found other token '{t}' in '{self.modelica_filename}' that is not supported... \
                                cannot continue"
                            )

                # now store data that is in between these other blocks
                if current_block == "model":
                    # grab the lines that are comments:
                    if (
                        not obj_data
                        and line.strip().startswith('"')
                        and line.strip().endswith('"')
                    ):
                        self.model["comment"] = line.rstrip()
                        continue

                    # determine if this is a new object or a new object (look for ';')
                    obj_data += line
                    if line.endswith(";\n"):
                        self.model["objects"].append(obj_data)
                        obj_data = ""
                elif current_block == "equation":
                    if line.strip().startswith("connect"):
                        connect_data += line
                    elif connect_data and line.endswith(";\n"):
                        connect_data += line
                        self.connections.append(connect_data)
                        connect_data = ""
                    elif connect_data:
                        connect_data += line
                    else:
                        self.equations.append(line)
                elif current_block == "end":
                    pass
                else:
                    # there is nothing to do here
                    pass

    def save(self):
        """
        Save the resulting file to the same file from which it was initialized

        :return:
        """
        self.save_as(self.modelica_filename)

    def save_as(self, new_filename):
        """
        Save the resulting file with a new filename

        :param new_filename:
        :return:
        """
        with open(new_filename, "w") as f:
            f.write(self.serialize())

    def remove_object(self, obj_name):
        """
        Remove an object by a name. Can be any part of the object name.

        :param obj_name: string, object name to match
        :return:
        """
        index, obj = self.find_model_object(obj_name)
        if index is not None:
            del self.model["objects"][index]

    def replace_within_string(self, new_string):
        """
        Replacement of the path portion of the within string

        :param new_string: string, what to replace the existing within string with.
        """
        self.within = new_string

    def find_model_object(self, obj_name):
        """
        Find a model object in the list of parsed objects
        :param obj_name: string, name (including the instance)
        :return: list, index and string of object
        """
        for index, o in enumerate(self.model["objects"]):
            if obj_name in o:
                return index, self.model["objects"][index]

        return None, None

    def reload(self):
        """
        Reparse the data. This will remove any unsaved changes.
        """
        self.init_vars()
        self.parse_mo()

    def replace_model_string(self, model_name, model_instance, old_string, new_string):
        """
        Go through the models and find the model_name with a model_instance and change the value in the field to
        the new_value. This will replace the entire value of the model field.

        This will not work with arrays or lists (e.g., {...}, [...])

        :param model_name: string, name of the model
        :param model_instance: string, instance of the model
        :param old_string: string, name of the old string to replace
        :param new_string: string, the new string
        """
        index, _model = self.find_model_object(f"{model_name} {model_instance}")
        if index is not None:
            self.model["objects"][index] = self.model["objects"][index].replace(
                old_string, new_string
            )

    def add_model_object(self, model_name, model_instance, data):
        """
        Add a new model object to the model

        :param model_name: string
        :param model_instance: string
        :param data: list of strings
        """
        str = f"  {model_name} {model_instance}\n"
        for d in data:
            str += f"    {d}\n"
        self.model["objects"].append(str)

    def add_connect(self, a, b, annotation):
        """
        Add a new connection of port a to port b. The annotation will be appended on a new line.

        :param a: string, port a
        :param b: string, port b
        :param annotation: string, description
        """
        self.connections.append(f"  connect({a}, {b})\n    {annotation};\n")

    def find_connect(self, port_a, port_b):
        """
        Find an existing connection that has port_a and/or port_b. If there are more than one, then it will only
        return the first.

        :param port_a:
        :param port_b:
        :return:
        """
        for index, c in enumerate(self.connections):
            if not port_a:
                raise Exception("Unable to replace string in connect if unknown port A")
            if not port_b:
                if f"({port_a}, " in c:
                    return index, c
            if port_a and port_b:
                if f"({port_a}, {port_b})" in c:
                    return index, c

        return None, None

    def replace_connect_string(self, a, b, new_a, new_b, replace_all=False):
        """
        Replace content of the connect string with new_a and/or new_b

        :param a: string, existing port a
        :param b: string, existing port b
        :param new_a: string, new port (or none)
        :param new_b: string, new port b (or none
        :param replace_all: boolean, allow replacemnt of all strings
        """
        # find the connection that matches a, b
        index, c = self.find_connect(a, b)
        while index:
            if index:
                if new_a:
                    self.connections[index] = self.connections[index].replace(a, new_a)
                if new_b:
                    self.connections[index] = self.connections[index].replace(b, new_b)

            if not replace_all:
                break
            else:
                index, c = self.find_connect(a, b)

    def remove_connect_string(self, a, b):
        """
        Remove a connection string that matches the a, b.

        :param a: string, existing port a
        :param b: string, existing port b
        """
        # find the connection that matches a, b
        index, c = self.find_connect(a, b)
        if index:
            del self.connections[index]

    def serialize(self):
        """
        Serialize the modelica object to a string with line feeds

        :return: string
        """
        str = f"within {self.within};\n"
        str += f"model {self.model['name']}\n"
        str += f"{self.model['comment']}\n\n"
        for o in self.model["objects"]:
            for l in o:
                str += l
        str += "equation\n"
        for c in self.connections:
            str += c
        for e in self.equations:
            str += e
        str += f"end {self.model['name']};\n"
        return str
