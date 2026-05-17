import pytest

from src.connectors.file_system.parquet_reader import ParquetReader
from src.connectors.postgres.postgres_connector import (
    PostgresConnectorContextManager
)
from src.data_quality.data_quality_validation_library import (
    DataQualityLibrary
)


def pytest_addoption(parser):

    parser.addoption("--db_host", action="store", default="localhost")
    parser.addoption("--db_port", action="store", default="5432")
    parser.addoption("--db_name", action="store", default="mydatabase")
    parser.addoption("--db_user", action="store")
    parser.addoption("--db_password", action="store")


@pytest.fixture(scope='session')
def db_connection(request):

    db_host = request.config.getoption("--db_host")
    db_port = request.config.getoption("--db_port")
    db_name = request.config.getoption("--db_name")
    db_user = request.config.getoption("--db_user")
    db_password = request.config.getoption("--db_password")

    with PostgresConnectorContextManager(
        db_user=db_user,
        db_password=db_password,
        db_host=db_host,
        db_name=db_name,
        db_port=db_port
    ) as db_connector:

        yield db_connector


@pytest.fixture(scope='session')
def parquet_reader():
    yield ParquetReader()


@pytest.fixture(scope='session')
def data_quality_library():
    yield DataQualityLibrary()
