from app.models import db, Product

def seed_products():
    product1 = Product(
        title='Lg Series TV Widescreen',
        description="Tv for home use 55 inches with a lasting screen",
        image="https://m.media-amazon.com/images/I/A1-qZyLRDuS._AC_SL1500_.jpg",
        price=599.99,
        rating=4,
        userId=1)
    product2 = Product(
        title='Huggies',
        description="Baby Wipes, Huggies Natural Care Sensitive Baby Diaper Wipes, Unscented, Hypoallergenic, 10 Flip-Top Packs",
        image="https://m.media-amazon.com/images/I/816Qm+QszcS._AC_SL1500_.jpg",
        price=25.99,
        rating=3,
        userId=1)
    product3 = Product(
        title='Boots',
        description="Dickies Men's Dri-tech Moisture Control Crew Socks Multipack",
        image="https://m.media-amazon.com/images/I/41LvUP4I2RL._SX38_SY50_CR,0,0,38,50_.jpg",
        price=16.99,
        rating=4,
        userId=1)
    product4 = Product(
        title='Bluerams Camera',
        description="Security Camera 2K, blurams Baby Monitor Dog Camera 360-degree for Home Security",
        image="https://m.media-amazon.com/images/I/514Q-oBHk7L._AC_SL1500_.jpg",
        price=40.98,
        rating=4,
        userId=1)
    product5 = Product(
        title='USBC Cord',
        description="USB C to DisplayPort VESA Certified, Maxonar 8K 60Hz Type-C to DP Cable",
        image="https://m.media-amazon.com/images/I/715Au6mknaL._AC_SL1500_.jpg",
        price=23.89,
        rating=3,
        userId=1)
    product6 = Product(
        title='H&R block',
        description="H&R Block Tax Software Deluxe + State 2021",
        image="https://m.media-amazon.com/images/I/51EN+1-mtoL._AC_SL1000_.jpg",
        price=34.99,
        rating=2,
        userId=1)
    product7 = Product(
        title='Batteries',
        description="Amazon Basics 10 Pack AAA High-Performance Alkaline Batteries, 10-Year Shelf Life",
        image="https://m.media-amazon.com/images/I/61wXhHl7uxL._AC_SL1415_.jpg",
        price=48.99,
        rating=4,
        userId=1)
    product8 = Product(
        title='Tape',
        description="EZlifego Double Sided Tape Heavy Duty (9.85FT)",
        image="https://m.media-amazon.com/images/I/61V0o79n41L._SL1500_.jpg",
        price=15.99,
        rating=3,
        userId=1)
    product9 = Product(
        title='Battleship',
        description="Battleship With Planes Strategy Board Game",
        image="https://m.media-amazon.com/images/I/91bDu7cDe4L._AC_SL1500_.jpg",
        price=10.99,
        rating=5,
        userId=1)
    product10 = Product(
        title='Connect 4',
        description="Connect 4 board game",
        image="https://m.media-amazon.com/images/I/81G-T0HGOhL._AC_SL1500_.jpg",
        price=7.99,
        rating=3,
        userId=1)
    product11 = Product(
        title='Uno',
        description="Uno board game",
        image="https://m.media-amazon.com/images/I/81LcVsRKnjS._AC_SL1500_.jpg",
        price=5.99,
        rating=3,
        userId=1)
    product12 = Product(
        title='Mario Kingdoms',
        description="Nintendo Switch Mario Kingdoms ages(4+)",
        image="https://m.media-amazon.com/images/I/8142IK7mMuL._SL1500_.jpg",
        price=54.99,
        rating=2,
        userId=1)
    product13 = Product(
        title='Gameboy',
        description="Handheld Games Console for Kids Adults - Retro Video Games Consoles",
        image="https://m.media-amazon.com/images/I/61J0iiHkohL._AC_SL1500_.jpg",
        price=56.49,
        rating=2,
        userId=1)

    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.add(product6)
    db.session.add(product7)
    db.session.add(product8)
    db.session.add(product9)
    db.session.add(product10)
    db.session.add(product11)
    db.session.add(product12)
    db.session.add(product13)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_products():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
