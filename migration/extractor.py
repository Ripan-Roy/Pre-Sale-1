import pandas as pd
class CSVColumnFinder:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.dataframe = None
        self.dataframe = pd.read_csv(self.file_path)
    def get_columns(self) -> list:
        if self.dataframe is None:
            raise ValueError(
                "CSV file not loaded. Call load_csv() before getting columns.")
        return self.dataframe.columns.tolist()

# Usage example:
# finder = CSVColumnFinder("your_file.csv")
# finder.load_csv()
# columns = finder.get_columns()
# print(columns)
