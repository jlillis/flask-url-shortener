from flask import Flask, render_template, request, redirect
import validators
import hashlib

app = Flask(__name__)

short_urls = {}

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
        
        print("URL input: "+url_input)

        # Generate the md5 hash of the input URL
        url_hash = hashlib.md5(url_input.encode("utf-8")).hexdigest()

        # Use the first 6 characters of the MD5 digest as the shortened URL
        short_urls[url_hash[:6]] = url_input

        return render_template("index.html", error_msg=url_hash[:6])


    return render_template("index.html")

@app.route("/<short_url>")
def redirect_short_url(short_url):
    """Redirects the short URL to the input URL."""
    for record in short_urls.keys():
        if record == short_url:
            return redirect(short_urls[record])
        
    return render_template("index.html", error_msg="Short URL not found.")