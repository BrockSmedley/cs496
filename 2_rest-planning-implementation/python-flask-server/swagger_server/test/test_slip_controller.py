# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.slip import Slip  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSlipController(BaseTestCase):
    """SlipController integration test stubs"""

    def test_add_slip(self):
        """Test case for add_slip

        Add a new slip to the marina
        """
        body = Slip()
        response = self.client.open(
            '/v1/slip',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_slip(self):
        """Test case for delete_slip

        Deletes a slip
        """
        response = self.client.open(
            '/v1/slip/{slipId}'.format(slipId=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_slip_by_id(self):
        """Test case for get_slip_by_id

        Check slip by ID
        """
        response = self.client.open(
            '/v1/slip/{slipId}'.format(slipId='slipId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_slips(self):
        """Test case for get_slips

        Returns slips by status
        """
        response = self.client.open(
            '/v1/slip',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_slip(self):
        """Test case for update_slip

        Update an existing slip
        """
        body = Slip()
        response = self.client.open(
            '/v1/slip',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
