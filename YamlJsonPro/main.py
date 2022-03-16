import sys
import modellogger
import yaml
from yaml.loader import SafeLoader
import json


def read_yam_file(filepath):
    modellogger.log_info("Reading Yaml File")
    with open(filepath) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data


def main():
    try:
        modellogger.init_logger()
        modellogger.log_info("Hello World!")

        modellogger.log_info("Name of Python script:" + sys.argv[0])
        modellogger.log_info("Name of Yaml File tO Read:" + sys.argv[1])
        modellogger.log_info("Name of Json File to Write:" + sys.argv[2])

        data = read_yam_file(sys.argv[1])
        write_json_file(data, sys.argv[2])
    except:
        modellogger.log_exception("Exception in main")


def write_json_file(data, filepath):

    modellogger.log_info("write_json_file")

    try:
        with open(filepath, "w") as outfile:
            json.dump(data, outfile)
    except:
        modellogger.log_exception("Exception in write_json_file")


if __name__ == "__main__":
    # Arguments passed

    main()
