import pandas as pd


class DataQualityLibrary:

    @staticmethod
    def check_dataset_is_not_empty(dataset):
        assert not dataset.empty, "Dataset is empty"

    @staticmethod
    def check_count(source_data, target_data):

        assert len(source_data) == len(target_data), (
            f"Count mismatch. "
            f"Source={len(source_data)}, "
            f"Target={len(target_data)}"
        )

    @staticmethod
    def check_duplicates(dataset):

        duplicates = dataset[dataset.duplicated()]

        assert duplicates.empty, (
            f"Duplicate rows found:\n{duplicates.head()}"
        )

    @staticmethod
    def check_not_null_values(dataset, columns):

        null_rows = dataset[
            dataset[columns].isnull().any(axis=1)
        ]

        assert null_rows.empty, (
            f"Null values found:\n{null_rows.head()}"
        )

    @staticmethod
    def check_data_completeness(source_data, target_data):

        missing_rows = pd.concat(
            [source_data, target_data]
        ).drop_duplicates(keep=False)

        assert missing_rows.empty, (
            f"Missing rows detected:\n{missing_rows.head()}"
        )
