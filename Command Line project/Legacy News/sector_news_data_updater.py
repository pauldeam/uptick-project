#updates sector_news_data sheet
#GENERAL IMPORTS #
import time
import datetime as dt

import pandas as pd
import numpy as np
import datetime as dt
from copy import copy
#import news module
import yahoo as news
import google_sheets_api as sheet


def update_sector_news_data():
    newsArticles = news.get_industry_news("AAPL")
    print(len(newsArticles))
    
    for i in range(len(newsArticles)):
        time.sleep(0.21)
        print("adding row sector_news_data...")
        try:
            sheet.sector_news_data.append_row([str(dt.datetime.now()), str(dt.datetime.now().time()), str(dt.datetime.now().date()), newsArticles[i]['title'], newsArticles[i]['summary'],newsArticles[i]['content'], newsArticles[i]['link']])
        except:
            print("error adding row")

