import connexion
import six

from swagger_server.models.slip import Slip  # noqa: E501
from swagger_server import util

from google.cloud import datastore
from util import util as mutil

def is_valid_slip_number(num):
    client = datastore.Client()
    query = client.query(kind="slip")
    query.add_filter('number', '=', num)
    qi = query.fetch()

    for i in qi:
        return False
    return True

def add_slip(body):  # noqa: E501
    """Add a new slip to the marina

     # noqa: E501

    :param body: Slip object that needs to be added to the marina
    :type body: dict | bytes

    :rtype: None
    """
#    if connexion.request.is_json:
#        body = Slip.from_dict(connexion.request.get_json())  # noqa: E501

    client = datastore.Client()
    bj = mutil.decode_body(body)
    keystr = mutil.generate_id()
    slip_key = mutil.get_key("slip", keystr)

    slip = datastore.Entity(key = slip_key)
    slip['arrival_date'] = ""
    slip['id'] = keystr
    num = bj['number']
    while (not is_valid_slip_number(num)):
        num += 1
    slip['number'] = num
    slip['current_boat'] = ""

    client.put(slip)

    return slip

def delete_slip(slipId):  # noqa: E501
    """Deletes a slip

     # noqa: E501

    :param slipId: Slip id to delete
    :type slipId: string

    :rtype: None
    """

    client = datastore.Client()
    slip_key = mutil.get_key("slip", slipId)
    if (slip_key):
        slip = client.get(slip_key)
    else:
        return ("%s does not exist" % slipId)
    
    # send out boat to sea before slip delete
    if (slip['current_boat'] and slip['current_boat'] != ""):
        boat_key = mutil.get_key("boat", slip['current_boat'])
        if (boat_key):
            boat = client.get(boat_key)
            boat['at_sea'] = True
            client.put(boat)

    client.delete(slip_key)
    return ('deleted slip %s' % slipId)


def get_slip_by_id(slipId):  # noqa: E501
    """Check slip by number

    Returns boat occupying a slip # noqa: E501

    :param slipId: ID of slip to return
    :type slipId: str

    :rtype: Slip
    """

    client = datastore.Client()
    query = client.query(kind='slip')
    query.add_filter('number', '=', int(slipId))
    qi = query.fetch()

    for i in qi:
        return i

def get_slips():  # noqa: E501
    """Returns slips by status

    Returns a map of status codes to slips # noqa: E501


    :rtype: Dict[str, int]
    """
    client = datastore.Client()
    query = client.query(kind='slip')
    qi = query.fetch()

    out = []
    for i in qi:
        out.append(i)
    return out


def update_slip(body):  # noqa: E501
    """Update an existing slip

     # noqa: E501

    :param body: Slip object that needs to be updated
    :type body: dict | bytes

    :rtype: None
    """
#    if connexion.request.is_json:
#        body = Slip.from_dict(connexion.request.get_json())  # noqa: E501

    client = datastore.Client()

    bj = mutil.decode_body(body)
    arr = bj['arrival_date']
    cbt = bj['current_boat']
    iid = bj['id']

    # update the slip
    slip_key = mutil.get_key("slip", iid)
    sent = client.get(slip_key)
    if (sent['current_boat'] != ""):
        return ("403: Slip is occupied")
    sent['arrival_date'] = arr
    sent['current_boat'] = cbt
    client.put(sent)

    if (cbt != "" and arr != ""):
        boat_key = mutil.get_key("boat", cbt)
        
        # update boat status
        bent = client.get(boat_key)
        bent['at_sea'] = False

        client.put(bent)

    return sent
