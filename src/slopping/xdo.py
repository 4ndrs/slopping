# Copyright (c) 2022 4ndrs <andres.degozaru@gmail.com>
# SPDX-License-Identifier: MIT
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
"""Use libxdo library with ctypes to get the window id"""

import ctypes
import os


class xdo_t(ctypes.Structure):
    """xdo_t struct type"""

    _fields_ = []


def get_window_id():
    """Returns the id of the Window under the mouse"""
    libxdo = ctypes.CDLL("libxdo.so")
    libxdo.xdo_new.argtypes = [ctypes.c_char_p]
    libxdo.xdo_new.restype = ctypes.POINTER(xdo_t)
    libxdo.xdo_get_window_at_mouse.argtypes = (
        ctypes.POINTER(xdo_t),
        ctypes.c_void_p,
    )

    xdo = libxdo.xdo_new(os.environ.get("DISPLAY").encode())
    window_id = ctypes.c_ulong()

    libxdo.xdo_get_window_at_mouse(xdo, ctypes.byref(window_id))

    return window_id.value
