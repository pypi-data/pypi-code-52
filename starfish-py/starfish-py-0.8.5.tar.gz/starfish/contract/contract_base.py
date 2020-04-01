"""

    Contactt Base

"""

nonce_list = {}

GAS_MINIMUM = 200000


class ContractBase:

    def __init__(self, name):
        self._name = name
        self._web3 = None
        self._abi = None
        self._address = None
        self._contract = None

    def load(self, web3, abi=None, address=None):
        self._web3 = web3
        self._abi = abi
        self._address = address
        self._contract = None
        if abi and address:
            self._contract = self._web3.eth.contract(
                address=address,
                abi=abi
            )

    def call(self, function_name, parameters, account=None, transact=None):
        if self._contract is None:
            raise ValueError('contract not loaded')

        if not isinstance(parameters, (list, tuple)):
            parameters = (parameters,)

        contract_function_call = self._contract.functions[function_name](*parameters)
        if account:
            result = self._call_as_transaction(contract_function_call, account, transact)
            if result is None:
                raise ValueError(f'unable to sign a transaciton for {self.name}:{function_name}')
        else:
            result = contract_function_call.call()
        return result

    def get_event(self, event_name, parameters=None):
        if self._contract is None:
            raise ValueError('contract not loaded')
        return self._contract.events[event_name]

    def create_event_filter(self, event_name, parameters=None, from_block=1, argument_filters=None):
        event = self.get_event(event_name, parameters)
        if event:
            return event.createFilter(
                fromBlock=from_block,
                argument_filters=argument_filters
            )
        return None

    def _call_as_transaction(self, contract_function_call, account, transact=None):
        if transact is None:
            gas_transact = {
                'from': account.address
            }
            gas = contract_function_call.estimateGas(gas_transact)
            transact = {
                'from': account.address,
                'gas': gas,
                'nonce': self.get_nonce(account.address)
            }

        built_transaction = contract_function_call.buildTransaction(transact)
        transaction = {
            'from': account.address,
            'to': built_transaction['to'],
            'gas': built_transaction['gas'],
            'data': built_transaction['data'],
            'gasPrice':  self.get_gas_price(account.address),
            'nonce':  built_transaction['nonce'],
        }
        signed = account.sign_transaction(self._web3, transaction)
        tx_hash = None
        if signed:
            tx_hash = self._web3.eth.sendRawTransaction(signed.rawTransaction)

        return tx_hash

    def wait_for_receipt(self, tx_hash, timeout=30):
        self._web3.eth.waitForTransactionReceipt(tx_hash, timeout=timeout)
        return self._web3.eth.getTransactionReceipt(tx_hash)

    def get_nonce(self, address):
        global nonce_list
        nonce = self._web3.eth.getTransactionCount(address)
        if address not in nonce_list:
            nonce_list[address] = nonce
        else:
            if nonce <= nonce_list[address]:
                nonce = nonce_list[address] + 1
        return nonce

    def get_gas_price(self, address):
        block = self._web3.eth.getBlock("latest")
        gas_price = int(self._web3.eth.gasPrice / 100)
        gas_price = min(block.gasLimit, gas_price)
        gas_price = max(GAS_MINIMUM, gas_price)
        return gas_price

    def unlockAccount(self, account):
        self._web3.personal.unlockAccount(account.address, account.password)

    def lockAccount(self, account):
        self._web3.personal.lockAccount(account.address, account.password)

    @property
    def name(self):
        return self._name

    @property
    def web3(self):
        return self._web3

    @property
    def address(self):
        return self._address

    def to_wei(self, amount_ether):
        return self._web3.toWei(amount_ether, 'ether')

    def to_ether(self, amount_wei):
        return self._web3.fromWei(amount_wei, 'ether')

    def get_account_address(self, account_address):
        address = account_address
        if hasattr(account_address, 'address'):
            address = account_address.address

        if not self.web3.isChecksumAddress(address):
            address = self.web3.toChecksumAddress(address)

        return address
