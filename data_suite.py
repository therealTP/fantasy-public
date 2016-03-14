from datetime import datetime, timedelta, date
import pytz

def addProjectionDictForSource(source, template, projection_dict):
    """
    projection_dict: final after all entries added
    Includes timestamp data and count
    """

    # get current time in pst
    now = datetime.now(
          pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S')

    # add info for source to
    template[source]["scrape_timestamp_pst"] = now
    template[source]["record_count"] = len(projection_dict)
    template[source]["projections"] = projection_dict


def getCurrentDate():
    """
    For final json
    YYYY-MM-DD format
    """
    # current date in pst
    current_date = datetime.now(
                   pytz.timezone('US/Pacific')).strftime('%Y-%m-%d')

    return current_date


def getYesterdayDate():
    """
    For actual NBA stats scraper
    YYYY-MM-DD format
    """
    # yesterday in pst
    yest = (datetime.now(pytz.timezone('US/Pacific')) -
            timedelta(days=1)).strftime('%Y-%m-%d')

    return yest


def getAllGameDates():
    """
    Gets all dates from beginning of season
    Returns array of dates
    """
    start = date(2015, 11, 2)
    end = date(2015, 11, 11)

    delta = timedelta(days=1)

    date_array = []

    while start <= end:
        date_array.append(start.strftime("%Y-%m-%d"))
        start += delta

    return date_array
