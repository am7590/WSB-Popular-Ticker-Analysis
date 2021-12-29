# Data Source 1:  ftp.nasdaqtrader.com/SymbolDirectory
# Data Source 2:  ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt
# Data Source 3:  ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt

from scrape_hot_posts import *
from scrape_24h_posts import *


def run_all_commands():
    scrape_hot_posts(100, 'wallstreetbets')
    scrape_hot_posts(50, 'wallstreetbets')
    scrape_24h_posts('wallstreetbets')


if __name__ == "__main__":
    run_all_commands()
