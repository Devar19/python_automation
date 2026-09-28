import csv
from pathlib import Path


class CSVReader:

    @staticmethod
    def read_test_data(filename):

        project_root = Path(__file__).resolve().parent.parent

        file_path = (
            project_root
            / "data"
            / filename
        )

        with open(
            file_path,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            return list(reader)