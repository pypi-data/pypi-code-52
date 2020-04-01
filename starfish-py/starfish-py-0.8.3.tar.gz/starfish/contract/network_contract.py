"""

    DIDRegistry Contract

"""

import logging

from starfish.contract.contract_base import ContractBase

logger = logging.getLogger(__name__)

CONTRACT_NAME = 'Network'


class NetworkContract(ContractBase):
    """

    Class representing a network contract, that does not access any actual underling contract, but does network based
    tasks.

    """

    def __init__(self):
        ContractBase.__init__(self, CONTRACT_NAME)

    def get_balance(self, account_address):

        address = self.get_account_address(account_address)
        amount_wei = self._web3.eth.getBalance(address, block_identifier='latest')
        return self.to_ether(amount_wei)

    def send_ether(self, account, to_account_address, amount):

        amount_wei = self.to_wei(amount)
        to_address = self.get_account_address(to_account_address)

        gas_transact = {
            'from': account.address,
            'to': to_address,
            'value': amount_wei,
        }
        transaction = {
            'from': account.address,
            'to':  to_address,
            'value': amount_wei,
            'gas': self._web3.eth.estimateGas(gas_transact),
            'gasPrice':  self.get_gas_price(account.address),
            'nonce': self.get_nonce(account.address),
        }
        signed = account.sign_transaction(self._web3, transaction)
        tx_hash = None
        if signed:
            tx_hash = self._web3.eth.sendRawTransaction(signed.rawTransaction)

        return tx_hash
