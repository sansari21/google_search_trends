import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# Initialize pytrends and define the keyword list
trends = TrendReq(hl='en-US', tz=360)
kw_list = ["Cloud Computing"]

# Build payload for the last 12 months
trends.build_payload(kw_list, cat=0, timeframe='today 12-m')

# Get interest over time and display top 10 peak interest periods
interest_over_time = trends.interest_over_time()
top_interest = interest_over_time.sort_values(by="Cloud Computing", ascending=False).head(10)
print("Interest Over Time (Top 10):\n", top_interest)

# Get interest by region and display top 10 regions
interest_by_region = trends.interest_by_region()
top_regions = interest_by_region.sort_values(by="Cloud Computing", ascending=False).head(10)
print("Interest by Region (Top 10):\n", top_regions)

# Plot the top regions with the highest interest in Cloud Computing
top_regions.reset_index().plot(x='geoName', y='Cloud Computing', figsize=(10, 5), kind="bar")
plt.title("Top Regions by Interest in Cloud Computing")
plt.style.use('fivethirtyeight')
plt.show()

# Get top charts for a specific year
top_charts = trends.top_charts(2020, hl='en-US', tz=300, geo='GLOBAL')
print("Top Charts for 2020:\n", top_charts.head(10))

# Build payload to get related queries
trends.build_payload(kw_list=['Cloud Computing'])

# Try to fetch related queries with error handling
try:
    related_queries = trends.related_queries()
    if related_queries and 'Cloud Computing' in related_queries:
        print("Related Queries:\n", related_queries['Cloud Computing'])
    else:
        print("No related queries found for 'Cloud Computing'.")
except IndexError:
    print("Error retrieving related queries. No data available for 'Cloud Computing'.")

# Get suggestions for the keyword
suggestions = trends.suggestions(keyword='Cloud Computing')
suggestions_df = pd.DataFrame(suggestions).drop(columns='mid')
print("Suggestions:\n", suggestions_df)
