import os
import unittest

from mindsdb.integrations.handlers.hubspot_handler.hubspot_handler import HubspotHandler
from mindsdb.api.executor.data_types.response_type import RESPONSE_TYPE


class HubSpotHandlerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        sets up class-level variables for connection data and creates an instance
        of a custom class (`HubspotHandler`) with the specified connection data.

        Args:
            cls (instance/class object of class `HubspotHandler`.): class being
                setup, providing a dictionary of keyword arguments to be used when
                initializing an instance of that class through the `setUpClass()`
                function call.
                
                	1/ `kwargs`: A dictionary containing connection data, with
                `access_token` as its sole key, which is set to an environment
                variable named `ACCESS_TOKEN`.
                	2/ `handler`: An instance of the `HubspotHandler` class, created
                with the name `'test_hubspot_handler'` and the connection data
                from `kwargs` as its arguments.
                

        """
        cls.kwargs = {
            "connection_data": {
                "access_token": os.environ.get('ACCESS_TOKEN')
            }
        }
        cls.handler = HubspotHandler('test_hubspot_handler', **cls.kwargs)

    def test_0_check_connection(self):
        assert self.handler.check_connection()

    def test_1_get_tables(self):
        """
        retrieves a list of tables from an API handler, checks if it's not an error
        response, and asserts that it is not.

        """
        tables = self.handler.get_tables()
        assert tables.type is not RESPONSE_TYPE.ERROR

    def test_2_select_companies_query(self):
        """
        performs a SQL query to retrieve all data from the `companies` table in
        the `test_hubspot_handler` database.

        """
        query = "SELECT * FROM test_hubspot_handler.companies"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE

    def test_3_select_contacts_query(self):
        """
        retrieves contacts data from HubSpot using a native query.

        """
        query = "SELECT * FROM test_hubspot_handler.contacts"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE

    def test_4_select_deals_query(self):
        """
        selects all deals from a table in HubSpot using a native query and validates
        that the result is a table with the correct type.

        """
        query = "SELECT * FROM test_hubspot_handler.deals"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE
