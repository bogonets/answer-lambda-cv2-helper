# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sys

def on_init():
    return True


def on_valid():
    return True


def on_run(xy: np.ndarray, wh: np.ndarray):

    assert len(xy) == 2
    assert len(wh) == 2

    #sys.stdout.write(f"[cvt to rect] xy {xy}\n")
    #sys.stdout.write(f"[cvt to rect] wh {wh}\n")
    #sys.stdout.flush()

    x1 = xy[0]
    y1 = xy[1]
    x2 = xy[0] + wh[0]
    y2 = xy[1] + wh[1]


    return {'rectangle': np.array([[x1, y1, x2, y2]], np.int32)}


def on_destroy():
    return True


if __name__ == '__main__':
    pass
