from typing import Dict
from foxcross.pandas_serving import DataFrameModelServing, run_pandas_serving
from foxcross.serving import ModelServing
import pandas


class InterpolateModel(DataFrameModelServing):
    test_data_path = "interpolate.json"

    def predict(self, data: pandas.DataFrame) -> pandas.DataFrame:
        return data.interpolate(limit_direction="both")


class AddOneModel(ModelServing):
    test_data_path = "add.json"

    def predict(self, data):
        return [x + 1 for x in data]


class InterpolateMultiDataFrameModel(DataFrameModelServing):
    test_data_path = "multi_interpolate.json"

    def predict(
        self, data: Dict[str, pandas.DataFrame]
    ) -> Dict[str, pandas.DataFrame]:
        return {
            key: value.interpolate(limit_direction="both")
            for key, value in data.items()
        }


if __name__ == "__main__":
    run_pandas_serving()
