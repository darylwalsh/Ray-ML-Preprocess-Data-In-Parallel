# preprocess-data-in-parallel-with-ray-lp-author
Repository for liveProject: Preprocess Data in Parallel with Ray

#News dataset
found in the /news folder, includes a set of news which you can use to run your scraper,
the usage of live websites for scraping is not advisable, as the huge amount of HTTP calls
made at the same time by yoru script and from multiple students might cause issues to a live platform.
You will need, also, to think about how to be less invasive as possible while you do your exercise, but for now
you can practice using these news, which have been already scraped for you, and you can re-scrape doing the following actions:

* Navigate to the news folder in your machine
* type:
``` python -m http.server 8000```

Depending on how you installed python in your system you might have to substitute *python* with *python3* but
make sure you have a version of python >= than 3.6
