import os

from metacase.adapters.polarion.polarion_adapter import PolarionAdapter
from metacase.adapters.polarion.polarion_test_case import PolarionTestCase

"""
This example fetches all FMF test cases found at ../test directory containing
"test_path" as part of their names, then it will use the FMF Polarion Adapter
to convert into a polarion test case. When the submit_testcase method is called,
the test case will be printed as an XML to the stdout.
"""

# Loading FMF Tree from ../tests
polarion = PolarionAdapter(os.path.dirname(os.path.abspath(__file__)) + "/../test")

# Listing all test cases found and containing "test_path" in their names
test_cases = [tc for tc in polarion.get_testcases_matching("test_path")]

# List all test case names and their content
polarion.submit_testcases(test_cases)
