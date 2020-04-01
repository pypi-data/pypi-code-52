"""Helpers for creating actions on eosio contract"""
from aioeos.types import EosAction


def newaccount(
    creator, account_name, owner_keys, active_keys=None, authorization=[]
) -> EosAction:
    active_keys = owner_keys if not active_keys else active_keys
    return EosAction(
        account='eosio',
        name='newaccount',
        authorization=authorization,
        data={
            'creator': creator,
            'name': account_name,
            'owner': owner_keys,
            'active': active_keys
        }
    )


def buyrambytes(payer, receiver, amount, authorization=[]) -> EosAction:
    return EosAction(
        account='eosio',
        name='buyrambytes',
        authorization=authorization,
        data={
            'payer': payer,
            'receiver': receiver,
            'bytes': amount
        }
    )


def sellram(account, amount, authorization=[]) -> EosAction:
    return EosAction(
        account='eosio',
        name='sellram',
        authorization=authorization,
        data={
            'account': account,
            'bytes': amount
        }
    )


def delegatebw(
    from_account, receiver, stake_net_quantity, stake_cpu_quantity,
    transfer=False, authorization=[]
) -> EosAction:
    return EosAction(
        account='eosio',
        name='delegatebw',
        authorization=authorization,
        data={
            'from': from_account,
            'receiver': receiver,
            'stake_net_quantity': stake_net_quantity,
            'stake_cpu_quantity': stake_cpu_quantity,
            'transfer': transfer
        }
    )


def undelegatebw(
    from_account, receiver, unstake_net_quantity, unstake_cpu_quantity,
    authorization=[]
) -> EosAction:
    return EosAction(
        account='eosio',
        name='undelegatebw',
        authorization=authorization,
        data={
            'from': from_account,
            'receiver': receiver,
            'unstake_net_quantity': unstake_net_quantity,
            'unstake_cpu_quantity': unstake_cpu_quantity,
        }
    )
