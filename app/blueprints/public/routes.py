from flask import render_template, send_from_directory, current_app

from ...portfolio import get_portfolio_store
from . import bp

@bp.get("/")
def index():
    store = get_portfolio_store()
    items = store.list_items()
    return render_template("index.html", portfolio_items=items)

# later: load post by slug; for now just show blank template
@bp.get("/blog")
def blog():
    return render_template("blog.html")

@bp.get("/resume")
def resume():
    # serves the file from static/files/
    return send_from_directory(
        current_app.static_folder + "/tran" + "/files",
        "resume.pdf",
        mimetype="application/pdf"
    )
    
