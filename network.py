from pycoin.networks.bitcoinish import create_bitcoinish_network

network = create_bitcoinish_network(symbol="BCS", network_name="BCS Chain", subnet_name="mainnet",
                                    wif_prefix_hex="80", address_prefix_hex="19",
                                    pay_to_script_prefix_hex="32", bip32_prv_prefix_hex="0488ade4",
                                    bip32_pub_prefix_hex="0488B21E", bech32_hrp="bc", bip49_prv_prefix_hex="049d7878",
                                    bip49_pub_prefix_hex="049D7CB2", bip84_prv_prefix_hex="04b2430c",
                                    bip84_pub_prefix_hex="04B24746", magic_header_hex="F1CFA6D3", default_port=3666)