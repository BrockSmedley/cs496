import json
from google.cloud import datastore
import random
import string

def decode_body(body):
    # decode binary data from body into a dict
    bs = body.decode('utf8')
    bj = json.loads(bs)
    return bj

def get_key(kind, iid):
    client = datastore.Client()
    return client.key(kind, iid)

def generate_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(8))

