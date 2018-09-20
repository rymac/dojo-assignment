import sys
import os
import json

def json_file_to_csv_string(json_file):
    with open(json_file, "r") as f:
        json_dict = json.load(f)

    csv_str = ('ITEM_NUMBER, DEFINE, REPAIR, PREVENT\n')
    for (i, item) in enumerate(json_dict):
        csv_str += '%d, "%s", "%s", "%s"\n' % (i+1, item['DEFINE'], item['REPAIR'], item['PREVENT'])

    return csv_str


def main():
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: python3 %s json_file" % sys.argv[0])
        sys.exit()

    csv_str = json_file_to_csv_string(sys.argv[1])
    print(csv_str)


if __name__ == "__main__":
    main()

