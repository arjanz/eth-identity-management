# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from populus import migrations


class Migration(migrations.Migration):

    migration_id = b'0002_auto'
    dependencies = [
        b'0001_initial',
    ]
    operations = []
    compiled_contracts = {
        'Greeter': {
            b'abi': [
                {
                    'constant': False,
                    'inputs': [
                        {
                            'name': '_greeting',
                            'type': 'string',
                        },
                    ],
                    'name': 'setGreeting',
                    'outputs': [],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': True,
                    'inputs': [],
                    'name': 'greet',
                    'outputs': [
                        {
                            'name': '',
                            'type': 'string',
                        },
                    ],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': True,
                    'inputs': [],
                    'name': 'greeting',
                    'outputs': [
                        {
                            'name': '',
                            'type': 'string',
                        },
                    ],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'inputs': [],
                    'type': 'constructor',
                },
            ],
            b'code': '0x60a060405260056060527f48656c6c6f000000000000000000000000000000000000000000000000000000608052600080548180527f48656c6c6f00000000000000000000000000000000000000000000000000000a825560b0907f290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e563602060026001841615610100026000190190931692909204601f01919091048101905b8082111560c05760008155600101609e565b50506102ce806100c46000396000f35b509056606060405260e060020a6000350463a41368628114610034578063cfae3217146100ea578063ef690cc014610158575b610002565b34610002576101bd6004808035906020019082018035906020019191908080601f016020809104026020016040519081016040528093929190818152602001838380828437509496505050505050508060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061022d57805160ff19168380011785555b5061025d9291505b8082111561026257600081556001016100d6565b3461000257604080516020808201835260008083528054845160026001831615610100026000190190921691909104601f81018490048402820184019095528481526101bf9490928301828280156102915780601f1061026657610100808354040283529160200191610291565b34610002576101bf60008054604080516020601f600260001961010060018816150201909516949094049384018190048102820181019092528281529291908301828280156102c65780601f1061029b576101008083540402835291602001916102c6565b005b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f16801561021f5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b828001600101855582156100ce579182015b828111156100ce57825182600050559160200191906001019061023f565b505050565b5090565b820191906000526020600020905b81548152906001019060200180831161027457829003601f168201915b5050505050905090565b820191906000526020600020905b8154815290600101906020018083116102a957829003601f168201915b50505050508156',
            b'code_runtime': '0x606060405260e060020a6000350463a41368628114610034578063cfae3217146100ea578063ef690cc014610158575b610002565b34610002576101bd6004808035906020019082018035906020019191908080601f016020809104026020016040519081016040528093929190818152602001838380828437509496505050505050508060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061022d57805160ff19168380011785555b5061025d9291505b8082111561026257600081556001016100d6565b3461000257604080516020808201835260008083528054845160026001831615610100026000190190921691909104601f81018490048402820184019095528481526101bf9490928301828280156102915780601f1061026657610100808354040283529160200191610291565b34610002576101bf60008054604080516020601f600260001961010060018816150201909516949094049384018190048102820181019092528281529291908301828280156102c65780601f1061029b576101008083540402835291602001916102c6565b005b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f16801561021f5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b828001600101855582156100ce579182015b828111156100ce57825182600050559160200191906001019061023f565b505050565b5090565b820191906000526020600020905b81548152906001019060200180831161027457829003601f168201915b5050505050905090565b820191906000526020600020905b8154815290600101906020018083116102a957829003601f168201915b50505050508156',
            b'meta': {
                b'compilerVersion': 'Version: 0.4.4+commit.4633f3de.Darwin.appleclang\n',
                b'language': b'Solidity',
            },
            b'source': None,
        },
        'IdentityRegistry': {
            b'abi': [
                {
                    'constant': False,
                    'inputs': [
                        {
                            'name': 'emailAddress',
                            'type': 'string',
                        },
                    ],
                    'name': 'removeEmailAddress',
                    'outputs': [
                        {
                            'name': 'registered',
                            'type': 'bool',
                        },
                    ],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': False,
                    'inputs': [],
                    'name': 'kill',
                    'outputs': [],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': True,
                    'inputs': [],
                    'name': 'owner',
                    'outputs': [
                        {
                            'name': '',
                            'type': 'address',
                        },
                    ],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': False,
                    'inputs': [
                        {
                            'name': 'addr',
                            'type': 'address',
                        },
                        {
                            'name': 'emailAddress',
                            'type': 'string',
                        },
                    ],
                    'name': 'verifyEmailAddress',
                    'outputs': [
                        {
                            'name': 'verified',
                            'type': 'bool',
                        },
                    ],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': False,
                    'inputs': [
                        {
                            'name': 'addr',
                            'type': 'address',
                        },
                        {
                            'name': 'emailAddress',
                            'type': 'string',
                        },
                    ],
                    'name': 'registerEmailAddress',
                    'outputs': [
                        {
                            'name': 'registered',
                            'type': 'bool',
                        },
                    ],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': False,
                    'inputs': [],
                    'name': 'mortal',
                    'outputs': [],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'anonymous': False,
                    'inputs': [
                        {
                            'indexed': False,
                            'name': 'sender',
                            'type': 'address',
                        },
                        {
                            'indexed': False,
                            'name': 'emailAddress',
                            'type': 'string',
                        },
                    ],
                    'name': 'EmailAddressRegistered',
                    'type': 'event',
                },
            ],
            b'code': '0x60606040526105dc806100126000396000f3606060405236156100565760e060020a60003504631f38034c811461005b57806341c0e1b5146101c85780638da5cb5b146101f5578063bc82f4d31461020c578063c5933658146102db578063f1eae25c14610456575b610002565b346100025761048e6004808035906020019082018035906020019191908080601f0160208091040260200160405190810160405280939291908181526020018383808284375094965050505050505060006000600260005083604051808280519060200190808383829060006004602084601f0104600302600f01f15090500191505090815260200160405180910390206000509050600060009054906101000a9004600160a060020a0316600160a060020a031633600160a060020a031614806101335750805433600160a060020a039081169116145b156101c257600260005083604051808280519060200190808383829060006004602084601f0104600302600f01f150905001915050908152602001604051809103902060006000820160006101000a815490600160a060020a03021916905560018201600050805460018160011615610100020316600290046000825580601f106104be57505b505050600191505b50919050565b346100025761048c60005433600160a060020a03908116911614156104f057600054600160a060020a0316ff5b34610002576104a2600054600160a060020a031681565b346100025760408051602060046024803582810135601f810185900485028601850190965285855261048e958335959394604494939290920191819084018382808284375094965050505050505060006000600260005083604051808280519060200190808383829060006004602084601f0104600302600f01f1509050019150509081526020016040518091039020600050905083600160a060020a03168160000160009054906101000a9004600160a060020a0316600160a060020a031614156104f257600191506104f7565b346100025760408051602060046024803582810135601f810185900485028601850190965285855261048e958335959394604494939290920191819084018382808284375094965050505050505060008054819033600160a060020a03908116911614156104f7576001600050600085600160a060020a031681526020019081526020016000206000509050604060405190810160405280858152602001848152602001508160000160005084604051808280519060200190808383829060006004602084601f0104600302600f01f150905001915050908152602001604051809103902060005060008201518160000160006101000a815481600160a060020a0302191690836c010000000000000000000000009081020402179055506020820151816001016000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106104fe57805160ff19168380011785555b5061052e9291506104d8565b34610002576000805473ffffffffffffffffffffffffffffffffffffffff19166c01000000000000000000000000338102041790555b005b604080519115158252519081900360200190f35b60408051600160a060020a039092168252519081900360200190f35b601f0160209004906000526020600020908101906101ba91905b808211156104ec57600081556001016104d8565b5090565b565b600091505b5092915050565b8280016001018555821561044a579182015b8281111561044a578251826000505591602001919060010190610510565b50509050507f1930cd24507a9ddb4c0c6f9b0b7fff91201fe41b30993d6a2412c221c764435284846040518083600160a060020a03168152602001806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156105c55780820380516001836020036101000a031916815260200191505b50935050505060405180910390a1600191506104f756',
            b'code_runtime': '0x606060405236156100565760e060020a60003504631f38034c811461005b57806341c0e1b5146101c85780638da5cb5b146101f5578063bc82f4d31461020c578063c5933658146102db578063f1eae25c14610456575b610002565b346100025761048e6004808035906020019082018035906020019191908080601f0160208091040260200160405190810160405280939291908181526020018383808284375094965050505050505060006000600260005083604051808280519060200190808383829060006004602084601f0104600302600f01f15090500191505090815260200160405180910390206000509050600060009054906101000a9004600160a060020a0316600160a060020a031633600160a060020a031614806101335750805433600160a060020a039081169116145b156101c257600260005083604051808280519060200190808383829060006004602084601f0104600302600f01f150905001915050908152602001604051809103902060006000820160006101000a815490600160a060020a03021916905560018201600050805460018160011615610100020316600290046000825580601f106104be57505b505050600191505b50919050565b346100025761048c60005433600160a060020a03908116911614156104f057600054600160a060020a0316ff5b34610002576104a2600054600160a060020a031681565b346100025760408051602060046024803582810135601f810185900485028601850190965285855261048e958335959394604494939290920191819084018382808284375094965050505050505060006000600260005083604051808280519060200190808383829060006004602084601f0104600302600f01f1509050019150509081526020016040518091039020600050905083600160a060020a03168160000160009054906101000a9004600160a060020a0316600160a060020a031614156104f257600191506104f7565b346100025760408051602060046024803582810135601f810185900485028601850190965285855261048e958335959394604494939290920191819084018382808284375094965050505050505060008054819033600160a060020a03908116911614156104f7576001600050600085600160a060020a031681526020019081526020016000206000509050604060405190810160405280858152602001848152602001508160000160005084604051808280519060200190808383829060006004602084601f0104600302600f01f150905001915050908152602001604051809103902060005060008201518160000160006101000a815481600160a060020a0302191690836c010000000000000000000000009081020402179055506020820151816001016000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106104fe57805160ff19168380011785555b5061052e9291506104d8565b34610002576000805473ffffffffffffffffffffffffffffffffffffffff19166c01000000000000000000000000338102041790555b005b604080519115158252519081900360200190f35b60408051600160a060020a039092168252519081900360200190f35b601f0160209004906000526020600020908101906101ba91905b808211156104ec57600081556001016104d8565b5090565b565b600091505b5092915050565b8280016001018555821561044a579182015b8281111561044a578251826000505591602001919060010190610510565b50509050507f1930cd24507a9ddb4c0c6f9b0b7fff91201fe41b30993d6a2412c221c764435284846040518083600160a060020a03168152602001806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156105c55780820380516001836020036101000a031916815260200191505b50935050505060405180910390a1600191506104f756',
            b'meta': {
                b'compilerVersion': 'Version: 0.4.4+commit.4633f3de.Darwin.appleclang\n',
                b'language': b'Solidity',
            },
            b'source': None,
        },
        'Mortal': {
            b'abi': [
                {
                    'constant': False,
                    'inputs': [],
                    'name': 'kill',
                    'outputs': [],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': True,
                    'inputs': [],
                    'name': 'owner',
                    'outputs': [
                        {
                            'name': '',
                            'type': 'address',
                        },
                    ],
                    'payable': False,
                    'type': 'function',
                },
                {
                    'constant': False,
                    'inputs': [],
                    'name': 'mortal',
                    'outputs': [],
                    'payable': False,
                    'type': 'function',
                },
            ],
            b'code': '0x606060405260c48060106000396000f3606060405260e060020a600035046341c0e1b5811460305780638da5cb5b14605a578063f1eae25c14606f575b6002565b3460025760a460005433600160a060020a039081169116141560c257600054600160a060020a0316ff5b3460025760a6600054600160a060020a031681565b346002576000805473ffffffffffffffffffffffffffffffffffffffff19166c01000000000000000000000000338102041790555b005b60408051600160a060020a039092168252519081900360200190f35b56',
            b'code_runtime': '0x606060405260e060020a600035046341c0e1b5811460305780638da5cb5b14605a578063f1eae25c14606f575b6002565b3460025760a460005433600160a060020a039081169116141560c257600054600160a060020a0316ff5b3460025760a6600054600160a060020a031681565b346002576000805473ffffffffffffffffffffffffffffffffffffffff19166c01000000000000000000000000338102041790555b005b60408051600160a060020a039092168252519081900360200190f35b56',
            b'meta': {
                b'compilerVersion': 'Version: 0.4.4+commit.4633f3de.Darwin.appleclang\n',
                b'language': b'Solidity',
            },
            b'source': None,
        },
    }
