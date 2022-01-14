# Data Source 1:  ftp.nasdaqtrader.com/SymbolDirectory
# Data Source 2:  ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt
# Data Source 3:  ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt

from scrape_hot_posts import *
from scrape_new_posts import *
from scrape_any_hour_posts import *


def run_all_commands(subreddit):
    scrape_hot_posts(50, subreddit)
    scrape_new_posts(50, subreddit)
    scrape_any_hour_posts(24, subreddit)


if __name__ == "__main__":
    run_all_commands('wallstreetbets')
