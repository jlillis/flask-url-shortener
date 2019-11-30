from flask import Flask, render_template, request, redirect
import validators
import hashlib

app = Flask(__name__)

short_urls = []

@app.route('/', methods=("GET", "POST"))
def index():
    """Handle GET and POST requests to the index page."""
    if request.method == "POST":
        # Try reading the input URL from the POST data
        # Flask will raise a KeyError if no URL was provided
        try:
            url_input = request.form["urlInput"]
        except KeyError:
            return render_template("index.html", error_msg="Invalid URL.")

        # Attempt to validate the url
        if not validators.url(url_input, public=True):
            return render_template("index.html", error_msg="Invalid URL.")

        # Generate the md5 hash of the input URL
        url_hash = hashlib.md5(url_input.encode("utf-8")).hexdigest()

        # Use the first 6 characters of the MD5 digest as the shortened URL
        short_urls.append({"url": url_hash, "destination": url_input})

        return render_template("index.html", error_msg=url_hash[:6])


    return render_template("index.html")

@app.route("/<url>")
def redirect_url(url):
    """Redirects the short URL to the input URL."""
    for record in short_urls:
        if record.url == url:
            return redirect(record.destination)
        
    return render_template("index.html", error_msg="Short URL not found.")

@app.route("/urls")
def url_listings():
    """Renders the URL listings page."""
    return render_template("urls.html", urls=short_urls)