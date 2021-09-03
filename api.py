import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests

access_key = ""
secret_key = ""

file_key = open("keys.txt",'r')

access_key= file_key.readline().strip("\n")
secret_key= file_key.readline().strip("\n")
server_url= "https://api.upbit.com"
print(f"access:{access_key},secret:{secret_key}")
def get_balance():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/accounts", headers=headers)
    return res.json()
def get_currency_balance(_currency):
    json_ = get_balance()
    print(len(json_))
    for i in range(len(json_)):
        if json_[i]['currency'] == _currency:
            return json_[i]['balance']

def buy(_ticker,_buy_amount): #매수
# ex) _ticker: krw-xrp, _buy_amount:10000 won
    query = {
        'market': str(_ticker),
        'side': 'bid',
        'price': str(_buy_amount),
        'ord_type': 'price',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
    return res.json()
def sell(_ticker,_sell_amount,_sell_price):
    query = {
        'market': str(_ticker,),
        'side': 'ask',
        'volume': str(_sell_amount),
        'price': str(_sell_price),
        'ord_type': 'limit',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
    return res.json()
def get_order(_uuid):
    query = {
        'uuid': str(_uuid),
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/order", params=query, headers=headers)


    return res.json()
def get_order_state(_uuid):
    return get_order(_uuid)['state']
def get_holds():
    account_info = get_balance()
    for i in range(len(account_info)):
        print(account_info[i]['currency']+": "+account_info[i]['balance'] +" + "+ account_info[i]['locked'])