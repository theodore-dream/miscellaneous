#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-2022 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Simple println capabilities.
"""

import time
from pathlib import Path
from demo_opts import get_device
from luma.core.virtual import terminal
from PIL import ImageFont

#requirements for openai API
import os
import openai

## adding logging
import requests
import logging
import datetime

## logging config
logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG,
    filename="file.log",
    filemode='w',
    force=True
    )
## this somehow helps ensure logging actually works
logger = logging.getLogger(__name__)

## openai setup
#openai.api_key = "DELETED"

## forming the openai api call with davinci model
def api_call():
    logger.debug("This is a debug log")
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="make a tiny poem.",
      temperature=1.0,
      max_tokens=400,
      # top_p=1,
      # frequency_penalty=0.0,
      # presence_penalty=0.0,
      # stop=["\n"]
    )

    #print("printed the response above, below is the completion")
    #print(response.choices[0].text)
    return (response.choices[0].text)


def make_font(name, size):
    font_path = str(Path(__file__).resolve().parent.joinpath('fonts', name))
    return ImageFont.truetype(font_path, size)

def boot():
            font = make_font("ProggyTiny.ttf", 16)
            term = terminal(device, font)
            term.println("Progress bar")
            term.println("------------")
            for mill in range(0, 10001, 25):
                term.puts("\rPercent: {0:0.1f} %".format(mill / 100.0))
                term.flush()

            time.sleep(2)
            term.clear()

# def poem()


def printtext():
#         for fontname, size in [(None, None), ("tiny.ttf", 6), ("ProggyTiny.ttf", 16), ("creep.bdf", 16), ("miscfs_.ttf", 12), ("FreePixel.ttf", 12), ('ChiKareGo.ttf', 16)]:
            font = make_font("ProggyTiny.ttf", 16)
            term = terminal(device, font)

            logging.info("python script started")
            poem = api_call()
            logging.info(f'Successfully output the poem to the terminal at {datetime.datetime.now()}')
            logger.debug("API call successful. Now printing.")
            term.println(poem)
            term.println("------------------")
            time.sleep(2)
            term.clear()

if __name__ == "__main__":
    try:
        device = get_device()
        # boot()
        printtext()
    except KeyboardInterrupt:
        logging.error(f'Interrupted with keyboard interrupt at {datetime.datetime.now()}')
        pass
