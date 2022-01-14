# WSB-Popular-Ticker-Analysis
- Run main.py to create frequency tables from the stock tickers mentioned in any subreddit.
- It can make frequency tables for as many new or hots posts as you want
- It can make frequency tables for posts from the last X hours 
- If you search more than a few thousand posts, it will take a while to run

### Example output.txt
```
Ticker Frequency from the hottest 50 posts in r/wallstreetbets at 17:26:10:
Term  Frequency
 GME          3
 AMC          1
  BE          1
  DD          1
   F          1
HOOD          1
WISH          1 
```

```
Ticker Frequency from the newest 50 posts in r/wallstreetbets at 17:26:11:
Term  Frequency
 GME          9
 IHS          5
PTON          5
BYND          4
  SP          4
 ALL          3
 CCO          3
 AMC          2
 ATH          2
WISH          2
AAPL          1
...           ...
```

```
Ticker Frequency from posts made in the last 24 hours from r/wallstreetbets at 17:26:24:
 Term  Frequency
  GME         63
 WISH         40
 TSLA         37
   SP         35
   DD         32
    M         32
   ET         28
  VIR         20
  TSM         19
 LCID         19
    K         18
  AMC         13
  LNG         13
   MA         13
   CP         12
  AMD         11
  GDP         10
 BYND         10
   GM         10
  ...         ...
```


### TODO
- [x] Successfully deploy [as an API](https://www.github.com/am7590/WSB-Ticker-API)
- [ ] Parse tickers with a $ in front of them
- [ ] Parse company names and count them as ticker frequency values
- [ ] Parse "call" and "put" from posts with tickers in them
- [ ] Read sentiment from all posts analyzed 
- [ ] Update ticker csv and add indexes/etf's
