from app.models import db, Product
    # id=db.Column(db.Integer, primary_key=True)
    # type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)
    # name=db.Column(db.String(255), nullable=False)
    # description=db.Column(db.String(2000), nullable=False)
    # price=db.Column(db.Float, nullable=False)
    # created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

def seed_products():
    product1 = Product(type_id=1, name='The Last Apprentice', description='Wonderful Book for the whole family. Great for falling asleep to', price=35.99)
    product2 = Product(type_id=1, name='Harry Potter', description='Book about wizard and magic. Great for falling asleep to', price=43.99)
    product3 = Product(type_id=1, name='Holes', description='Boy avoids prison to dig holes to find treasure', price=5.99)
    product4 = Product(type_id=1, name='Series of Unforunate Events', description='A not so fortunate series of events happen to orphans', price=22.99)
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
