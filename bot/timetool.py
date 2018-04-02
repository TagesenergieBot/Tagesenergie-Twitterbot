from datetime import datetime
from pytz import timezone


central_europe = timezone('Europe/Berlin')


def get_current_time():
    return datetime.now(central_europe)


def get_date_and_time():
    return get_current_time().strftime('%d.%m.%Y %H:%M:%S')


def get_time():
    return get_current_time().strftime('%H:%M:%S')


def get_date():
    return get_current_time().strftime('%d.%m.%Y')


def getf_date():
    return get_current_time().strftime('%d-%m-%Y')
