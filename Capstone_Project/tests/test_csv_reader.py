from utils.csv_reader import CSVReader

def test_csv_reader():

    data = CSVReader.read_test_data(
        "login_data.csv"
    )

    print("CSV data:", data)

    assert len(data) > 0
    assert "email" in data[0]
    assert "password_type" in data[0]
    assert "expected_result" in data[0]