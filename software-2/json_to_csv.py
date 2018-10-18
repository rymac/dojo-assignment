import sys
import json

class FearConverter:
    def __init__(self):
        self.HEADER_CSV = 'ITEM_NUMBER, DEFINE, PREVENT, REPAIR\n'
        self.result_csv = ""
        self.fears_json = {}


    def convert_json_file_to_csv_string(self, json_file):
        self._open_json_file(json_file)
        self._generate_csv_from_json()
        return self.result_csv


    def _open_json_file(self, json_file):
        try:
            return self._read_fears_from_json_file(json_file)
        except Exception as e:
            self._print_error_and_exit(e)


    def _read_fears_from_json_file(self, json_file):
        with open(json_file, "r") as f:
            self.fears_json = json.load(f)


    def _print_error_and_exit(self, e):
        print("Error:", e)
        sys.exit()


    def _generate_csv_from_json(self):
        self._add_csv_header()
        self._add_csv_body()


    def _add_csv_header(self):
        self.result_csv += self.HEADER_CSV


    def _add_csv_body(self):
        for (i, fear) in enumerate(self.fears_json):
            fear_csv = '%d, "%s", "%s", "%s"\n' \
                       % (i+1, fear['DEFINE'], fear['PREVENT'], fear['REPAIR'])
            self.result_csv += fear_csv


def main():
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: python3 %s json_file" % sys.argv[0])
        sys.exit()
    else:
        json_file = sys.argv[1]

    fear_converter = FearConverter()
    csv_str = fear_converter.convert_json_file_to_csv_string(json_file)
    print(csv_str)


if __name__ == "__main__":
    main()
