import pytest
import pandas as pd
import re

FILE_PATH = "..\src/data/data.csv"

# Read CSV
@pytest.fixture(scope="module")
def csv_data():
   return pd.read_csv(FILE_PATH)

# Validate file is not empty
def test_file_not_empty(csv_data):
   assert not csv_data.empty, \
       "CSV file is empty"

# Validate schema
@pytest.mark.validate_csv
def test_validate_schema(csv_data):
   expected_schema = [
       "id",
       "name",
       "age",
       "email",
       "is_active"
   ]
   actual_schema = list(csv_data.columns)
   assert actual_schema == expected_schema, \
       "Schema validation failed"

# Validate age column
@pytest.mark.validate_csv
@pytest.mark.skip(reason="Skipping age validation")
def test_age_column_valid(csv_data):
   assert csv_data["age"].between(0, 100).all(), \
       "Invalid age values found"

# Validate email format
@pytest.mark.validate_csv
def test_email_column_valid(csv_data):
   pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
   for email in csv_data["email"]:
       assert re.match(pattern, email), \
           f"Invalid email found: {email}"

# Validate duplicates
@pytest.mark.validate_csv
@pytest.mark.xfail(reason="Duplicate rows exist")
def test_duplicates(csv_data):
   assert not csv_data.duplicated().any(), \
       "Duplicate rows found"

# Parameterized test
@pytest.mark.parametrize(
   "player_id, expected_status",
   [
       (1, False),
       (2, False)
   ]
)
def test_active_players(
   csv_data,
   player_id,
   expected_status
):
   actual_status = csv_data.loc[
       csv_data["id"] == player_id,
       "is_active"
   ].values[0]
   assert actual_status == expected_status, \
       f"is_active mismatch for id {player_id}"

# Same test without parameterized mark
def test_active_player(csv_data):
   actual_status = csv_data.loc[
       csv_data["id"] == 2,
       "is_active"
   ].values[0]
   assert actual_status == False, \
       "Player with id 2 should be inactive"
