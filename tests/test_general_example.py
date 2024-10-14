import pytest
from unittest.mock import patch
from src.general_example import GeneralExample

def test_flatten_dictionary():
    # Define test cases
    test_cases = [
        ({'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}, [0, 1, 2, 3, 10, 22, 42, 55]),
        ({'a': [1, 2], 'b': [3, 4]}, [1, 2, 3, 4]),
        ({'a': [3]}, [3]),
        ({}, [])
    ]

    for content, expected in test_cases:
        result = GeneralExample.flatten_dictionary(content)
        assert result == expected

@patch.object(GeneralExample, 'load_employee_rec_from_database', return_value=['emp001', 'Sam', '100000'])
def test_fetch_emp_details(mock_load_employee_rec_from_database):
    # Create an instance of GeneralExample
    instance = GeneralExample()

    # Call the method to be tested
    result = instance.fetch_emp_details()

    # Define the expected result
    expected = {
        'empId': 'emp001',
        'empName': 'Sam',
        'empSalary': '100000'
    }

    # Assert that the result matches the expected result
    assert result == expected

    # Assert that load_employee_rec_from_database was called exactly once
    mock_load_employee_rec_from_database.assert_called_once()
