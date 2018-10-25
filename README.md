# QuotesBot
This is a Scrapy project to scrape review data hotel from http://www.tripadvisor.com.



## Extracted data

This project extracts quotes, combined with the respective author names and tags.
The extracted data looks like this sample:

    {
        'noQuotes': 'Paradisus La Perla very good but with Melia quirks',
        'partial_entry': '“The hotel is finnished (just) but there is a lot of snagging going on although ...”',
    }


## Spiders

This project contains one spiders and you can list them using the `list`
command:

    $ scrapy list
    quote

You can learn more about the spiders by going through the
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).


## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl quote

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl quote -o quote.json
