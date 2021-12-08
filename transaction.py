import requests
import json

from confidence_info import w_address, url, auth, wifs
from network import network
from pycoin.coins.tx_utils import create_signed_tx
from pycoin.services.agent import urlopen
from pycoin.coins.bitcoin.Spendable import Spendable
from pycoin.encoding.hexbytes import h2b



def get_address(url, auth):
    headers = {'content-type': 'application/json'}
    request = {"method": "getnewaddress"}

    response = requests.post(url, auth=auth, data=json.dumps(request), headers=headers).json()
    address = response["result"]
    return address


def spendables_for_my_wallet(w_address):
    URL = "https://bcschain.info/api/address/%s/utxo" % w_address
    r = json.loads(urlopen(URL).read().decode("utf8"))
    r = r[0]
    spendables = []

    coin_value = r["value"]
    script = h2b(r["scriptPubKey"])
    previous_hash = h2b(r["transactionId"])
    previous_hash = previous_hash[::-1]
    previous_index = r["outputIndex"]

    spendables.append(Spendable(coin_value, script, previous_hash, previous_index))
    return spendables


def form_transaction(address, spendables, wifs):
    to_address = address
    spendables = spendables[0]

    tx = create_signed_tx(network, [spendables], [to_address], wifs, fee=76800)
    tx_hex = tx.as_hex()
    return tx_hex
    

def send_transaction(url, auth, tx_hex):
    headers = {'content-type': 'application/json'}
    request = {"method": "sendrawtransaction", 
               "params": [tx_hex]}

    response = requests.post(url, auth=auth, data=json.dumps(request), headers=headers).json()
    return response




address = get_address(url, auth)
spendables = spendables_for_my_wallet(w_address)
tx_hex = form_transaction(address, spendables, wifs)

print(send_transaction(url, auth, tx_hex))


    
