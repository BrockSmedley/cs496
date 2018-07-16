import connexion
import six
import json
from google.cloud import datastore

from util import util as mutil

from swagger_server.models.boat import Boat  # noqa: E501
from swagger_server import util


def add_boat(body):  # noqa: E501
    """Add a new boat to the marina

     # noqa: E501

    :param body: Boat object that needs to be added to the marina
    :type body: dict | bytes

    :rtype: None
    """

    bj = mutil.decode_body(body)
    
    # create entity key
    client = datastore.Client()
    keystr = mutil.generate_id()
    boat_key = mutil.get_key("boat", keystr)

    boat = datastore.Entity(key = boat_key)
    boat['name'] = bj['name']
    boat['length'] = bj['length']
    boat['at_sea'] = True
    boat['type'] = bj['type']
    boat['id'] = keystr;

    client.put(boat)
    print ("saved boat")


    return boat

def delete_boat(boatId):  # noqa: E501
    """Deletes a boat

     # noqa: E501

    :param boatId: Boat id to delete
    :type boatId: string

    :rtype: None
    """
    
    client = datastore.Client()
    boat_key = mutil.get_key("boat", boatId)

    # find slip assoc. with boat
    query = client.query(kind="slip")
    query.add_filter('current_boat', '=', boatId)

    qi = query.fetch()
    for i in qi:
        i['current_boat'] = ""
        client.put(i)
    
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

    return out


def get_boat_by_id(boatId):  # noqa: E501
    """Find boat by ID

    Returns a single boat # noqa: E501

    :param boatId: ID of boat to return
    :type boatId: int

    :rtype: Boat
    """
    client = datastore.Client()
    boat_key = mutil.get_key("boat", boatId)

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
    bj = mutil.decode_body(body)
    boatId = bj['id']

    boat_key = mutil.get_key("boat", boatId)

    boat = datastore.Entity(key = boat_key)
    boat['name'] = bj['name']
    boat['length'] = bj['length']
    boat['at_sea'] = True
    boat['type'] = bj['type']

    client.put(boat)
    print ("saved boat")


    return bj['id']
