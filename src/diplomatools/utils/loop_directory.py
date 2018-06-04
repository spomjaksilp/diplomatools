import os
import logging
logging.basicConfig(level=logging.INFO)


def do_nothing(x):
    return x


def loop_directory(dir, filetype=None, callback=do_nothing):
    for file in os.listdir(dir):
        if filetype is None or file.endswith(filetype):
            logging.info(file)
            file_path = os.path.join(dir, file)
            yield callback(file_path)
