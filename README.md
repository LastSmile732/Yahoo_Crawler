# Yahoo_Crawler
A web crawler which gets hot products from Yahoo Taiwan Shop

Required module:
pandas
numpy
bs4

To excute the Python script:
1) simply get the yahoo_shop_crawler.py
2) type "python yahoo_shop_crawler.py" in the console command line.
3) the excution will take a few minutes since it waits 0.3 seconds before fetching data on the next page.
4) the result file "yahoo_shop_fig.csv" will appear in the same folder as this python script.

Please notice that the result does not guarantee to display the top selling products 
because there are no selling amount for them. There is a figure in sub-category pages display top selling products, such as:
https://tw.buy.yahoo.com/?catitemid=113971&sort=-sales&pg=1, 
but the format of sub-category pages is inconsistent, and finding all sub-category could be time consuming.
