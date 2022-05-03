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
        image="data:image/jpeg;base64,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"

    )
    pet8 = Product(
        type_id=3,
        name="MAVRICFLEX Weatherproof Dog Door with Sliding Lock Panel",
        description="",
        price=149.99,
        image="https://m.media-amazon.com/images/I/31tr6GpHUlS._AC_SR160,160_.jpg"

    )
    pet9 = Product(
        type_id=3,
        name="Dog Collar",
        description="PetSafe Premium In-Ground Cat Fence Receiver Collar",
        price=199.99,
        image="https://m.media-amazon.com/images/I/41ocw0bmcwL._AC_SR160,160_.jpg"

    )
    pet10 = Product(
        type_id=3,
        name="ION Intelligence of Nature Gut Support for Pets",
        description="By fortifying their gut lining, ION* Gut Support For Pets diversifies your pet’s microbiome the natural way. How? It acts as a catalyst for redox signaling which maintains tight junction integrity in their gut lining.",
        price=32.99,
        image="https://m.media-amazon.com/images/I/614gnVgjNaL._AC_UY218_.jpg"

    )
    pet11 = Product(
        type_id=3,
        name="Power Pet Fully Automatic Pet Door for Wall Installation (Wall Installation, Large)",
        description="",
        price=8.99,
        image="data:image/jpeg;base64,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"

    )
    pet12 = Product(
        type_id=3,
        name="Pet Stairs/Non-Slip-4-Step",
        description="Power Pet doors are motor driven and activated by a tiny ultrasonic collar. Unlike other electronic pet doors that merely unlock a hinged panel, requiring your pet to push it open, Patented Power Pet doors open completely under their own power",
        price=499.99,
        image="https://m.media-amazon.com/images/I/71HM2aJ3wQL._AC_UY218_.jpg"

    )









    food1 = Product(
        type_id=4,
        name="Nestle Waters Poland Spring 100% Natural Spring Water",
        description="Nestle Waters Poland Spring 100% Natural Spring Water, 16.9 oz Plastic Bottles Case of 24 Bottles (78 Cases), 16.9 Fl Oz (Pack of 1872)",
        price=49.99,
        image="https://m.media-amazon.com/images/I/91u80mQvbiL._AC_UL320_.jpg"

    )
    food2 = Product(
        type_id=4,
        name="Pop-Tarts Toaster Pastries",
        description="Pop-Tarts Toaster Pastries, Breakfast Foods, Baked in the USA, Frosted Apple Fritter, 10.1lb Case (12 Boxes) 8 Count (Pack of 12)",
        price=38.38,
        image="https://m.media-amazon.com/images/I/71eDoQL8f-L._AC_UL320_.jpg"

    )
    food3 = Product(
        type_id=4,
        name="Frito-Lay Ultimate Snack Care Package",
        description="($14.98/Count) $20.99$14.23 with Subscribe & Save discoun50% off gift wrap service: code GIFTWRAP50SNAP EBT eligibleFREE Shipping on orders over $25 shipped by Amazon",
        price=1.00,
        image="https://m.media-amazon.com/images/I/A1dBzjL58SL._AC_UL320_.jpg"

    )
    food4 = Product(
        type_id=4,
        name="Reese's Peanut Butter Sauce 4.5 Lbs",
        description="If you love Reese’s peanut butter cups as much as we do—and we love them a lot—then your pantry isn’t complete without a giant tub of Reese’s peanut butter sauce.",
        price=40.20,
        image="https://m.media-amazon.com/images/I/91tg4ZH+08L._AC_UL320_.jpg"

    )
    food5 = Product(
        type_id=4,
        name="Wise Company Long Term Emergency Food Supply",
        description="Wise Company Long Term Emergency Food Supply, Breakfast and Entree Variety, Twelve-120 Serving Buckets (1440 Total Servings)",
        price=1899.00,
        image="https://m.media-amazon.com/images/I/813Y1xsUvYL._AC_UL320_.jpg"

    )
    food6 = Product(
        type_id=4,
        name="Blender BREVILLE",
        description="Breville BFP820BAL Sous Chef 16 Peel & Dice Food Processor, Brushed Aluminum",
        price=512.00,
        image="https://m.media-amazon.com/images/I/71+DrQGlaJL._AC_UL320_.jpg"

    )
    food7 = Product(
        type_id=4,
        name="OatMeal",
        description="Quaker Instant Oatmeal, 4 Flavor Variety Pack, Individual Packets, 48 Count",
        price=14.00,
        image="https://m.media-amazon.com/images/I/911XLyCu1RL._AC_UL320_.jpg"

    )
    food8 = Product(
        type_id=4,
        name="Easy Mac",
        description="Kraft Easy Mac Original Macaroni & Cheese Microwavable Dinner (18 ct Packets)",
        price=6.48,
        image="https://m.media-amazon.com/images/I/81te0dgkN4L._AC_UL320_.jpg"

    )
    food9 = Product(
        type_id=4,
        name="Hot Pockets",
        description="HOT POCKETS Premium Pepperoni Pizza Frozen Sandwiches 12 ct. Box Frozen Food With Mozzarella Cheese",
        price=18.00,
        image="https://m.media-amazon.com/images/I/81bUrSZAg9L._AC_UL320_.jpg"

    )
    food10 = Product(
        type_id=4,
        name="Energy Drinks",
        description="BODYARMOR Sports Drink Sports Beverage, Strawberry Banana, Natural Flavors With Vitamins, Potassium-Packed Electrolytes, No Preservatives, Perfect For",
        price=12.32,
        image="https://m.media-amazon.com/images/I/71gKBo316WL._AC_UL320_.jpg"

    )
    food11 = Product(
        type_id=4,
        name="Grandma's Cookies",
        description="($14.98/Count)$14.23 with Subscribe & Save discount50% off gift wrap service: code GIFTWRAP50SNAP EBT eligible",
        price=14.98,
        image="https://m.media-amazon.com/images/I/91afkHiUzDS._AC_UL320_.jpg"

    )
    food12 = Product(
        type_id=4,
        name="Planets Peanuts",
        description="PLANTERS Deluxe Lightly Salted Whole Cashews, 1lb 2.25oz . Resealable Canister - Lightly Salted Cashews & Lightly Salted Nuts - Nutrient Dense Snacks for Adults ",
        price=32.00,
        image="https://m.media-amazon.com/images/I/81k9r1EnY5L._AC_UL320_.jpg"

    )







    sports1 = Product(
        type_id=5,
        name="Hollywood Racks Sport Rider for Electric Bikes HR-1500-2” Hitch Rack, 2 Bike",
        description="Locking bike frame hooks to deter thefts; includes keyed alike locking hitch pin; Step Thru Bike Frames may require use of a Bike AdapterFits 2 hitches only; Features patented no wobble-no tools hitch tightening system for fast and secure installation; Cannot be used with 1-1/4 to 2 adapter; Not to be used on any trailer, towed vehicle, or fifth wheel",
        price=499.00,
        image="https://m.media-amazon.com/images/I/71PLNLRhjcL._AC_UY218_.jpg"

    )
    sports2 = Product(
        type_id=5,
        name="Golf Bag Storage Rack - Fits 2 Golf Bags",
        description="Golf Bag Storage Rack - Fits 2 Golf Bags, Sports Ball Organizer Stand with Baskets and Hooks, Golf and Sport Equipment Holder Rack, Movable Garage Storage Shelf with Wheel for Garage, Shed, Basement",
        price=149.00,
        image="https://m.media-amazon.com/images/I/81Z+F93AkkL._AC_UY218_.jpg"

    )
    sports3 = Product(
        type_id=5,
        name="Garmin Delta Sport Pro Hunting",
        description="Garmin Delta Sport Pro Hunting Dog Collar Bundle - Water-Resistant, Long-Lasting Dog E-Collar with Handheld Device with Teacher’s Pet Vinyl Dog Training Hunting Dummy Bumper",
        price=124.50,
        image="https://m.media-amazon.com/images/I/716qvFk+APL._AC_UY218_.jpg"

    )
    sports4 = Product(
        type_id=5,
        name="BESTKID BALL Arcade Basketball",
        description="BESTKID BALL Arcade Basketball Hoop Game – Basement Toys – Basketball Hoop for Kids – Basketball Game with Hoop Training System – Kids Indoor Sports Toys – Fun and Entertaining",
        price=294.00,
        image="https://m.media-amazon.com/images/I/714v9ugp-jL._AC_UY218_.jpg"

    )
    sports5 = Product(
        type_id=5,
        name="adidas Boys' Active Sports Athletic Tricot Jogger Pant",
        description="100% Polyester Imported Pull On closure Machine Wash Material: 100% polyester Fit: regular Pockets: 2 front hand",
        price=12.00,
        image="https://m.media-amazon.com/images/I/71WP8RH5pkL._AC_UY218_.jpg"

    )
    sports6 = Product(
        type_id=5,
        name="Polaris 9450 Sport Robotic Pool Cleaner",
        description="Polaris 9450 Sport Robotic Pool Cleaner, Automatic Vacuum for InGround Pools up to 50ft, 60ft Swivel Cable, Wall Climbing Vac w/ Strong Suction & Easy Access Debris Canister",
        price=949.00,
        image="https://m.media-amazon.com/images/I/81XD4hqm66S._AC_UY218_.jpg"

    )
    sports7 = Product(
        type_id=5,
        name="Cramer Team Color Athletic Tape",
        description="Cramer Team Color Athletic Tape for Ankle, Wrist, and Injury Taping, Helps Protect and Prevent Injuries, Promotes Faster Healing, Athletic Training First Aid Supplies, 1.5 Inch, Bulk 32 Roll Case",
        price=63.99,
        image="https://m.media-amazon.com/images/I/61hl7PmY9vL._AC_UY218_.jpg"

    )
    sports8 = Product(
        type_id=5,
        name="AoHu 3-in-1 Hover Hockey Soccer Ball",
        description="AoHu 3-in-1 Hover Hockey Soccer Ball Set for Kids, Rechargeable Led Lights Floating Air Football for Indoor Outdoor Sports Toys Gifts for Boys Girls Ages 3 4 5 6 7 8-12 Years Old",
        price=28.34,
        image="https://m.media-amazon.com/images/I/71SnClQxhML._AC_UY218_.jpg"

    )
    sports9 = Product(
        type_id=5,
        name="BIKESTAR Safety Sport Kids Bike ",
        description="BIKESTAR Safety Sport Kids Bike Bicycle with sidestand for Age 4 Year Old Children | 16 Inch Classic Edition for Boys and Girls |",
        price=149.99,
        image="https://m.media-amazon.com/images/I/81g8XGApZFL._AC_UY218_.jpg"

    )
    sports10 = Product(
        type_id=5,
        name="Duduma Sunglasses",
        description="Duduma Polarized Sports Sunglasses for Men Women Running Cycling Fishing Golf Driving Shades Sun Glasses Tr90",
        price=19.99,
        image="https://m.media-amazon.com/images/I/619VsaQgtZL._AC_UY218_.jpg"

    )
    sports11 = Product(
        type_id=5,
        name="Kick Ball",
        description="Size: 10 diameter ball is the recommended size for Adult kickball but is designed to be fun for kids of all ages Surface: textured, tacky rubber surface that is easy to handle and won't puncture easily or wear down quickly",
        price=1.00,
        image="https://m.media-amazon.com/images/I/91vs-F-5r1S._AC_UY218_.jpg"

    )
    sports12 = Product(
        type_id=5,
        name="Inflatable Football Toss Target",
        description="Inflatable Football Toss Target Party Game, Sports Toys Gear and Gifts for Kids Boys Girls and Family",
        price=1.00,
        image="https://m.media-amazon.com/images/I/81+BRA+MuBL._AC_UY218_.jpg"

    )








    outdoors1 = Product(
        type_id=6,
        name="Best Choice Products",
        description="Best Choice Products Outdoor Hanging Curved Steel Chaise Lounge Chair Swing w/Built-in Pillow and Removable Canopy -Red",
        price=233.49,
        image="https://m.media-amazon.com/images/I/715CqX1BUnL._AC_UL320_.jpg"

    )
    outdoors2 = Product(
        type_id=6,
        name="KaiMeng Patio Furniture",
        description="KaiMeng Patio Furniture Round Outdoor Daybed with Retractable Canopy Wicker Rattan Sectional Sofa for Lawn Garden Backyard Pool (Beige)",
        price=349.99,
        image="https://m.media-amazon.com/images/I/71ZL-w2hm7L._AC_UL320_.jpg"

    )
    outdoors3 = Product(
        type_id=6,
        name="Outdoor speakers",
        description="Blink Outdoor - wireless, weather-resistant HD security camera, two-year battery life, motion detection, set up in minutes – 2 camera kit",
        price=154.06,
        image="https://m.media-amazon.com/images/I/41lLBXd-5YL._AC_UL320_.jpg"

    )
    outdoors4 = Product(
        type_id=6,
        name="Outdoor Lights",
        description="Aialun 96FT LED Outdoor String Lights,Shatterproof Patio Backyard, Upgrade 2200K Warm Light Ambience,Commercial Grade",
        price=17.00,
        image="https://m.media-amazon.com/images/I/71nTCyox8sS._AC_UL320_.jpg"

    )
    outdoors5 = Product(
        type_id=6,
        name="Best Choice Products 10ft Offset Hanging Market Patio",
        description="Aialun 96FT LED Outdoor String Lights,Shatterproof Patio Backyard, Upgrade 2200K Warm Light Ambience,Commercial Grade",
        price=142.89,
        image="https://m.media-amazon.com/images/I/61r94kJ640L._AC_UL320_.jpg"

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
        name="homenote Large Under Grill",
        description="homenote Large Under Grill Mats, Durable 36 x 65 inches Deck and Patio Protective Mats, Fireproof Grill Pads for Outdoor, Perfect for Charcoal Grills, Gas Grills, Oil Fryers and Smokers",
        price=487.89,
        image="https://m.media-amazon.com/images/I/71e-Q1z7szS._AC_UL320_.jpg"

    )
    outdoors8 = Product(
        type_id=6,
        name="Amazon Basics 46,000 BTU Outdoor Propane Patio",
        description="Powerful 46,000 BTU outdoor gas heater provides heat up to a 9 foot radius; ideal for commercial cafes and restaurants or home patiosConstructed with aluminum, plastic, and steel with a durable powder-coated finish",
        price=131.58,
        image="https://m.media-amazon.com/images/I/611AH1RdrLL._AC_UL320_.jpg"

    )
    outdoors9 = Product(
        type_id=6,
        name="SOLPEX Solar Deck Lights Outdoor ",
        description="SOLPEX Solar Deck Lights Outdoor 16 Pack, Solar Step Lights Waterproof Led Solar lights for Outdoor Stairs, Step , Fence, Yard, Patio, and Pathway(Warm",
        price=39.99,
        image="https://m.media-amazon.com/images/I/71SqsmIpekL._AC_UL320_.jpg"

    )
    outdoors10 = Product(
        type_id=6,
        name="Solar Lights Outdoor with Motion Senso",
        description="Solar Lights Outdoor with Motion Sensor, WICOLO Security Lights with Remote Control 4 Rotatable Heads 228 LEDs 7000K IP65 Waterproof Flood Lights for",
        price=188.99,
        image="https://m.media-amazon.com/images/I/71qozlNjWCL._AC_UL320_.jpg"

    )
    outdoors11 = Product(
        type_id=6,
        name="3 Piece Outdoor Furniture Set Patio",
        description="3 Piece Outdoor Furniture Set Patio Wicker Chairs Furniture Bistro Conversation Set 2 Rattan Chairs with Blue Cushions and Glass Coffee Table for Porch Lawn Garden",
        price=155.21,
        image="https://m.media-amazon.com/images/I/61PKqwVFulL._AC_UL320_.jpg"

    )
    outdoors12 = Product(
        type_id=6,
        name="Outdoor Bluetooth Speaker with Ligh",
        description="Outdoor Bluetooth Speaker with Light, Realistic Flame Effect, Sync up to 100 Wireless Portable Speaker with Wall Mount/Stake/Hook, Waterproof for",
        price=20.99,
        image="https://m.media-amazon.com/images/I/81orC1l2+8L._AC_UL320_.jpg"

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








    movies1 = Product(
        type_id=10,
        name="",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQudt5t_EZf55GHHTHhDogYg1HvLhU3-3Y6bQ&usqp=CAU"

    )

    movies2 = Product(
        type_id=10,
        name="Harry Potter 1",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3DhkzTf_OxvG6690L3HHBVfb5GBK96_4eHA&usqp=CAU"

    )
    movies3 = Product(
        type_id=10,
        name="Joker",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwM8sRQ_CrNfrWnrT-Pl2uvkfJZa5eA9ypgg&usqp=CAU"

    )
    movies4 = Product(
        type_id=10,
        name="Uncharted",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTand8zTxuYCbBygvgJdXcXjtbM_Xx7OgGD2A&usqp=CAU"

    )
    movies5 = Product(
        type_id=10,
        name="Avatar",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThY0TTfIT4MbS2tcS95yoH4MeJTfbe-w45FA&usqp=CAU"

    )
    movies6 = Product(
        type_id=10,
        name="Black Swan",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoUg2t__lqkZBIjqycnh_G70HR-Qq2yRmHCQ&usqp=CAU"

    )
    movies7 = Product(
        type_id=10,
        name="Avengers",
        description="",
        price=1.00,
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmmzEXBR-Xu9AWSxTNV55f8tl0RDLT_vvl8g&usqp=CAU"

    )
    movies8 = Product(
        type_id=10,
        name="The ",
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
    db.session.add(pet8)
    db.session.add(pet9)
    db.session.add(pet10)
    db.session.add(pet11)
    db.session.add(pet12)

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
