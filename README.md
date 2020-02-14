# News Aggregator

### Description

For this assignment you have to implement an application that aggregates news from two different APIs. The APIs you’ll be using are Reddit and [News API](https://newsapi.org/). This application should be running on your localhost and serve the result in JSON format from an endpoint whenever it gets a request. You are allowed to use 3rd party wrappers of these APIs.

### Part I

The two functionalities that need to be implemented are “list” and “search”.

This is an example request for a generic GET request.

    > Request
    GET /news   HTTP/1.1
    Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ
    Accept: application/json
    
    > Response
    [
      {
        "headline": "Human organs can be stored for three times as long in major breakthrough for transplants",  // Headline of the article
        "link": "https://www.telegraph.co.uk/science/2019/09/09/human-organs-can-stored-three-times-long-major-breakthrough/",  // Link of the article
        "source": "reddit" // Source that you retrieved this news from
      },
      {
        "headline": "Depth of Field: The Shared Memory of One World Trade Center",
        "link": "https://www.wired.com/story/one-world-trade-center-history-future/",
        "source": "newsapi"
      },
    ]

You should also implement a feature that allows someone to search.

    > Request
    GET /news?query=bitcoin   HTTP/1.1
    Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ
    Accept: application/json
    
    > Response
    [
      {
        "headline": "IRS goes after cryptocurrency owners for unpaid taxes",
        "link": "https://www.cbsnews.com/news/own-bitcoin-irs-pursues-cryptocurrency-owners-for-unpaid-taxes/",
        "source": "reddit"
      },
      {
        "headline": "Skirting US sanctions, Cubans flock to cryptocurrency to shop online, send funds",
        "link": "https://www.channelnewsasia.com/news/business/skirting-us-sanctions--cubans-flock-to-cryptocurrency-to-shop-online--send-funds-11901148",
        "source": "newsapi"
      },
    ]

*Suggestion:* Try to use /r/news for Reddit and the general category for News API (you don’t have to but it’s worth checking out).

You have to at least return the three fields that are in the sample requests above. You can add more fields if you’d like.

### Part II

Store the data from the API into a database such that, if a request is repeated, the response is returned from the database and does not need a new API call.

Again, you must store at least the three fields from Part I and any other fields you decide to store.

You should also set an expiry on this data. If a user makes a request that you have seen in the past, but it is past the expiry limit, you should make a fresh call to the API

Note that you should not store this data in the cache, but rather in the database.

### How to Run

Clone this repository.
  ```
$ cd django-news-aggregator
```
Make sure you have Python > 3.6 installed

Create a virtual environment. Take a look at virtualenv, python3-venv
  ```
$ pip install django
```
  ```
$ pip install djangorestframework
```
  ```
$ pip install requests
```
 ```
python manage.py runserver
```

You can access the application by opening the link at which project is running (displayed in terminal).
