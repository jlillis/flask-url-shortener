from app import app, db
from app.models import ShortURL
from flask import render_template, request, redirect
import validators
import hashlib

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
        short_url = ShortURL(identifier=url_hash[:8], destination=url_input, hits=0)
        db.session.add(short_url)
        db.session.commit()
        #short_urls.append({"url": url_hash, "destination": url_input})

        return render_template("index.html", error_msg=short_url)


    return render_template("index.html")

@app.route("/<url>")
def redirect_url(url):
    """Redirects the short URL to the input URL."""
    for short_url in ShortURL.query.all():
        if short_url.identifier == url:
            # Increment number of hits for this URL
            short_url.hits += 1
            db.session.commit()
            return redirect(short_url.destination)
        
    return render_template("index.html", error_msg="Short URL not found.")

@app.route("/top10")
def top10():
    """Renders the top 10 page."""
    top10_urls = ShortURL.query.order_by(ShortURL.hits.desc()).limit(10)
    return render_template("top10.html", urls=top10_urls)