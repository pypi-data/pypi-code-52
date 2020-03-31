# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
from typing import Optional

import pulumi
import pulumi.runtime
from pulumi import Input, ResourceOptions

from ... import tables, version


class Deployment(pulumi.CustomResource):
    """
    DEPRECATED - apps/v1beta2/Deployment is deprecated by apps/v1/Deployment and not supported by
    Kubernetes v1.16+ clusters.
    
    Deployment enables declarative updates for Pods and ReplicaSets.
    
    This resource waits until its status is ready before registering success
    for create/update, and populating output properties from the current state of the resource.
    The following conditions are used to determine whether the resource creation has
    succeeded or failed:
    
    1. The Deployment has begun to be updated by the Deployment controller. If the current
       generation of the Deployment is > 1, then this means that the current generation must
       be different from the generation reported by the last outputs.
    2. There exists a ReplicaSet whose revision is equal to the current revision of the
       Deployment.
    3. The Deployment's '.status.conditions' has a status of type 'Available' whose 'status'
       member is set to 'True'.
    4. If the Deployment has generation > 1, then '.status.conditions' has a status of type
       'Progressing', whose 'status' member is set to 'True', and whose 'reason' is
       'NewReplicaSetAvailable'. For generation <= 1, this status field does not exist,
       because it doesn't do a rollout (i.e., it simply creates the Deployment and
       corresponding ReplicaSet), and therefore there is no rollout to mark as 'Progressing'.
    
    If the Deployment has not reached a Ready state after 10 minutes, it will
    time out and mark the resource update as Failed. You can override the default timeout value
    by setting the 'customTimeouts' option on the resource.
    """

    apiVersion: pulumi.Output[str]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should
    convert recognized schemas to the latest internal value, and may reject unrecognized values.
    More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources
    """

    kind: pulumi.Output[str]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer
    this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
    info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds
    """

    metadata: pulumi.Output[dict]
    """
    Standard object metadata.
    """

    spec: pulumi.Output[dict]
    """
    Specification of the desired behavior of the Deployment.
    """

    status: pulumi.Output[dict]
    """
    Most recently observed status of the Deployment.
    """

    def __init__(self, resource_name, opts=None, metadata=None, spec=None, __name__=None, __opts__=None):
        """
        Create a Deployment resource with the given unique name, arguments, and options.

        :param str resource_name: The _unique_ name of the resource.
        :param pulumi.ResourceOptions opts: A bag of options that control this resource's behavior.
        :param pulumi.Input[dict] metadata: Standard object metadata.
        :param pulumi.Input[dict] spec: Specification of the desired behavior of the Deployment.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'apps/v1beta2'
        __props__['kind'] = 'Deployment'
        __props__['metadata'] = metadata
        __props__['spec'] = spec

        __props__['status'] = None

        parent = opts.parent if opts and opts.parent else None
        aliases = [
            pulumi.Alias(type_="kubernetes:apps/v1:Deployment"),
            pulumi.Alias(type_="kubernetes:apps/v1beta1:Deployment"),
            pulumi.Alias(type_="kubernetes:extensions/v1beta1:Deployment"),
        ]
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(
            version=version.get_version(),
            aliases=aliases,
        ))

        super(Deployment, self).__init__(
            "kubernetes:apps/v1beta2:Deployment",
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None):
        """
        Get the state of an existing `Deployment` resource, as identified by `id`.
        The ID is of the form `[namespace]/[name]`; if `[namespace]` is omitted,
        then (per Kubernetes convention) the ID becomes `default/[name]`.

        Pulumi will keep track of this resource using `resource_name` as the Pulumi ID.

        :param str resource_name: _Unique_ name used to register this resource with Pulumi.
        :param pulumi.Input[str] id: An ID for the Kubernetes resource to retrieve.
               Takes the form `[namespace]/[name]` or `[name]`.
        :param Optional[pulumi.ResourceOptions] opts: A bag of options that control this
               resource's behavior.
        """
        opts = ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))
        return Deployment(resource_name, opts)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
