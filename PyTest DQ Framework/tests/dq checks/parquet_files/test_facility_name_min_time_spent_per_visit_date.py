import pytest


@pytest.fixture(scope='module')
def source_data(db_connection):

    query = """
        SELECT
            facility_name,
            visit_date,
            min_time_spent
        FROM core_data.facility_name_min_time_spent_per_visit_date
    """

    return db_connection.get_data_sql(query)


@pytest.fixture(scope='module')
def target_data(parquet_reader):

    target_path = '/parquet_data/facility_name_min_time_spent_per_visit_date'

    return parquet_reader.process(
        target_path,
        include_subfolders=True
    )


@pytest.mark.parquet_data
@pytest.mark.smoke
def test_dataset_not_empty(target_data, data_quality_library):

    data_quality_library.check_dataset_is_not_empty(
        target_data
    )


@pytest.mark.parquet_data
def test_count(source_data, target_data, data_quality_library):

    data_quality_library.check_count(
        source_data,
        target_data
    )


@pytest.mark.parquet_data
def test_duplicates(target_data, data_quality_library):

    data_quality_library.check_duplicates(
        target_data
    )


@pytest.mark.parquet_data
def test_not_null(target_data, data_quality_library):

    data_quality_library.check_not_null_values(
        target_data,
        [
            'facility_name',
            'visit_date',
            'min_time_spent'
        ]
    )


@pytest.mark.parquet_data
def test_completeness(source_data, target_data, data_quality_library):

    data_quality_library.check_data_completeness(
        source_data,
        target_data
    )
