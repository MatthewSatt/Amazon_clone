            # 'id': self.id,
            # 'user_id': self.user_id,
            # 'product_id': self.product_id,
            # 'title': self.title,
            # 'body': self.body,
            # 'rating': self.rating,
            # 'created_at': self.created_at,
            # 'updated_at': self.updated_at
from app.models import db, Review
def seed_reviews():
    review1 = Review(
        user_id=1,
        product_id=1,
        title='One of my favorites',
        body='This is a very well written book with an interesting plot and good story. However, it is probably one of the more scary books I have ever read. There is no way it should be shelved in the juvenile fiction part of the library - definitely more young adult.',
        rating=5
        )
    review2 = Review(
        user_id=2,
        product_id=1,
        title='Not that great',
        body='Just like a classic: scary, entertaining, and has a plot like a fairytale. Revenge of the witch is played out just like a Grimm brothers tale: dark but yet entertaining with positive messages. There is a fair handful of violence, but Mr. Gregory advises against it often',
        rating=2
        )
    review3 = Review(
        user_id=3,
        product_id=1,
        title='Decent Book',
        body='Joseph DELANEY is the author of the internationally best-selling The Last Apprentice series, which is now a major motion picture, Seventh Son. He is a former English teacher who lives in the heart of boggart territory in Lancashire, England.',
        rating=4
        )

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.commit()



def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()
