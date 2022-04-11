from cgi import test
from app.app import create_app
from app.nav_bar.models import User, Housing, Cookie
from app.extenstions.database import db

app = create_app()
app.app_context().push()



cookie_data = {
  'housing1' : {'name': 'Chocolate Chip', 'price': 1.50},
  'housing2' : {'name': 'Oatmeal Raisin', 'price': 1.00},
  'housing3' : {'name': 'Sugar', 'price': 0.75},
  'peanut-butter' : {'name': 'Peanut Butter', 'price': 0.50},
  'oatmeal' : {'name': 'Oatmeal', 'price': 0.25},
  'salted-caramel' : {'name': 'Salted Caramel', 'price': 1.00},
}


for slug, cookie in cookie_data.items():
    new_cookie = Cookie(slug=slug, name=cookie['name'], price=cookie['price'])
    db.session.add(new_cookie)

db.session.commit()