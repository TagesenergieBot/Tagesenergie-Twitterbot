from bs4 import BeautifulSoup
import sys
import requests
import re
from bot import loggingservice, timetool


page_link = 'https://tagesenergie.org/energie-des-tages/tagesenergie-am-' + timetool.getf_date() + '/'

# fetch the content from url
try:
    page_response = requests.get(page_link, timeout=5)
except Exception as e:
    loggingservice.log(repr(e), "ConnectionErrors.log")
    sys.exit(1)

# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")


# extract values
def get_magicvalue():
    return re.sub(r'\D', '', page_content.find(id='mk-chart-9').text)


def get_energyimpulsvalue():
    return re.sub(r'\D', '', page_content.find(id='mk-chart-13').text)


def get_consiousvalue():
    return re.sub(r'\D', '', page_content.find(id='mk-chart-17').text)


def get_errortext():
    for x in page_content.find_all(class_='mk-single-content clearfix'):
        for y in page_content.find_all('h3'):
            if "Schwankungen" or "klare Feststellung" or "verhindern" or "Status" in y.text:
                return y.text