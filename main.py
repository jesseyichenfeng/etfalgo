import json
import pandas as pd
import pandas_ta as ta
import os
from experiment.function import pull_data

start_date = "2013-01-01"

if __name__ == "__main__":

    tiingo_token = os.getenv("TIINGO")
    data = pull_data(ticker="UPRO", start_date=start_date)
    benchmark_data = pull_data(ticker="VOO", start_date=start_date)