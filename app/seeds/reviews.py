from sqlalchemy import text
from app.models.db import qualified
from app.models import db, Review

# (user_id, product_id, rating, title, body)
REVIEWS = [
    (1, 1, 5, 'Gripping from the first chapter',
     'A properly creepy story with a great sense of atmosphere. It is darker than the shelf it sits on suggests, so probably best for older readers.'),
    (2, 1, 3, 'Good, but not for everyone',
     'Fairytale-style horror with plenty of menace. The pacing drags a little in the middle, though the ending makes up for it.'),
    (3, 1, 4, 'Great start to a series',
     'Solid world-building and a likeable narrator. I finished it in two evenings and immediately ordered the next one.'),
    (2, 3, 5, 'Still holds up',
     'Read it as a kid and just picked it up again. The way the storylines connect is every bit as clever as I remembered.'),
    (3, 7, 5, 'Timeless and unsettling',
     'Beautifully written and more relevant than ever. A book that stays with you long after the last page.'),
    (1, 11, 5, 'Practical and easy to apply',
     'Clear ideas, short chapters and real examples. I started two small habits the same week and both have stuck.'),
    (2, 13, 4, 'Fixed our dead spots',
     'Setup took about five minutes and the signal in the back bedroom went from one bar to full. Speeds are noticeably better.'),
    (1, 15, 4, 'Great little console',
     'Quiet, fast and plays everything I care about. Wish the internal storage were larger, but it is easy to expand.'),
    (3, 16, 4, 'Worth the money',
     'Bright screen, good speakers and the battery lasts all week for casual use. Perfect for the couch.'),
    (2, 18, 5, 'Pairs instantly',
     'Connect to my phone in seconds, sound is clear and they stay put on my commute. Battery life is solid.'),
    (1, 18, 4, 'Comfortable all day',
     'Nice fit and reliable connection. The case is a bit slippery but I have no real complaints.'),
    (3, 9, 2, 'Very specialised',
     'Comprehensive, but it is a dense clinical textbook and priced accordingly. Only buy it if your course requires it.'),
]


def seed_reviews():
    for user_id, product_id, rating, title, body in REVIEWS:
        db.session.add(Review(
            user_id=user_id, product_id=product_id, rating=rating, title=title, body=body))
    db.session.commit()


def undo_reviews():
    db.session.execute(text(f'TRUNCATE {qualified("reviews")} RESTART IDENTITY CASCADE;'))
    db.session.commit()
