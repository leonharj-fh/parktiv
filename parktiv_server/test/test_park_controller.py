# coding: utf-8

from parktiv_server.test import BaseTestCase

class TestParkController(BaseTestCase):
    """ParkController integration test stubs"""

    def test_animals_memory_random_get(self):
        """Test case for animals_memory_random_get

        Retrieve a random list of animal ids
        """
        query_string = [('size', 2)]
        headers = [('Accept_Language', 'Accept_Language_example')]
        response = self.client.open(
            '/parktiv/animals/memory/random',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        jsonData = response.get_json()
        assert type(jsonData) == list
        assert len(jsonData) == 4
        assert len(set(jsonData)) == 2


    def test_get_animal(self):
        """Test case for get_animal

        Get a specific animal including the task
        """
        headers = [('Accept_Language', 'Accept_Language_example')]
        response = self.client.open(
            '/parktiv/animals/{identifier}/task/{roleId}'.format(identifier='elephant', roleId='faenger'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_animal(self):
        """Test case for list_animal

        List of all available animals with exercises
        """
        headers = [('Accept_Language', 'Accept_Language_example')]
        response = self.client.open(
            '/parktiv/animals',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        jsonData = response.get_json()

    def test_list_park(self):
        """Test case for list_park

        List of parks containing a QR-Code
        """
        headers = [('Accept_Language', 'Accept_Language_example')]
        response = self.client.open(
            '/parktiv/parks',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_roles_get(self):
        """Test case for roles_get

        List of roles which can be chosen to complete different exersices
        """
        headers = [('Accept_Language', 'Accept_Language_example')]
        response = self.client.open(
            '/parktiv/roles',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
