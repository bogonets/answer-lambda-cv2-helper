# -*- coding: utf-8 -*-

import numpy as np


def on_run(roi):
    if roi.size < 4:
        raise ValueError("roi length should be greater than 4.")

    x_list = roi[::, 0::2]
    y_list = roi[::, 1::2]

    return {"result": np.array([np.min(x_list), np.min(y_list), np.max(x_list), np.max(y_list)])}


if __name__ == '__main__':
    pass
