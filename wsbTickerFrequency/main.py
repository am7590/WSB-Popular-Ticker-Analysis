# Data Source 1:  ftp.nasdaqtrader.com/SymbolDirectory
# Data Source 2:  ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt
# Data Source 3:  ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt

import csv
import pandas as pd
import praw
import re
from datetime import datetime

# Step 1: Print a list of tickers
# Save tickers and company names ['ticker', 'name']
ticker_list = []
with open('tickers.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         ticker_list.append(row[0].split(","))

#for obj in ticker_list:
    # print(obj[0])  # Print ticker name
    # print(obj[1])  # Print company name
    # print(obj[0] + ": " + obj[1])  # Print company + ticker name

# Step 2: Create frequency list of tickers
# Read data from reddit API
reddit = praw.Reddit(
  client_id = "qBibtPUZ69Gi1IUUGhQ87w",
  client_secret = "8mzMqF5BRRa1kEWR9FqpJzhN1-WvBA",
  user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
)


# Grab hot or new posts based on user input
settings_input = input("Commands:\nView hot posts: h\nView new posts: n\nReset output.txt: r\n\n")

if settings_input == "r":
    file = open('output.txt', 'w')
    file.truncate(0)
    print("Reset successful. Enter a new command:")
    settings_input = input("View hot posts: h\nView new posts: n\n\n")

WSB_POSTS_SCRAPED = int(input("How many posts should be scraped? (100 is the default): "))
WSB_NEW_OR_HOT = ""

# Grab all hot WSB posts
df = []
if settings_input == "h":
    WSB_NEW_OR_HOT = "hottest"
    for post in reddit.subreddit('wallstreetbets').hot(limit=WSB_POSTS_SCRAPED):
        content = {
            "title": post.title,
            "text": post.selftext
        }
        df.append(content)
if settings_input == "n":
    WSB_NEW_OR_HOT = "newest"
    for post in reddit.subreddit('wallstreetbets').new(limit=WSB_POSTS_SCRAPED):
        content = {
            "title": post.title,
            "text": post.selftext
        }
        df.append(content)
df = pd.DataFrame(df)


# Analyze word frequency
# (from https://medium.com/@tom.santinelli/scraping-reddits-wall-street-bets-for-popular-stock-tickers-38ed5202affc)
regex = re.compile('[^a-zA-Z ]')
word_dict = {}
for (index, row) in df.iterrows():
    # titles
    title = row['title']
    title = regex.sub('', title)
    title_words = title.split(' ')
    # content
    content = row['text']
    content = regex.sub('', content)
    content_words = content.split(' ')
    # combine
    words = title_words + content_words
    for x in words:
        if x in ['A', 'B', 'GO', 'ARE', 'ON']:
            pass

        elif x in word_dict:
            word_dict[x] += 1
        else:
            word_dict[x] = 1
word_df = pd.DataFrame.from_dict(list(word_dict.items())).rename(columns={0: "Term", 1: "Frequency"})
ticker_df = pd.DataFrame(ticker_list).rename(columns={0: "Term", 1: "Name"})


# Step 3: Print data to output.txt with timestamp

# List of tickers (sorted by frequency)
stonks_df = pd.merge(ticker_df["Term"], word_df, on="Term")
final_df = stonks_df.sort_values(by=['Frequency'], ascending=False)
new_line = final_df.to_string(index=False)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

with open("output.txt", "a") as a_file:
  a_file.write(f"WSB Ticker Frequency of Top {WSB_POSTS_SCRAPED} {WSB_NEW_OR_HOT} posts: {current_time}\n")
  a_file.write(new_line)
  a_file.write("\n\n")