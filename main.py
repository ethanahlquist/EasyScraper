#!/usr/bin/env python3

import re  # regular expressions
import csv
import sys

from driver import SeleniumDriver
from element import ScrapElement
from selenium.common.exceptions import *

# This is where most user-code goes:
from userCode import *

e = configDict['elements']


def openCSV(csvfile):
    writer = csv.DictWriter(csvfile, fieldnames=e.keys(), delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    return writer


def appendCSV(csvfile):
    writer = csv.DictWriter(csvfile, fieldnames=e.keys(), delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    return writer


def main(argv):

    URL = configDict['URL']
    driver = configDict['driver']
    csvfile = configDict['csv']

    # Open Url
    driver.get(URL)

    # 'a+' = append,
    # 'w+' = overwrite
    mode = 'w+'
    csvfile = open('data.csv', mode)

    if re.match(r'w.', mode):
        writer = openCSV(csvfile)
    elif re.match(r'a.', mode):
        writer = appendCSV(csvfile)

    try:
        dataLoop(e, writer)
    except (NoSuchWindowException, WebDriverException) as error:
        pass
    else:
        print(error)

    csvfile.close()  # Close opened file
    driver.quit()  # No longer need browser open

    afterScrap(csvfile)


if __name__ == "__main__":
    main(sys.argv[1:])
