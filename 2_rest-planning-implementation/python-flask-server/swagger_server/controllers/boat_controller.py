import connexion
import six

from swagger_server.models.boat import Boat  # noqa: E501
from swagger_server import util


def add_boat(body):  # noqa: E501
    """Add a new boat to the marina

     # noqa: E501

    :param body: Boat object that needs to be added to the marina
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Boat.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_boat(boatId):  # noqa: E501
    """Deletes a boat

     # noqa: E501

    :param boatId: Boat id to delete
    :type boatId: int

    :rtype: None
    """
    return 'do some magic!'


def find_boats_by_status(status):  # noqa: E501
    """Finds boats by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Boat]
    """
    return 'do some magic!'


def get_boat_by_id(boatId):  # noqa: E501
    """Find boat by ID

    Returns a single boat # noqa: E501

    :param boatId: ID of boat to return
    :type boatId: int

    :rtype: Boat
    """
    return 'do some magic!'


def update_boat(body):  # noqa: E501
    """Update an existing boat

     # noqa: E501

    :param body: Boat object that needs to be updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Boat.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
