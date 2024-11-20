import requests

# All component variables to create proper routing URL for news API call
API_KEY = "773a9dc7cd75450d8c850256149561a6"

base_url_everything = f"https://newsapi.org/v2/everything?q=Apple&from=2024-10-23&sortBy=popularity&apiKey={API_KEY}"
base_url_top = f"https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey={API_KEY}"

response = requests.get(base_url_everything)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Response Error {response.status_code}.")


def createURLEverything(q, searchIn, sources, domains, excludeDomains, fromDate, toDate, language, sortBy):
    """
    Constructs an API URL for the "everything" endpoint.

    Args:
        q (string): Keyword surrounded in quotes
        searchIn (string): Restrict article section to search in (title, description, content)
        sources (string): Specify news sources to take headlines from; comma seperated string of identifiers
        domains (string): Comma seperated string of domains to source from (eg: bbc.co.uk)
        excludeDomains (string): Comma seperated string of domains to avoid sourcing from 
        fromDate (string): Date and time for oldest article allowed (2024-11-20 or 2024-11-20T03:55:31)
        toDate (string): Date and time for newest artciles allowed
        language (string): 2 letter ISO code for language (fr, en, sp)
        sortBy (string): Order to sort articles by (relevency, popularity, publishedAt)

    Returns:
        string: API URL that can be used in a request.get() function call.
    """
    return -1

def createURLTop(country, category, sources, q):
    """
    Constructs an API URL for the "everything" endpoint.

    Args:
        country (string): 2 letter ISO code for country (us, ja, ch)
        category (string): Category to recieve headlines from (business, entertainment, general, health, science, sports, technology, etc)
        sources (string): Specify news sources to take headlines from; comma seperated string of identifiers
        q (string): Keyword surrounded in quotes

    Returns:
        string: API URL that can be used in a request.get() function call.
    """
    return -1