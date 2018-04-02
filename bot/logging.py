import os
from twitterbot import timetool


def log(message, logfile_name):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path += "\\logs"
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = timetool.get_date_and_time()
        f.write( t + " " + message + "\n\n")
