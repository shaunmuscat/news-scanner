from pathlib import Path


def get_test_data_file_contents(filename):
    file = Path(__file__).parent / 'test_data' / filename
    with open(file, encoding='UTF-8') as reader:
        contents = reader.read()
    return contents
