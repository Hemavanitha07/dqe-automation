from pathlib import Path
import pandas as pd


class ParquetReader:

    def process(self, target_path, include_subfolders=True):

        path = Path(target_path)

        parquet_files = (
            path.rglob("*.parquet")
            if include_subfolders
            else path.glob("*.parquet")
        )

        dataframes = [pd.read_parquet(file) for file in parquet_files]

        if not dataframes:
            return pd.DataFrame()

        return pd.concat(dataframes, ignore_index=True)
