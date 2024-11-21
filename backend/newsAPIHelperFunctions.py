import requests

API_KEY = "773a9dc7cd75450d8c850256149561a6"

# Function to create everything URL with given parameters for making API request
def createURLEverything(q, fromDate, toDate):
    """
    Constructs an API URL for the "everything" endpoint.

    Args:
        q (string): Keyword surrounded in quotes 
        fromDate (string): Date and time for oldest article allowed (2024-11-20 or 2024-11-20T03:55:31)
        toDate (string): Date and time for newest artciles allowed

    Returns:
        string: API URL that can be used in a request.get() function call.
    """
    q_string = f"q=\"{q}\""
    fromDate_string = f"from={fromDate}"
    toDate_string = f"to={toDate}"

    url = f"https://newsapi.org/v2/everything?{q_string}&{fromDate_string}&{toDate_string}&language=en&sortBy=popularity&apiKey={API_KEY}"

    return url

# Function to create top-headlines URL with given parameters for making API request
def createURLTop(country, q):
    """
    Constructs an API URL for the "top-headlines" endpoint.

    Args:
        country (string): 2 letter ISO code for country (us, ja, ch)
        q (string): Keyword surrounded in quotes

    Returns:
        string: API URL that can be used in a request.get() function call.
    """
    country_string = f"country={country}"
    q_string = f"q=\"{q}\""

    url = f"https://newsapi.org/v2/top-headlines?{country_string}&{q_string}&apiKey={API_KEY}"

    return url


# Make API request and return results for given URL
def getResponseJSON (url):
    """
    Requests data from News API given URL destination.

    Args:
        url (string): URL to make the request to

    Returns:
        string: JSON formatted data from the response.
    """
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Response Error {response.status_code}.")
