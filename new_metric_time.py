import time
import os

HOUR_DAY_CONV = 24
MIN_HOUR_CONV = 60
METRIC_SEC_CONV = 0.864
METRIC_TIME_DIS_CONS = 10000



def get_metric_time():
    hours = (((time.localtime().tm_hour*MIN_HOUR_CONV*MIN_HOUR_CONV)/METRIC_SEC_CONV)/METRIC_TIME_DIS_CONS)
    mins = (((time.localtime().tm_min*MIN_HOUR_CONV)/METRIC_SEC_CONV)/METRIC_TIME_DIS_CONS)
    secs = (time.localtime().tm_sec/METRIC_SEC_CONV/METRIC_TIME_DIS_CONS)
    metric_time = "{:.4f}".format(hours+mins+secs)
    return metric_time

def get_metric_date():
    year  = (time.localtime().tm_year)

def main():
    while True:
        metric_time = get_metric_time()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(str(metric_time))

main()