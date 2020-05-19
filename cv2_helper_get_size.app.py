# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sys

def on_init():
    return True


def on_valid():
    return True


def on_run(image: np.ndarray):
    #sys.stdout.write(f"[findMaxLocRect] array : {array}")
    #sys.stdout.write(f"[findMaxLocRect] template : {template}")
    #sys.stdout.flush()

    assert len(image.shape) == 3
    assert image.shape[0] >= 1
    assert image.shape[1] >= 1
    assert image.shape[2] >= 1

    h, w = image.shape[:2]

    return {
        'w': np.array(w, np.int32),
        'h': np.array(h, np.int32),
        'wh': np.array([w, h], np.int32)
        }


def on_destroy():
    return True


if __name__ == '__main__':
    pass
