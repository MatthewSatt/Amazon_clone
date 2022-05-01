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
    book11=Product(
        type_id=1,
        name="Atomic Habits",
        description="Goals are about the results you want to achieve. Systems are about the processes that lead to those results.",
        price=11.98,
        image="https://images-na.ssl-images-amazon.com/images/I/51-uspgqWIL._AC_SX184_.jpg"
      )
    book12=Product(
        type_id=1,
        name="Slow Horses",
        description="Everyone wanted a life less ordinary. And only a tiny minority ever got it, and even they probably didn’t appreciate it much..",
        price=11.69,
        image="https://images-na.ssl-images-amazon.com/images/I/51qzR6Ok+fL._AC_SX184_.jpg"
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
    electronics4=Product(
        type_id=2,
        name="Fire HD 10 tablet, 10.1, 1080p Full HD, 32 GB, latest model (2021 release), Black",
        description="Fast and responsive - powerful octa-core processor and 3 GB RAM. 50% more RAM than previous generation. Long-lasting 12-hour battery and 32 or 64 GB internal storage. Add up to 1 TB with microSD (sold separately). Brighter display - Vivid 10.1 1080p Full HD display is 10% brighter than previous generation, with more than 2 million pixels.",
        price=149.99,
        image="https://m.media-amazon.com/images/I/61uE03cRsyS._AC_UY218_.jpg"
      )
    electronics5=Product(
        type_id=2,
        name="TCL 32-inch 1080p Roku Smart LED TV - 32S327, 2019 Model",
        description="CPU: 3.5GHz, 8-core AMD Zen 2, Storage: Custom 825GB SSD, RAM: 16GB GDDR6, Disc drive: 4K Blu-ray player, GPU: 10.3 teraflop RDNA 2 GPU PVT GoPdik",
        price=178.99,
        image="https://m.media-amazon.com/images/I/71wYJc19PiL._AC_UY218_.jpg"
      )
    electronics6=Product(
        type_id=2,
        name="Apple AirPods (2nd Generation)",
        description="Quick access to Siri by saying “ Hey Siri ” More than 24 hours total listening time with the Charging Case Effortless setup, in-ear detection, and automatic switching for a magical experience",
        price=118.99,
        image="https://m.media-amazon.com/images/I/7120GgUKj3L._AC_UY218_.jpg"
      )
    electronics7=Product(
        type_id=2,
        name="Echo Dot (3rd Gen, 2018 release) - Smart speaker with Alexa - Charcoal",
        description="Meet Echo Dot - Our most compact smart speaker that fits perfectly into small spaces. Improved speaker quality - Better speaker quality than Echo Dot Gen 2 for richer and louder sound. Pair with a second Echo Dot for stereo sound.",
        price=24.99,
        image="https://m.media-amazon.com/images/I/610Ga56awRL._AC_UY436_FMwebp_QL65_.jpg"
      )
    electronics8=Product(
        type_id=2,
        name="Playstation 5",
        description="CPU: 3.5GHz, 8-core AMD Zen 2, Storage: Custom 825GB SSD, RAM: 16GB GDDR6, Disc drive: 4K Blu-ray player, GPU: 10.3 teraflop RDNA 2 GPU PVT GoPdik",
        price=1259.99,
        image="https://m.media-amazon.com/images/I/31Rq-MKrmSL._AC_UY436_FMwebp_QL65_.jpg"
      )
    electronics9=Product(
        type_id=2,
        name="XBox Series S",
        description="Access your favorite entertainment through apps like YouTube, Netflix, and more Enjoy over 100 games right out of the box with a 1 month Xbox Game Pass trialWatch 4K Blu-ray movies and stream 4K video on Netflix, Amazon, Hulu, Microsoft Movies & TV, and more",
        price=309.99,
        image="https://m.media-amazon.com/images/I/71NBQ2a52CL._AC_UY436_FMwebp_QL65_.jpg"
      )
    electronics10=Product(
        type_id=2,
        name="WiFi Range Extender Signal Booster up to 5000 sq.ft, Wireless Internet Repeater Wi-Fi Booster",
        description="【Up to 5000 Square Feet】No Blind Spot! Although most WiFi range extender signal devices get stuck behind walls and cement floors, Hyzom delivers ultra-stable bandwidth for Internet surfing, video conferences, online gaming, and even streaming 4K HD video.",
        price=59.99,
        image="https://m.media-amazon.com/images/I/610Ga56awRL._AC_UY436_FMwebp_QL65_.jpg"
      )
    electronics11=Product(
        type_id=2,
        name="Playstation 5",
        description="CPU: 3.5GHz, 8-core AMD Zen 2, Storage: Custom 825GB SSD, RAM: 16GB GDDR6, Disc drive: 4K Blu-ray player, GPU: 10.3 teraflop RDNA 2 GPU PVT GoPdik",
        price=1259.99,
        image="https://m.media-amazon.com/images/I/31Rq-MKrmSL._AC_UY436_FMwebp_QL65_.jpg"
      )
    electronics12=Product(
        type_id=2,
        name="XBox Series S",
        description="Access your favorite entertainment through apps like YouTube, Netflix, and more Enjoy over 100 games right out of the box with a 1 month Xbox Game Pass trialWatch 4K Blu-ray movies and stream 4K video on Netflix, Amazon, Hulu, Microsoft Movies & TV, and more",
        price=309.99,
        image="https://m.media-amazon.com/images/I/71NBQ2a52CL._AC_UY436_FMwebp_QL65_.jpg"
      )
    pet1 = Product(
        type_id=3,
        name="Bissell 74R7 Pet Stain & Odor Portable Machine Formula, 32-Ounce, Fl Oz",
        description="Full HD Camera & Night Vision: livestream video to monitor your pet with a wide-angle view,that functions even in pitch black, without disturbing those being monitored. It also features an intelligent system to ensure clear and high-quality images day and night.",
        price=129.99,
        image="https://m.media-amazon.com/images/I/61E90Y7EEdS._AC_UY436_FMwebp_QL65_.jpg"

    )
    pet2 = Product(
        type_id=3,
        name="WOpet Smart Pet Camera:Dog Treat Dispenser, Full HD WiFi Pet Camera with Night Vision for Pet Viewing,Two Way Audio Communication",
        description="Full HD Camera & Night Vision: livestream video to monitor your pet with a wide-angle view,that functions even in pitch black, without disturbing those being monitored. It also features an intelligent system to ensure clear and high-quality images day and night.",
        price=129.99,
        image="https://m.media-amazon.com/images/I/615CxGedJpL._AC_UY436_FMwebp_QL65_.jpg"

    )
    pet3 = Product(
        type_id=3,
        name="WOpet Smart Pet Camera:Dog Treat Dispenser, Full HD WiFi Pet Camera with Night Vision for Pet Viewing,Two Way Audio Communication",
        description="Full HD Camera & Night Vision: livestream video to monitor your pet with a wide-angle view,that functions even in pitch black, without disturbing those being monitored. It also features an intelligent system to ensure clear and high-quality images day and night.",
        price=129.99,
        image="https://m.media-amazon.com/images/I/71XFKVLXXjL._AC_UY436_FMwebp_QL65_.jpg"

    )
    pet4 = Product(
        type_id=3,
        name="WOpet Smart Pet Camera:Dog Treat Dispenser, Full HD WiFi Pet Camera with Night Vision for Pet Viewing,Two Way Audio Communication",
        description="Full HD Camera & Night Vision: livestream video to monitor your pet with a wide-angle view,that functions even in pitch black, without disturbing those being monitored. It also features an intelligent system to ensure clear and high-quality images day and night.",
        price=129.99,
        image="https://m.media-amazon.com/images/I/81dABCf4jCL._AC_UY436_FMwebp_QL65_.jpg"

    )
    pet5 = Product(
        type_id=3,
        name="The Pet Climber Thing",
        description="Full HD Camera & Night Vision: livestream video to monitor your pet with a wide-angle view,that functions even in pitch black, without disturbing those being monitored. It also features an intelligent system to ensure clear and high-quality images day and night.",
        price=129.99,
        image="https://m.media-amazon.com/images/I/21wge1Dq22L._AC_UY436_FMwebp_QL65_.jpg"

    )
    pet6 = Product(
        type_id=3,
        name="Dog Bowl",
        description="Full HD Camera & Night Vision: livestream video to monitor your pet with a wide-angle view,that functions even in pitch black, without disturbing those being monitored. It also features an intelligent system to ensure clear and high-quality images day and night.",
        price=129.99,
        image="https://st2.depositphotos.com/1504385/10861/i/600/depositphotos_108614828-stock-photo-natural-and-dry-dogs-food.jpg"

    )
    pet7 = Product(
        type_id=3,
        name="Dog Food",
        description="",
        price=8.99,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food1 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food2 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food3 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food4 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food5 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food6 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food7 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food8 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food9 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food10 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food11 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    food12 = Product(
        type_id=4,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )

    sports1 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports2 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports3 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports4 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports5 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports6 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports7 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports8 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports9 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports10 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports11 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    sports12 = Product(
        type_id=5,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )

    outdoors1 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors2 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors3 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors4 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors5 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors6 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors7 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors8 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors9 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors10 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors11 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    outdoors12 = Product(
        type_id=6,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive1 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive2 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive3 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive4 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive5 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive6 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive7 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive8 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive9 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive10 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive11 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    automotive12 = Product(
        type_id=7,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies1 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies2 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies3 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies4 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies5 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies6 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies7 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies8 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies9 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies10 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies11 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    babies12 = Product(
        type_id=8,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music1 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music2 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music3 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music4 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music5 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music6 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music7 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music8 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music9 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music10 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music11 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    music12 = Product(
        type_id=9,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )


        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThY0TTfIT4MbS2tcS95yoH4MeJTfbe-w45FA&usqp=CAU"className="movieimage"></img>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoUg2t__lqkZBIjqycnh_G70HR-Qq2yRmHCQ&usqp=CAU"className="movieimage"></img>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmmzEXBR-Xu9AWSxTNV55f8tl0RDLT_vvl8g&usqp=CAU"className="movieimage"></img>
    movies1 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQudt5t_EZf55GHHTHhDogYg1HvLhU3-3Y6bQ&usqp=CAU"

    )
    movies2 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3DhkzTf_OxvG6690L3HHBVfb5GBK96_4eHA&usqp=CAU"

    )
    movies3 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwM8sRQ_CrNfrWnrT-Pl2uvkfJZa5eA9ypgg&usqp=CAU"

    )
    movies4 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTand8zTxuYCbBygvgJdXcXjtbM_Xx7OgGD2A&usqp=CAU"

    )
    movies5 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    movies6 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    movies7 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    movies8 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    movies9 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    movies10 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    movies11 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    movies12 = Product(
        type_id=10,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health1 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health2 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health3 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health4 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health5 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health6 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health7 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health8 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health9 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health10 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health11 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

    )
    health12 = Product(
        type_id=11,
        name="Replace",
        description="",
        price=1.00,
        image="https://www.iams.com/sites/g/files/fnmzdf386/files/migrate-product-files/images/ugrp5w7bxhsd9ltxey7d.png"

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
    db.session.add(book11)
    db.session.add(book12)

    db.session.add(electronics1)
    db.session.add(electronics2)
    db.session.add(electronics3)
    db.session.add(electronics4)
    db.session.add(electronics5)
    db.session.add(electronics6)
    db.session.add(electronics7)
    db.session.add(electronics8)
    db.session.add(electronics9)
    db.session.add(electronics10)
    db.session.add(electronics11)
    db.session.add(electronics12)

    db.session.add(pet1)
    db.session.add(pet2)
    db.session.add(pet3)
    db.session.add(pet4)
    db.session.add(pet5)
    db.session.add(pet6)
    db.session.add(pet7)

    db.session.add(food1)
    db.session.add(food2)
    db.session.add(food3)
    db.session.add(food4)
    db.session.add(food5)
    db.session.add(food6)
    db.session.add(food7)
    db.session.add(food8)
    db.session.add(food9)
    db.session.add(food10)
    db.session.add(food11)
    db.session.add(food12)

    db.session.add(sports1)
    db.session.add(sports2)
    db.session.add(sports3)
    db.session.add(sports4)
    db.session.add(sports5)
    db.session.add(sports6)
    db.session.add(sports7)
    db.session.add(sports8)
    db.session.add(sports9)
    db.session.add(sports10)
    db.session.add(sports11)
    db.session.add(sports12)

    db.session.add(outdoors1)
    db.session.add(outdoors2)
    db.session.add(outdoors3)
    db.session.add(outdoors4)
    db.session.add(outdoors5)
    db.session.add(outdoors6)
    db.session.add(outdoors7)
    db.session.add(outdoors8)
    db.session.add(outdoors9)
    db.session.add(outdoors10)
    db.session.add(outdoors11)
    db.session.add(outdoors12)

    db.session.add(automotive1)
    db.session.add(automotive2)
    db.session.add(automotive3)
    db.session.add(automotive4)
    db.session.add(automotive5)
    db.session.add(automotive6)
    db.session.add(automotive7)
    db.session.add(automotive8)
    db.session.add(automotive9)
    db.session.add(automotive10)
    db.session.add(automotive11)
    db.session.add(automotive12)

    db.session.add(babies1)
    db.session.add(babies2)
    db.session.add(babies3)
    db.session.add(babies4)
    db.session.add(babies5)
    db.session.add(babies6)
    db.session.add(babies7)
    db.session.add(babies8)
    db.session.add(babies9)
    db.session.add(babies10)
    db.session.add(babies11)
    db.session.add(babies12)

    db.session.add(music1)
    db.session.add(music2)
    db.session.add(music3)
    db.session.add(music4)
    db.session.add(music5)
    db.session.add(music6)
    db.session.add(music7)
    db.session.add(music8)
    db.session.add(music9)
    db.session.add(music10)
    db.session.add(music11)
    db.session.add(music12)

    db.session.add(movies1)
    db.session.add(movies2)
    db.session.add(movies3)
    db.session.add(movies4)
    db.session.add(movies5)
    db.session.add(movies6)
    db.session.add(movies7)
    db.session.add(movies8)
    db.session.add(movies9)
    db.session.add(movies10)
    db.session.add(movies11)
    db.session.add(movies12)

    db.session.add(health1)
    db.session.add(health2)
    db.session.add(health3)
    db.session.add(health4)
    db.session.add(health5)
    db.session.add(health6)
    db.session.add(health7)
    db.session.add(health8)
    db.session.add(health9)
    db.session.add(health10)
    db.session.add(health11)
    db.session.add(health12)


    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
