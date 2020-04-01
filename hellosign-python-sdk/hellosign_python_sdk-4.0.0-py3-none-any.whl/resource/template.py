from .resource import Resource
from .account import Account

#
# The MIT License (MIT)
# 
# Copyright (C) 2014 hellosign.com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


class Template(Resource):
    ''' Contains information about the templates you and your team have created

    Attributes:
        template_id (str): The id of the Template

        title (str): The title of the Template which will also be the
        default subject of the message sent to signers when using this
        Template to send a SignatureRequest.

        message (str): The default message that will be sent to signers when
        using this Template to send a SignatureRequest.

        signer_roles (list of dict): An array of the designated signer roles
        that must be specified when sending a SignatureRequest using this
        Template.
            name (str): The name of the Role
            order (int): If signer order is assigned this is the 0-based index
            for this role

        cc_roles (list of dict): An array of the designated CC roles that must
        be specified when sending a SignatureRequest using this
        Template.
            name (str): The name of the Role

        documents (list of dict): An array describing each document associated
        with this Template. Includes form field data for each document.
            name (str): Name of the associated file
            index (int): Document ordering, the lowest index is diplayed first
                and the highest last
            form_fields (list of dict): An array of Form Field objects
                containing the name and type of each named textbox and checkmark
                field.

                api_id (str): A unique id for the form field
                name (str): The name of the form field
                type (str): The type of this form field
                x (int): The horizontal offset in pixels for this form field
                y (int): The vertical offset in pixels for this form field
                width (int): The width in pixels of this form field
                height (int): The height in pixels of this form field
                required (bool): Boolean showing whether or not this field is
                    required
            custom_fields (list of dict): An array of Custom Field objects
                containing the name and type of each custom field

                name (str): The name of the Custom Field
                type (str): The type of this Custom Field. Currently, 'text' is
                    the only valid value
            named_form_fields (DEPRECATED): Use "form_fields" under the
                "documents" array instead.

        accounts (list of dict): An array of the Accounts that can use this Template.

            account_id (str): The id of the Account
            email_address (str): The email address associated with the Account

        is_creator (bool): True if you are the owner of this template, false if
            it's been shared with you by a team member.

        can_edit (bool): Indicates whether edit rights have been granted to you
            by the owner (always true if that's you).

        edit_url (str): Returned when creating a new embedded draft

        expires_at (int): Date when the edit_url expires
    '''

    def __init__(self, jsonstr=None, key=None, warnings=None):
        ''' Initialization of the object

        Args:
            jsonstr (str): a raw JSON string that is returned by a request.
                We store all the data in `self.json_data` and use `__getattr__`
                and `__setattr__` to make the data accessible like attributes
                of the object
            key (str): Optional key to use with jsonstr. If `key` exists, we'll
                load the data of `jsonstr[key]` instead of the whole `jsonstr`
            warnings (list): List of associated warnings
        '''
        super(Template, self).__init__(jsonstr, key, warnings)
        if 'reusable_form_id' in self.json_data:
            self.json_data['template_id'] = self.json_data['reusable_form_id']
            del self.json_data['reusable_form_id']
        if 'accounts' in self.json_data:
            acct_list = []
            for acct in self.accounts:
                acct_list.append(Account(acct))
            self.accounts = acct_list

    def __str__(self):
        ''' Return a string representation of this template '''
        return 'Template %s' % self.template_id
