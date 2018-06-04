import numpy as np
import logging
logging.basicConfig(level=logging.INFO)


def parse_anritsu(file_path, skip_top, skip_bottom):
    """
    parse Anritsu .spa file to numpy array
    :param file_path: path to spa file
    :param skip_top: number of lines to skip at the top of the file
    :param skip_bottom: number of lines to skip at the bottom of the file
    :return:
    """
    with open(file_path) as fp:
        amp = []
        freq = []
        loc = 0
        for line in fp:
            loc += 1
            if loc <= skip_top or loc > skip_bottom:
                continue

            # line format
            # P_48=-59.292000 , 109.759455 MHz
            y, x = line.split("=")[1][:-5].split(",")
            logging.debug("{}\t{}".format(y, x))

            amp.append(float(y))
            freq.append(float(x))

        return np.array([freq, amp])
