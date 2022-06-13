from metacase import TestCase
from metacase.adapter import Adapter, AdapterArgParser
import os
import pprint

"""
This is a simple example that demonstrates an FMF test case being parsed and displayed.
It fetches all test cases containing "test_path" in their names.
"""


class AdapterTest(Adapter):
    """
    Dummy implementation just for unit tests.
    """

    @staticmethod
    def adapter_id() -> str:
        return "test"

    @staticmethod
    def get_args_parser() -> AdapterArgParser:
        pass

    def convert_from(self, testcase: TestCase):
        pass

    def submit_testcase(self, testcase: TestCase):
        pass

    def submit_testcases(self, testcase: list):
        pass


adapter = AdapterTest(os.path.dirname(os.path.abspath(__file__)) + "/../test")

# Listing all test cases found and containing "test_path" in their names
test_cases = [tc for tc in adapter.get_testcases_matching("test_path")]

# List all test case names and their content
for tc in test_cases:
    print(tc.name)
    pprint.PrettyPrinter(indent=4).pprint(tc.__dict__)
