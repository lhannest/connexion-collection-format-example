# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestExampleController(BaseTestCase):
    """ ExampleController integration test stubs """

    def test_example_get(self):
        """
        Test case for example_get

        
        """
        query_string = [('multi', 'multi_example'),
                        ('csv', 'csv_example'),
                        ('pipes', 'pipes_example')]
        response = self.client.open('/example',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
