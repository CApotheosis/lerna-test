from flask import redirect, render_template, url_for, request

from project import app
from project.forms import SearchForm
from project.models import Cats


@app.route("/")
@app.route("/cats/")
def cat_list():
    page = request.args.get("page", 1, type=int)
    cats = Cats.query.paginate(
        page=page, 
        per_page=app.config["POSTS_PER_PAGE"], 
        error_out=False,
    )
    next_url = url_for("cat_list", page=cats.next_num) if cats.has_next else None
    prev_url = url_for("cat_list", page=cats.prev_num) if cats.has_prev else None
    search_form = SearchForm()
    if search_form.validate_on_submit():
        cats = Cats.query.filter_by(search_form.search.data)
        return redirect(url_for("cat_list", cats=cats))
    return render_template(
        "cat_list.html",
        cats=cats,
        next_url=next_url,
        prev_url=prev_url,
        search_form=search_form,
    )


@app.route("/cats/<int:id>/")
def cat_detail(id):
    cat = Cats.query.get_or_404(id)
    return render_template("cat_detail.html", cat=cat)
