from app.models import db, Type




def seed_types():
    type1 = Type(name='Books')
    type2 = Type(name='Electronics')
    type3 = Type(name='Pets')
    type4 = Type(name='Food')
    type5 = Type(name='Sports')
    type6 = Type(name='Outdoors')
    type7 = Type(name='Automotive')
    type8 = Type(name='Babies')
    type9 = Type(name='Music')
    type10 = Type(name="Movies")
    type11 = Type(name='Health')
    db.session.add(type1)
    db.session.add(type2)
    db.session.add(type3)
    db.session.add(type4)
    db.session.add(type5)
    db.session.add(type6)
    db.session.add(type7)
    db.session.add(type8)
    db.session.add(type9)
    db.session.add(type10)
    db.session.add(type11)
    db.session.commit()
f
f
def undo_types():
    db.session.execute('TRUNCATE types RESTART IDENTITY CASCADE;')
    db.session.commit()
