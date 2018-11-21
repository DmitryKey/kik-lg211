from flask import Flask, render_template, request, redirect, url_for
from urllib import *

# Initialize Flask instance
app = Flask(__name__)

example_data = [
    {"name": "Cat sleeping on a bed", "source": "cat.jpg"},
    {"name": "Misty forest", "source": "forest.jpg"},
    {"name": "Bonfire burning", "source": "fire.jpg"},
    {"name": "Old library", "source": "library.jpg"},
    {"name": "Sliced orange", "source": "orange.jpg"}
]


# Use "query" variable from the URL. If no variable is given,
# use empty string instead. GET and POST methods are allowed.
@app.route("/search", defaults={"query": ""}, methods=["GET", "POST"])
@app.route("/search/<query>", methods=["GET", "POST"])
def search(query):
    if request.method == "POST":
        # Get query from the POST form.
        query = request.form["query"]

        # Redirect to the same page with the query in the url.
        # ALWAYS REDIRECT AFTER POSTING!
        return redirect(url_for("search", query=query))

    matches = []

    # If an entry name contains the query, add the entry to matches.
    if query != "":
        for entry in example_data:
            if query.lower() in entry["name"].lower():
                matches.append(entry)

    # Render index.html with matches variable.
    return render_template("index.html", matches=matches)


@app.route("/solr", defaults={"query": "cat"}, methods=["GET", "POST"])
@app.route("/solr/<query>", methods=["GET", "POST"])
def solr(query):
    if request.method == "POST":
        # Get query from the POST form.
        query = request.form["query"]

        # Redirect to the same page with the query in the url.
        # ALWAYS REDIRECT AFTER POSTING!
        return redirect(url_for("solr", query=query))

    matches = []

    url = 'http://localhost:8998/solr/wiki/select?q=text:' + query + '&wt=python&start=0&rows=10&fl=title,id,text&hl=on&hl.fl=text&hl.simple.post=</b>&hl.simple.pre=<b>'

    print(url)

    connection = urlopen(url)
    response = eval(connection.read())

    print(response['response']['numFound'], "documents found.")
    print "========================="
    print response['highlighting']
    print "========================="

    # Print the name of each document.

    print("Printing 100 top documents:")

    for i, document in enumerate(response['response']['docs']):
        # print("  Document title ", i, "=", document['title'])
        id = document['id']
        print "id=" + id
        # print(response['response']['highlighting'][id])
        highlight = response['highlighting'][id]['text'][0]
        match = {"title": document['title'], "text": highlight}
        matches.append(match)

    # Render index.html with matches variable.
    return render_template("solr.html", matches=matches)
