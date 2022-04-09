from app.models import db, Product
    # id=db.Column(db.Integer, primary_key=True)
    # type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)
    # name=db.Column(db.String(255), nullable=False)
    # description=db.Column(db.String(2000), nullable=False)
    # price=db.Column(db.Float, nullable=False)
    # created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

def seed_products():
    book1 = Product(type_id=1, name='The Last Apprentice', description='For years, Old Gregory has been the Spook for the county, ridding the local villages of evil. Now his time is coming to an end. But who will take over for him? Twenty-nine apprentices have tried—some floundered, some fled, some failed to stay alive.', price=35.99, image='https://m.media-amazon.com/images/I/61VThHweiOL._AC_UY436_FMwebp_QL65_.jpg')
    book2 = Product(type_id=1, name='Harry Potter', description="Readers beware. The brilliant, breathtaking conclusion to J.K. Rowling's spellbinding series is not for the faint of heart--such revelations, battles, and betrayals await in Harry Potter and the Deathly Hallows that no fan will make it to the end unscathed. Luckily, Rowling has prepped loyal readers for the end of her series by doling out increasingly dark and dangerous tales of magic and mystery, shot through with lessons about honor and contempt, love and loss, and right and wrong.", price=43.99, image='https://m.media-amazon.com/images/I/71sH3vxziLL._AC_UL640_FMwebp_QL65_.jpg')
    book3 = Product(type_id=1, name='Holes', description="Stanley Yelnats is under a curse. A curse that began with his no-good-dirty-rotten-pig-stealing-great-great-grandfather and has since followed generations of Yelnatses. Now Stanley has been unjustly sent to a boys’ detention center, Camp Green Lake, where the boys build character by spending all day, every day digging holes exactly five feet wide and five feet deep. There is no lake at Camp Green Lake. But there are an awful lot of holes.", price=5.99, image='https://m.media-amazon.com/images/I/814TCW6Y7hL._AC_UY436_FMwebp_QL65_.jpg')
    book4 = Product(type_id=1, name='Series of Unforunate Events', description="Violet, Klaus, and Sunny Baudelaire are intelligent children. They are charming, and resourceful, and have pleasant facial features. Unfortunately, they are exceptionally unlucky.", price=22.99, image="https://m.media-amazon.com/images/I/51Yno8F2hNL._AC_UY436_FMwebp_QL65_.jpg")
    book5=Product(
        type_id=1,
        name="Dr. Seuss's Beginner Book Collection",
        description="This collectible Dr. Seuss boxed set is perfect for inspiring a love of reading, and with five books in one super giftable set, it will complete any beginning reader's shelf!",
        price=22.99,
        image="https://images-na.ssl-images-amazon.com/images/I/51PWDGLykIL._SX339_BO1,204,203,200_.jpg"
      )
    book6=Product(
        type_id=1,
        name="Maid: Hard Work, Low Pay, and a Mother's Will to Survive",
        description="At 28, Stephanie Land's plans of breaking free from the roots of her hometown in the Pacific Northwest to chase her dreams of attending a university and becoming a writer, were cut short when a summer fling turned into an unexpected pregnancy. She turned to housekeeping to make ends meet, and with a tenacious grip on her dream to provide her daughter the very best life possible, Stephanie worked days and took classes online to earn a college degree, and began to write relentlessly.",
        price=22.99,
        image="https://images-na.ssl-images-amazon.com/images/I/51vavZ9ijsL._AC_SX368_.jpg"
      )
    book7=Product(
        type_id=1,
        name="The Handmaid's Tale",
        description="In Margaret Atwood’s dystopian future, environmental disasters and declining birthrates have led to a Second American Civil War. The result is the rise of the Republic of Gilead, a totalitarian regime that enforces rigid social roles and enslaves the few remaining fertile women. Offred is one of these, a Handmaid bound to produce children for one of Gilead’s commanders. Deprived of her husband, her child, her freedom, and even her own name, Offred clings to her memories and her will to survive. At once a scathing satire, an ominous warning, and a tour de force of narrative suspense, The Handmaid’s Tale is a modern classic.",
        price=7.99,
        image="https://images-na.ssl-images-amazon.com/images/I/41vgWYsM82L._AC_SX368_.jpg"
      )
    book8=Product(
        type_id=1,
        name="The Very Hungry Caterpillar",
        description="Featuring interactive die-cut pages, this board book edition is the perfect size for little hands and great for teaching counting and days of the week.",
        price=5.06,
        image="https://images-na.ssl-images-amazon.com/images/I/41w4B0f21VL._AC_SX368_.jpg"
      )
    book9=Product(
        type_id=1,
        name="Dulcan's Textbook of Child and Adolescent Psychiatry 3rd ed. Edition",
        description="The American Psychiatric Association (APA) has updated its Privacy Policy, including with new information specifically addressed to individuals in the European Economic Area. As described in the Privacy Policy, this website utilizes cookies, including for the purpose of offering an optimal online experience and services tailored to your preferences.",
        price=98.50,
        image="https://m.media-amazon.com/images/I/51M08lS-LYL._AC_UL640_FMwebp_QL65_.jpg"
      )
    book10=Product(
        type_id=1,
        name="The Deep, Deep Snow",
        description="Deputy Shelby Lake was abandoned as a baby, saved by a stranger who found her in the freezing cold. Now, years later, a young boy is missing -- and Shelby is the one who must rescue a child. The only evidence of what happened to ten-year-old Jeremiah Sloan is a bicycle left behind on a lonely road. After a desperate search fails to locate him, the close bonds of Shelby's hometown begin to fray under the weight of accusations and suspicion. Everyone around her is keeping secrets. Her adoptive father, her best friend, her best friend's young daughter -- they all have something to hide. Even Shelby is concealing a mistake that could jeopardize her career and her future.",
        price=98.50,
        image="https://m.media-amazon.com/images/I/81F4YQEvsNL._AC_UL640_FMwebp_QL65_.jpg"
      )
    electronics1=Product(
        type_id=2,
        name="WiFi Range Extender Signal Booster up to 5000 sq.ft, Wireless Internet Repeater Wi-Fi Booster",
        description="【Up to 5000 Square Feet】No Blind Spot! Although most WiFi range extender signal devices get stuck behind walls and cement floors, Hyzom delivers ultra-stable bandwidth for Internet surfing, video conferences, online gaming, and even streaming 4K HD video.",
        price=59.99,
        image="https://m.media-amazon.com/images/I/610Ga56awRL._AC_UY436_FMwebp_QL65_.jpg"
      )
    electronics2=Product(
        type_id=2,
        name="Playstation 5",
        description="CPU: 3.5GHz, 8-core AMD Zen 2, Storage: Custom 825GB SSD, RAM: 16GB GDDR6, Disc drive: 4K Blu-ray player, GPU: 10.3 teraflop RDNA 2 GPU PVT GoPdik",
        price=1259.99,
        image="https://m.media-amazon.com/images/I/31Rq-MKrmSL._AC_UY436_FMwebp_QL65_.jpg"
      )
    electronics3=Product(
        type_id=2,
        name="XBox Series S",
        description="Access your favorite entertainment through apps like YouTube, Netflix, and more Enjoy over 100 games right out of the box with a 1 month Xbox Game Pass trialWatch 4K Blu-ray movies and stream 4K video on Netflix, Amazon, Hulu, Microsoft Movies & TV, and more",
        price=309.99,
        image="https://m.media-amazon.com/images/I/71NBQ2a52CL._AC_UY436_FMwebp_QL65_.jpg"
      )

    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.add(book4)
    db.session.add(book5)
    db.session.add(book6)
    db.session.add(book7)
    db.session.add(book8)
    db.session.add(book9)
    db.session.add(book10)
    db.session.add(electronics1)
    db.session.add(electronics2)
    db.session.add(electronics3)

    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
