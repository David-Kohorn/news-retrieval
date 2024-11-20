from  flask import Flask
from newsAPIHelperFunctions import *

app = Flask("__name__")

# TODO All news API route 
@app.route("/all-news")
def get_all_news():
    return {"text": ["all-news"]}

# TODO Top headlines news API route
@app.route("/top-news")
def get_top_news():
    return {"text": ["top-news"]}

if __name__ == "__main__":
    app.run(debug=True)