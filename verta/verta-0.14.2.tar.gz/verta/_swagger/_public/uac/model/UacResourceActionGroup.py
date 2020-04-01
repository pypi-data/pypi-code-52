# THIS FILE IS AUTO-GENERATED. DO NOT EDIT
from verta._swagger.base_type import BaseType

class UacResourceActionGroup(BaseType):
  def __init__(self, resources=None, actions=None):
    required = {
      "resources": False,
      "actions": False,
    }
    self.resources = resources
    self.actions = actions

    for k, v in required.items():
      if self[k] is None and v:
        raise ValueError('attribute {} is required'.format(k))

  @staticmethod
  def from_json(d):
    from .UacResources import UacResources

    from .UacAction import UacAction


    tmp = d.get('resources', None)
    if tmp is not None:
      d['resources'] = [UacResources.from_json(tmp) for tmp in tmp]
    tmp = d.get('actions', None)
    if tmp is not None:
      d['actions'] = [UacAction.from_json(tmp) for tmp in tmp]

    return UacResourceActionGroup(**d)
