import connexion
import six

from swagger_server.models.slip import Slip  # noqa: E501
from swagger_server import util


def add_slip(body):  # noqa: E501
    """Add a new slip to the marina

     # noqa: E501

    :param body: Slip object that needs to be added to the marina
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Slip.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_slip(slipId):  # noqa: E501
    """Deletes a slip

     # noqa: E501

    :param slipId: Slip id to delete
    :type slipId: int

    :rtype: None
    """
    return 'do some magic!'


def get_slip_by_id(slipId):  # noqa: E501
    """Check slip by ID

    Returns boat occupying a slip # noqa: E501

    :param slipId: ID of slip to return
    :type slipId: str

    :rtype: Slip
    """
    return 'do some magic!'


def get_slips():  # noqa: E501
    """Returns slips by status

    Returns a map of status codes to slips # noqa: E501


    :rtype: Dict[str, int]
    """
    return 'do some magic!'


def update_slip(body):  # noqa: E501
    """Update an existing slip

     # noqa: E501

    :param body: Slip object that needs to be updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Slip.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
