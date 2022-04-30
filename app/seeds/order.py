from app.models import db, Order




def seed_orders():
    order1 = Order(user_id=1, product_id=1)
    order2 = Order(user_id=1, product_id=2)
    order3 = Order(user_id=1, product_id=3)
    order4 = Order(user_id=1, product_id=4)
    order5 = Order(user_id=1, product_id=5)
    order6 = Order(user_id=2, product_id=6)
    order7 = Order(user_id=2, product_id=7)
    order8 = Order(user_id=2, product_id=8)
    order9 = Order(user_id=2, product_id=9)
    order10 = Order(user_id=2, product_id=10)
    order11 = Order(user_id=3, product_id=11)
    order12 = Order(user_id=3, product_id=12)
    order13 = Order(user_id=3, product_id=13)
    order14 = Order(user_id=3, product_id=14)
    order15 = Order(user_id=3, product_id=15)


    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)
    db.session.add(order4)
    db.session.add(order5)
    db.session.add(order6)
    db.session.add(order7)
    db.session.add(order8)
    db.session.add(order9)
    db.session.add(order10)
    db.session.add(order11)
    db.session.add(order12)
    db.session.add(order13)
    db.session.add(order14)
    db.session.add(order15)
    db.session.commit()


def undo_orders():
    db.session.execute('TRUNCATE orders RESTART IDENTITY CASCADE;')
    db.session.commit()
