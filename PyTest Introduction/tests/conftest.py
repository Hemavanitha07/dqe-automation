import pytest
import pandas as pd

@pytest.fixture(scope="session")
def csv_data():
   path = "../src/data/data.csv"
   print("Current Working Directory:",os.getcwd())
   print("Resolved Path:",os.path.abspath(path))
   return pd.read_csv(path)

@pytest.fixture(scope="session")
def validate_schema():
   def _validate(actual_schema, expected_schema):
       return actual_schema == expected_schema
   return _validate

def pytest_collection_modifyitems(items):
   for item in items:
       if not item.own_markers:
           item.add_marker(pytest.mark.unmarked)
