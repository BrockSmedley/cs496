import connexion
import six
import json
from google.cloud import datastore

from swagger_server.models.boat import Boat  # noqa: E501
from swagger_server import util


def decode_body(body):
    # decode binary data from body into a dict
    bs = body.decode('utf8')
    bj = json.loads(bs)
    return bj

def get_key(kind, iid):
    client = datastore.Client()
    return client.key(kind, iid)

def add_boat(body):  # noqa: E501
    """Add a new boat to the marina

     # noqa: E501

    :param body: Boat object that needs to be added to the marina
    :type body: dict | bytes

    :rtype: None
    """

    bj = decode_body(body)
    
    # create entity key
    client = datastore.Client()
    boat_key = get_key("boat", bj['id'])

    boat = datastore.Entity(key = boat_key)
    boat['name'] = bj['name']
    boat['length'] = bj['length']
    boat['at_sea'] = True
    boat['type'] = bj['type']

    client.put(boat)
    print ("saved boat")


    return bj['id']

def delete_boat(boatId):  # noqa: E501
    """Deletes a boat

     # noqa: E501

    :param boatId: Boat id to delete
    :type boatId: string

    :rtype: None
    """
    
    print (boatId)

    client = datastore.Client()
    boat_key = get_key("boat", boatId)
    
    client.delete(boat_key)

    return ("boat deleted; id: %s" % boatId)


def find_boats_by_status(status):  # noqa: E501
    """Finds boats by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Boat]
    """
    client = datastore.Client()
    query = client.query(kind="boat")

    # convert status to boolean
    if (status[0] == 'at_sea'):
        at_sea = True
    elif (status[0] == 'docked'):
        at_sea = False

    # build query & fetch results
    query.add_filter('at_sea', '=', at_sea)
    query_iter = query.fetch()
    out = []
    for ent in query_iter:
        out.append(ent)

    return str(out)


def get_boat_by_id(boatId):  # noqa: E501
    """Find boat by ID

    Returns a single boat # noqa: E501

    :param boatId: ID of boat to return
    :type boatId: int

    :rtype: Boat
    """
    client = datastore.Client()
    boat_key = get_key("boat", boatId)

    return client.get(boat_key)


def update_boat(body):  # noqa: E501
    """Update an existing boat

     # noqa: E501

    :param body: Boat object that needs to be updated
    :type body: dict | bytes

    :rtype: None
    """
#    if connexion.request.is_json:
#        body = Boat.from_dict(connexion.request.get_json())  # noqa: E501
    
    client = datastore.Client()
    bj = decode_body(body)
    boatId = bj['id']

    boat_key = get_key("boat", boatId)

    boat = datastore.Entity(key = boat_key)
    boat['name'] = bj['name']
    boat['length'] = bj['length']
    boat['at_sea'] = True
    boat['type'] = bj['type']

    client.put(boat)
    print ("saved boat")


    return bj['id']
