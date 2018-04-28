#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Color import Color

class Output:
    prompt = Color.green + "=> " + Color.reset

    def __init__(self):
        return

    def load_prompt(self):
        print(self.prompt, end='', flush=True)

    def write_message(self, msg, end='\n'):
        print(msg, end=end)

    def write_error_message(self, msg):
        print(Color.yellow + msg + Color.reset)

