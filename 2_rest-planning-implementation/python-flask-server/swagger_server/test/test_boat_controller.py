# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.boat import Boat  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBoatController(BaseTestCase):
    """BoatController integration test stubs"""

    def test_add_boat(self):
        """Test case for add_boat

        Add a new boat to the marina
        """
        body = Boat()
        response = self.client.open(
            '/v1/boat',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_boat(self):
        """Test case for delete_boat

        Deletes a boat
        """
        response = self.client.open(
            '/v1/boat/{boatId}'.format(boatId=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_boats_by_status(self):
        """Test case for find_boats_by_status

        Finds boats by status
        """
        query_string = [('status', 'at_sea')]
        response = self.client.open(
            '/v1/boat/findByStatus',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_boat_by_id(self):
        """Test case for get_boat_by_id

        Find boat by ID
        """
        response = self.client.open(
            '/v1/boat/{boatId}'.format(boatId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_boat(self):
        """Test case for update_boat

        Update an existing boat
        """
        body = Boat()
        response = self.client.open(
            '/v1/boat',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
