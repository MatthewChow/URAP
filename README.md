URAP
====
LeaflyStrains folder contains all the files needed to scrape strain information from leafly.com.

All commands should be run inside of the first LeaflyStrains directory (the one containing scrapy.cfg)

To scrape strain information: scrapy crawl leafly
# This creates leafly_items.csv that has all of the strain information.

To update the list of strains that are being scraped, run the following 3 commands:
1) scrapy crawl strains -o hybrid_strains.json -t json -a category=hybrid
2) scrapy crawl strains -o indica_strains.json -t json -a category=indica
3) scrapy crawl strains -o sativa_strains.json -t json -a category=sativa
