#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Option import Option
from MainLoop import MainLoop
from Color import Color

if __name__ == '__main__':
    print(Color.pink + "    ____        ________          ____            __                            " + Color.red + " _____ ____ \n" +
          Color.pink + "   / __ )__  __/ __/ __/__  _____/ __ \___  _____/ /__________  __  _____  _____" + Color.red + "/ ___// __ \\\n" +
          Color.pink + "  / __  / / / / /_/ /_/ _ \/ ___/ / / / _ \/ ___/ __/ ___/ __ \/ / / / _ \/ ___/" + Color.red + " __ \/ /_/ /\n" +
          Color.pink + " / /_/ / /_/ / __/ __/  __/ /  / /_/ /  __(__  ) /_/ /  / /_/ / /_/ /  __/ /  " + Color.red + "/ /_/ /\__, / \n" +
          Color.pink + "/_____/\__,_/_/ /_/  \___/_/  /_____/\___/____/\__/_/   \____/\__, /\___/_/   " + Color.red + "\____//____/  \n" +
          Color.pink + "                                                             /____/                         \n" + Color.reset)

    option = Option
    mainloop = MainLoop(option)
