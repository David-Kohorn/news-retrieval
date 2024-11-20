from  flask import Flask

app = Flask("__name__")

# All News API route
@app.route("/news")
def get_news():
    return {"text": ["hi"]}

if __name__ == "__main__":
    app.run(debug=True)