import copy

from unittest.mock import call, Mock

import kopf
from kopf.structs.bodies import RawBody, RawMeta, Body

OWNER_API_VERSION = 'owner-api-version'
OWNER_NAMESPACE = 'owner-namespace'
OWNER_KIND = 'OwnerKind'
OWNER_NAME = 'owner-name'
OWNER_UID = 'owner-uid'
OWNER_LABELS = {'label-1': 'value-1', 'label-2': 'value-2'}
OWNER = RawBody(
    apiVersion=OWNER_API_VERSION,
    kind=OWNER_KIND,
    metadata=RawMeta(
        namespace=OWNER_NAMESPACE,
        name=OWNER_NAME,
        uid=OWNER_UID,
        labels=OWNER_LABELS,
    ),
)


def test_appending_to_dict():
    obj = {}

    kopf.append_owner_reference(obj, owner=Body(OWNER))

    assert 'metadata' in obj
    assert 'ownerReferences' in obj['metadata']
    assert isinstance(obj['metadata']['ownerReferences'], list)
    assert len(obj['metadata']['ownerReferences']) == 1
    assert isinstance(obj['metadata']['ownerReferences'][0], dict)
    assert obj['metadata']['ownerReferences'][0]['apiVersion'] == OWNER_API_VERSION
    assert obj['metadata']['ownerReferences'][0]['kind'] == OWNER_KIND
    assert obj['metadata']['ownerReferences'][0]['name'] == OWNER_NAME
    assert obj['metadata']['ownerReferences'][0]['uid'] == OWNER_UID


def test_appending_to_multiple_objects(multicls):
    obj1 = {}
    obj2 = {}
    objs = multicls([obj1, obj2])

    kopf.append_owner_reference(objs, owner=Body(OWNER))

    assert isinstance(obj1['metadata']['ownerReferences'], list)
    assert len(obj1['metadata']['ownerReferences']) == 1
    assert obj1['metadata']['ownerReferences'][0]['apiVersion'] == OWNER_API_VERSION
    assert obj1['metadata']['ownerReferences'][0]['kind'] == OWNER_KIND
    assert obj1['metadata']['ownerReferences'][0]['name'] == OWNER_NAME
    assert obj1['metadata']['ownerReferences'][0]['uid'] == OWNER_UID

    assert isinstance(obj2['metadata']['ownerReferences'], list)
    assert len(obj2['metadata']['ownerReferences']) == 1
    assert obj2['metadata']['ownerReferences'][0]['apiVersion'] == OWNER_API_VERSION
    assert obj2['metadata']['ownerReferences'][0]['kind'] == OWNER_KIND
    assert obj2['metadata']['ownerReferences'][0]['name'] == OWNER_NAME
    assert obj2['metadata']['ownerReferences'][0]['uid'] == OWNER_UID


def test_appending_deduplicates_by_uid():
    """
    The uid is the only necessary criterion to identify same objects.
    No matter how we change the irrelevant non-id fields, they must be ignored.
    """
    owner1 = copy.deepcopy(OWNER)
    owner2 = copy.deepcopy(OWNER)
    owner3 = copy.deepcopy(OWNER)
    owner1['kind'] = 'KindA'
    owner2['kind'] = 'KindA'
    owner3['kind'] = 'KindB'
    owner1['metadata']['name'] = 'name-a'
    owner2['metadata']['name'] = 'name-b'
    owner3['metadata']['name'] = 'name-b'
    owner1['metadata']['uid'] = 'uid-0'
    owner2['metadata']['uid'] = 'uid-0'
    owner3['metadata']['uid'] = 'uid-0'
    obj = {}

    kopf.append_owner_reference(obj, owner=Body(owner1))
    kopf.append_owner_reference(obj, owner=Body(owner2))
    kopf.append_owner_reference(obj, owner=Body(owner3))

    assert len(obj['metadata']['ownerReferences']) == 1
    assert obj['metadata']['ownerReferences'][0]['uid'] == 'uid-0'


def test_appending_distinguishes_by_uid():
    """
    Changing only the uid should be sufficient to consider a new owner.
    Here, all other non-id fields are the same, and must be ignored.
    """
    owner1 = copy.deepcopy(OWNER)
    owner2 = copy.deepcopy(OWNER)
    owner1['metadata']['uid'] = 'uid-a'
    owner2['metadata']['uid'] = 'uid-b'
    obj = {}

    kopf.append_owner_reference(obj, owner=Body(owner1))
    kopf.append_owner_reference(obj, owner=Body(owner2))

    uids = {ref['uid'] for ref in obj['metadata']['ownerReferences']}
    assert uids == {'uid-a', 'uid-b'}


def test_removal_from_dict():
    obj = {}

    kopf.append_owner_reference(obj, owner=Body(OWNER))  # assumed to work, tested above
    kopf.remove_owner_reference(obj, owner=Body(OWNER))  # this one is being tested here

    assert 'metadata' in obj
    assert 'ownerReferences' in obj['metadata']
    assert isinstance(obj['metadata']['ownerReferences'], list)
    assert len(obj['metadata']['ownerReferences']) == 0


def test_removal_from_multiple_objects(multicls):
    obj1 = {}
    obj2 = {}
    objs = multicls([obj1, obj2])

    kopf.append_owner_reference(objs, owner=Body(OWNER))  # assumed to work, tested above
    kopf.remove_owner_reference(objs, owner=Body(OWNER))  # this one is being tested here

    assert 'metadata' in obj1
    assert 'ownerReferences' in obj1['metadata']
    assert isinstance(obj1['metadata']['ownerReferences'], list)
    assert len(obj1['metadata']['ownerReferences']) == 0

    assert 'metadata' in obj2
    assert 'ownerReferences' in obj2['metadata']
    assert isinstance(obj2['metadata']['ownerReferences'], list)
    assert len(obj2['metadata']['ownerReferences']) == 0


def test_removal_identifies_by_uid():
    owner1 = copy.deepcopy(OWNER)
    owner2 = copy.deepcopy(OWNER)
    owner3 = copy.deepcopy(OWNER)
    owner1['kind'] = 'KindA'
    owner2['kind'] = 'KindA'
    owner3['kind'] = 'KindB'
    owner1['metadata']['name'] = 'name-a'
    owner2['metadata']['name'] = 'name-b'
    owner3['metadata']['name'] = 'name-b'
    owner1['metadata']['uid'] = 'uid-0'
    owner2['metadata']['uid'] = 'uid-0'
    owner3['metadata']['uid'] = 'uid-0'
    obj = {}

    # Three different owners added, but all have the same uid.
    # One is removed and only once, all must be gone (due to same uids).
    kopf.append_owner_reference(obj, owner=Body(owner1))  # assumed to work, tested above
    kopf.append_owner_reference(obj, owner=Body(owner2))  # assumed to work, tested above
    kopf.append_owner_reference(obj, owner=Body(owner3))  # assumed to work, tested above
    kopf.remove_owner_reference(obj, owner=Body(owner1))  # this one is being tested here

    assert len(obj['metadata']['ownerReferences']) == 0


def test_removal_distinguishes_by_uid():
    owner1 = copy.deepcopy(OWNER)
    owner2 = copy.deepcopy(OWNER)
    owner3 = copy.deepcopy(OWNER)
    owner1['metadata']['uid'] = 'uid-a'
    owner2['metadata']['uid'] = 'uid-b'
    owner3['metadata']['uid'] = 'uid-c'
    obj = {}

    # Three very similar owners added, different only by uid.
    # One is removed, others must stay (even if kinds/names are the same).
    kopf.append_owner_reference(obj, owner=Body(owner1))  # assumed to work, tested above
    kopf.append_owner_reference(obj, owner=Body(owner2))  # assumed to work, tested above
    kopf.append_owner_reference(obj, owner=Body(owner3))  # assumed to work, tested above
    kopf.remove_owner_reference(obj, owner=Body(owner1))  # this one is being tested here

    uids = {ref['uid'] for ref in obj['metadata']['ownerReferences']}
    assert uids == {'uid-b', 'uid-c'}

#
# Not related to owner references only, but uses the OWNER constants.
#

def test_adopting(mocker):
    # These methods are tested in their own tests.
    # We just check that they are called at all.
    append_owner_ref = mocker.patch('kopf.toolkits.hierarchies.append_owner_reference')
    harmonize_naming = mocker.patch('kopf.toolkits.hierarchies.harmonize_naming')
    adjust_namespace = mocker.patch('kopf.toolkits.hierarchies.adjust_namespace')
    label = mocker.patch('kopf.toolkits.hierarchies.label')

    obj = Mock()
    kopf.adopt(obj, owner=Body(OWNER), nested=['template'])

    assert append_owner_ref.called
    assert harmonize_naming.called
    assert adjust_namespace.called
    assert label.called

    assert append_owner_ref.call_args_list == [call(obj, owner=Body(OWNER))]
    assert harmonize_naming.call_args_list == [call(obj, name=OWNER_NAME)]
    assert adjust_namespace.call_args_list == [call(obj, namespace=OWNER_NAMESPACE)]
    assert label.call_args_list == [call(obj, labels=OWNER_LABELS, nested=['template'])]
