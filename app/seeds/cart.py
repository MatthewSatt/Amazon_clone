from sqlalchemy import text
from app.models.db import qualified
from app.models import db, Cart




def seed_carts():
    cart1 = Cart(user_id=1, product_id=1, quantity=3)
    cart2 = Cart(user_id=2, product_id=2, quantity=6)
    cart3 = Cart(user_id=3, product_id=6, quantity=1)
    cart4 = Cart(user_id=3, product_id=13, quantity=2)



    db.session.add(cart1)
    db.session.add(cart2)
    db.session.add(cart3)
    db.session.add(cart4)
    db.session.commit()


def undo_carts():
    db.session.execute(text(f'TRUNCATE {qualified("carts")} RESTART IDENTITY CASCADE;'))
    db.session.commit()
