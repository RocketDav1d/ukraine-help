from calendar import c
import imp
from app.extenstions.database import db
from app.nav_bar.models import Cookie


def test_cookie_update(client):
    #update cookie's properties
    cookie = Cookie(slug="choco", name="chocolate", price=1.50)
    db.session.add(cookie)
    db.session.commit()

    cookie.name = "peanut"
    cookie.save()

    updated_cookie = Cookie.query.filter_by(slug="choco").first()
    assert updated_cookie.name == "peanut"

def test_delete_cookie(client):
    #delete Cookie
    cookie = Cookie(slug="choco", name="chocolate", price=1.50)
    db.session.add(cookie)
    db.session.commit()

    cookie.delete()

    deleted_cookie = Cookie.query.filter_by(slug="chocolate").first()
    assert deleted_cookie is None

    