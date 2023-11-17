from pytrends.request import TrendReq
import pandas as pd
import pycountry
from colors import GREEN, YELLOW, BLUE, ENDC


def get_volume(kw, locale):
    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = [kw]
    pytrends.build_payload(kw_list=keywords, timeframe='today 12-m', geo=locale)

    interest_over_time_df = pytrends.interest_over_time()
    # Resample the data to monthly frequency, calculating the mean for each month
    yearly_average = interest_over_time_df[kw].mean()
    monthly_interest = interest_over_time_df.resample('M').mean()
    country = pycountry.countries.get(alpha_2=locale.upper()).name
    yearly_total = interest_over_time_df[kw].sum()

    print(" ")
    print(f"{YELLOW}|> SEARCH VOLUME FOR {GREEN}'{kw.upper()}'{ENDC} for geolocalisation : {GREEN}'{country}'{ENDC}")
    print(" ")

    print(f"{BLUE}------------------------")
    print("  MONTHLY AVERAGES")
    print(f"------------------------{ENDC}")

    for date, row in monthly_interest.iterrows():
        month = date.strftime('%Y-%m')
        average_volume = row[kw] if not pd.isna(row[kw]) else 0
        print(f"{month} : {GREEN}{average_volume}{ENDC}")

    print(" ")
    print(f"{YELLOW}|> YEARLY AVERAGE : {GREEN}{yearly_average:.2f}{ENDC}")
    print(f"{YELLOW}|> YEARLY TOTAL : {GREEN}{yearly_total}{ENDC}")