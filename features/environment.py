import time

import sys
from os.path import abspath
sys.path.append(abspath('../'))

from config_reader import ConfigReader
from browser2 import Browser
from header import Header



def before_feature(context, feature):
    print("-Before feature function call-")
    configs = ConfigReader("config.ini")
    context.configs = configs


def before_scenario(context, scenario):
    print("-Before scenario function call-")
    section = 'environment'
    configs = context.configs
    browser = Browser(configs.get_url(section), configs.get_browser(section), configs.get_wait_time(section))
    context.browser = browser
    header = Header(context.browser)
    context.header = header


def after_scenario(context, scenario):
    print("-After scenario function call-")
    browser = context.browser
    time.sleep(2)
    browser.shutdown()


def after_feature(context, feature):
    print("-After feature function call-")
