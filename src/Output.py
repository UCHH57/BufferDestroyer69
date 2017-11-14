#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Output:
    prompt = "=>"

    def __init__(self):
        return

    def load_prompt(self):
        print(self.prompt, end='', flush=True)

    def write_message(self, msg):
        print(msg)

    def write_error_message(self, msg):
        print(msg)

