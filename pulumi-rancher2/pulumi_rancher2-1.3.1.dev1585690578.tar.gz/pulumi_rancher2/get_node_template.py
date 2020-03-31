# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetNodeTemplateResult:
    """
    A collection of values returned by getNodeTemplate.
    """
    def __init__(__self__, annotations=None, cloud_credential_id=None, description=None, driver=None, engine_env=None, engine_insecure_registries=None, engine_install_url=None, engine_label=None, engine_opt=None, engine_registry_mirrors=None, engine_storage_driver=None, id=None, labels=None, name=None, use_internal_ip_address=None):
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        __self__.annotations = annotations
        """
        (Computed) Annotations for Node Template object (map)
        """
        if cloud_credential_id and not isinstance(cloud_credential_id, str):
            raise TypeError("Expected argument 'cloud_credential_id' to be a str")
        __self__.cloud_credential_id = cloud_credential_id
        """
        (Computed) Cloud credential ID for the Node Template. Required from Rancher v2.2.x (string)
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        (Computed) Description for the Node Template (string)
        """
        if driver and not isinstance(driver, str):
            raise TypeError("Expected argument 'driver' to be a str")
        __self__.driver = driver
        """
        (Computed) The driver of the node template (string)
        """
        if engine_env and not isinstance(engine_env, dict):
            raise TypeError("Expected argument 'engine_env' to be a dict")
        __self__.engine_env = engine_env
        """
        (Computed) Engine environment for the node template (string)
        """
        if engine_insecure_registries and not isinstance(engine_insecure_registries, list):
            raise TypeError("Expected argument 'engine_insecure_registries' to be a list")
        __self__.engine_insecure_registries = engine_insecure_registries
        """
        (Computed) Insecure registry for the node template (list)
        """
        if engine_install_url and not isinstance(engine_install_url, str):
            raise TypeError("Expected argument 'engine_install_url' to be a str")
        __self__.engine_install_url = engine_install_url
        """
        (Computed) Docker engine install URL for the node template (string)
        """
        if engine_label and not isinstance(engine_label, dict):
            raise TypeError("Expected argument 'engine_label' to be a dict")
        __self__.engine_label = engine_label
        """
        (Computed) Engine label for the node template (string)
        """
        if engine_opt and not isinstance(engine_opt, dict):
            raise TypeError("Expected argument 'engine_opt' to be a dict")
        __self__.engine_opt = engine_opt
        """
        (Computed) Engine options for the node template (map)
        """
        if engine_registry_mirrors and not isinstance(engine_registry_mirrors, list):
            raise TypeError("Expected argument 'engine_registry_mirrors' to be a list")
        __self__.engine_registry_mirrors = engine_registry_mirrors
        """
        (Computed) Engine registry mirror for the node template (list)
        """
        if engine_storage_driver and not isinstance(engine_storage_driver, str):
            raise TypeError("Expected argument 'engine_storage_driver' to be a str")
        __self__.engine_storage_driver = engine_storage_driver
        """
        (Computed) Engine storage driver for the node template (string)
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
        (Computed) Labels for Node Template object (map)
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if use_internal_ip_address and not isinstance(use_internal_ip_address, bool):
            raise TypeError("Expected argument 'use_internal_ip_address' to be a bool")
        __self__.use_internal_ip_address = use_internal_ip_address
        """
        (Computed) Engine storage driver for the node template (bool)
        """
class AwaitableGetNodeTemplateResult(GetNodeTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNodeTemplateResult(
            annotations=self.annotations,
            cloud_credential_id=self.cloud_credential_id,
            description=self.description,
            driver=self.driver,
            engine_env=self.engine_env,
            engine_insecure_registries=self.engine_insecure_registries,
            engine_install_url=self.engine_install_url,
            engine_label=self.engine_label,
            engine_opt=self.engine_opt,
            engine_registry_mirrors=self.engine_registry_mirrors,
            engine_storage_driver=self.engine_storage_driver,
            id=self.id,
            labels=self.labels,
            name=self.name,
            use_internal_ip_address=self.use_internal_ip_address)

def get_node_template(name=None,use_internal_ip_address=None,opts=None):
    """
    Use this data source to retrieve information about a Rancher v2 Node Template resource.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-rancher2/blob/master/website/docs/d/nodeTemplate.html.markdown.


    :param str name: The name of the Node Template (string)
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['useInternalIpAddress'] = use_internal_ip_address
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('rancher2:index/getNodeTemplate:getNodeTemplate', __args__, opts=opts).value

    return AwaitableGetNodeTemplateResult(
        annotations=__ret__.get('annotations'),
        cloud_credential_id=__ret__.get('cloudCredentialId'),
        description=__ret__.get('description'),
        driver=__ret__.get('driver'),
        engine_env=__ret__.get('engineEnv'),
        engine_insecure_registries=__ret__.get('engineInsecureRegistries'),
        engine_install_url=__ret__.get('engineInstallUrl'),
        engine_label=__ret__.get('engineLabel'),
        engine_opt=__ret__.get('engineOpt'),
        engine_registry_mirrors=__ret__.get('engineRegistryMirrors'),
        engine_storage_driver=__ret__.get('engineStorageDriver'),
        id=__ret__.get('id'),
        labels=__ret__.get('labels'),
        name=__ret__.get('name'),
        use_internal_ip_address=__ret__.get('useInternalIpAddress'))
