import utilities
from utilities import *


# Grab all WSB posts
def get_wsb_posts(posts_scraped, subreddit):
    df = []
    for post in utilities.reddit.subreddit(subreddit).hot(limit=posts_scraped):
        content = {
            "title": post.title,
            "text": post.selftext
        }
        df.append(content)
    df = pd.DataFrame(df)

    return df


def scrape_hot_posts(posts_scraped, subreddit):
    df = get_wsb_posts(posts_scraped, subreddit)
    [word_df, ticker_df] = analyze_word_frequency(df)
    list_tickers(ticker_df, word_df, posts_scraped)


