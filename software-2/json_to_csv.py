import sys
import json

def convert_json_file_to_csv_string(json_file):
    json_dict = open_json_file(json_file)
    csv_str = generate_csv_from_json(json_dict)
    return csv_str


def open_json_file(json_file):
    try:
        return read_json_dict_from_json_file(json_file)
    except Exception as e:
        print_error_and_exit(e)


def read_json_dict_from_json_file(json_file):
    with open(json_file, "r") as f:
        json_dict = json.load(f)
    return json_dict


def print_error_and_exit(e):
    print("Error:", e)
    sys.exit()


def generate_csv_from_json(json_dict):
    csv_str = ('ITEM_NUMBER, DEFINE, REPAIR, PREVENT\n')
    for (i, item) in enumerate(json_dict):
        csv_str += '%d, "%s", "%s", "%s"\n' % (i+1, item['DEFINE'], item['REPAIR'], item['PREVENT'])
    return csv_str


def main():
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: python3 %s json_file" % sys.argv[0])
        sys.exit()
    else:
        json_file = sys.argv[1]

    csv_str = convert_json_file_to_csv_string(json_file)
    print(csv_str)


if __name__ == "__main__":
    main()
