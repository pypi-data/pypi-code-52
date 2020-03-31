# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, annotations=None, data=None, description=None, id=None, labels=None, name=None, namespace_id=None, project_id=None):
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        __self__.annotations = annotations
        """
        (Computed) Annotations for secret object (map)
        """
        if data and not isinstance(data, dict):
            raise TypeError("Expected argument 'data' to be a dict")
        __self__.data = data
        """
        (Computed) Secret key/value data. Base64 encoding required for values (map)
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        (Computed) A secret description (string)
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        __self__.labels = labels
        """
        (Computed) Labels for secret object (map)
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if namespace_id and not isinstance(namespace_id, str):
            raise TypeError("Expected argument 'namespace_id' to be a str")
        __self__.namespace_id = namespace_id
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            annotations=self.annotations,
            data=self.data,
            description=self.description,
            id=self.id,
            labels=self.labels,
            name=self.name,
            namespace_id=self.namespace_id,
            project_id=self.project_id)

def get_secret(name=None,namespace_id=None,project_id=None,opts=None):
    """
    Use this data source to retrieve information about a Rancher v2 secret.

    Depending of the availability, there are 2 types of Rancher v2 secrets:
    - Project secret: Available to all namespaces in the `project_id`
    - Namespaced secret: Available to just `namespace_id` in the `project_id`

    > This content is derived from https://github.com/terraform-providers/terraform-provider-rancher2/blob/master/website/docs/d/secret.html.markdown.


    :param str name: The name of the secret (string)
    :param str namespace_id: The namespace id where to assign the namespaced secret (string)
    :param str project_id: The project id where to assign the secret (string)
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['namespaceId'] = namespace_id
    __args__['projectId'] = project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('rancher2:index/getSecret:getSecret', __args__, opts=opts).value

    return AwaitableGetSecretResult(
        annotations=__ret__.get('annotations'),
        data=__ret__.get('data'),
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        labels=__ret__.get('labels'),
        name=__ret__.get('name'),
        namespace_id=__ret__.get('namespaceId'),
        project_id=__ret__.get('projectId'))
