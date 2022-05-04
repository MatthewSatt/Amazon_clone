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
        image="https://m.media-amazon.com/images/I/51maMLyRs4L._AC_UY218_.jpg"
      )
    electronics8=Product(
        type_id=2,
        name="Razer Keyboard",
        description="CPU: 3.5GHz, 8-core AMD Zen 2, Storage: Custom 825GB SSD, RAM: 16GB GDDR6, Disc drive: 4K Blu-ray player, GPU: 10.3 teraflop RDNA 2 GPU PVT GoPdik",
        price=159.99,
        image="https://m.media-amazon.com/images/I/61BsbJkWSSS._AC_UL320_.jpg"
      )
    electronics9=Product(
        type_id=2,
        name="Lenovo ThinkVision",
        description="Access your favorite entertainment through apps like YouTube, Netflix, and more Enjoy over 100 games right out of the box with a 1 month Xbox Game Pass trialWatch 4K Blu-ray movies and stream 4K video on Netflix, Amazon, Hulu, Microsoft Movies & TV, and more",
        price=309.99,
        image="https://m.media-amazon.com/images/I/71zNBOOYAVL._AC_UL320_.jpg"
      )
    electronics10=Product(
        type_id=2,
        name="PRJ 5G WiFi Projector",
        description="【Up to 5000 Square Feet】No Blind Spot! Although most WiFi range extender signal devices get stuck behind walls and cement floors, Hyzom delivers ultra-stable bandwidth for Internet surfing, video conferences, online gaming, and even streaming 4K HD video.",
        price=59.99,
        image="https://m.media-amazon.com/images/I/61bZ3-m1UzL._AC_UL320_.jpg"
      )
    electronics11=Product(
        type_id=2,
        name="Desktop Cooling Fan",
        description="CPU: 3.5GHz, 8-core AMD Zen 2, Storage: Custom 825GB SSD, RAM: 16GB GDDR6, Disc drive: 4K Blu-ray player, GPU: 10.3 teraflop RDNA 2 GPU PVT GoPdik",
        price=39.99,
        image="https://m.media-amazon.com/images/I/61H9Gtz4RWL._AC_UL320_.jpg"
      )
    electronics12=Product(
        type_id=2,
        name="High Power Bipolar Tower Speaker",
        description="SOUND THAT TRANSCENDS THE STATUS QUO – Features BDSS technology drivers on front & rear array – 8 SPEAKERS! - Front 1 tweeter & (2) 4.5 mid drivers - rear facing 1 tweeter & 4.5 mid driver for more accurate lifelike sound",
        price=999.99,
        image="https://m.media-amazon.com/images/I/618ZF9xZBiL._AC_UL320_.jpg"
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
        price=24.99,
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
        price=5.99,
        image="https://m.media-amazon.com/images/I/91vs-F-5r1S._AC_UY218_.jpg"

    )
    sports12 = Product(
        type_id=5,
        name="Inflatable Football Toss Target",
        description="Inflatable Football Toss Target Party Game, Sports Toys Gear and Gifts for Kids Boys Girls and Family",
        price=23.79,
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
        name="Solar Lights Outdoor",
        description="Auto Colorful Changing & Warm white】 Adjust to【FADE】mode,the light will automatically solar changer various colors,decorate your lawn,patio,courtyard, walkway, make them colorful and beautiful. Warm white will provide more lighter environment for you.",
        price=45.99,
        image="https://m.media-amazon.com/images/I/71YWMp1fXwL._AC_UY218_.jpg"

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
        name="NOCO Boost Plus GB40 1000 Amp 12-Volt",
        description="Start Dead Batteries - Safely jump start a dead battery in seconds with this compact, yet powerful, 1000-amp portable lithium car battery jump starter pack - up to 20 jump starts on a single charge - and rated for gasoline engines up to 6 liters and diesel engines up to 3 liters.",
        price=99.95,
        image="https://m.media-amazon.com/images/I/913+OdWA3NL._AC_UL320_.jpg"

    )
    automotive2 = Product(
        type_id=7,
        name="Car Trash Can, Pucuwu Car Garbage Can with Lid",
        description="G CAR TRASH CAN- Dimensions 11.8’’ H x 7.3’’W x 7.3’’D, our foldable trash can with a large compartment, 2 side pocket and a tissue holder. which can hold 2.7 Gallon.CONVENIENCE GARBAGE BAG- With opening rubber lid. can put in tissue paper, fruit peels and bottle etc. Prevents litter and odor spills.",
        price=8.49,
        image="https://m.media-amazon.com/images/I/71OFhMigEOL._AC_UL320_.jpg"

    )
    automotive3 = Product(
        type_id=7,
        name="BDK PolyPro Car Seat Covers Full Set in Charcoal on Black",
        description="PROTECTS AGAINST WEAR & TEAR – These are the perfect seat covers for your new car, or even a car that’s just new-to-you. Our car seat covers provide protection against daily wear and tear that occurs inside of your vehicle.",
        price=26.39,
        image="https://m.media-amazon.com/images/I/51Ntz25nijL._AC_UL320_.jpg"

    )
    automotive4 = Product(
        type_id=7,
        name="Phone Mount for Car Dashboard,Car Phone Holder",
        description="This upgraded version of the cell phone automobile cradle is made of the airliner PTFE materia and super suction cups. Say goodbye to substandard suction cups, limited compatibility and easy-to-break clamp arms, lengthy and tedious operations, and problems that hinder driving vision. All look similar,YFYYF always chooses the best materials.",
        price=19.99,
        image="https://m.media-amazon.com/images/I/71boW17cwGL._AC_UL320_.jpg"

    )
    automotive5 = Product(
        type_id=7,
        name="Car Jump Starter, SUNPOW 2000A Peak 20000mAh Lithium",
        description=":SUNPOW Car Jump Starter used High-speed polymer battery instead of normal starter. With the super 2000A peak and 20000mah capacity, it is easy to start a 12V vehicle (any gas engine or up to 8.5L diesel engine) , SUVs, trucks, vans, lawn-mower, snowmobile, motorcycle, yacht etc up to 35 times(charging only takes 4 to 5 hours).",
        price=99.99,
        image="https://m.media-amazon.com/images/I/817sadFMAvL._AC_UL320_.jpg"

    )
    automotive6 = Product(
        type_id=7,
        name="kyohans Car Seat Covers Full Set Fit for 2009-2019 Chevy Silverado Sierra, 5 Seats",
        description="Premium Quality Material - Adopting high quality leather and padded with sponge, our car seat covers make you feel soft and comfortable. The car seat cover offers ultra-high anti-scratch and wear-proof protection for your original seats, also no need to worry about dogs’claw marks. It is waterproof and can be easily wiped clean by wet towels.",
        price=169.99,
        image="https://m.media-amazon.com/images/I/71eHvxr4NzL._AC_UL320_.jpg"

    )
    automotive7 = Product(
        type_id=7,
        name="Wireless Backup Camera for Truck HD 1080P Waterproof Car Mini-RV Back Up Camera",
        description="【Easy and Time-Saving Installation】 backup camera for truck just 2 steps to install: ①The monitor be powered by the cigarette lighter outlet or Fuse box, ACC, Radio, Ignition switch. ②Connect the camera to continuous power source like tail light/ running light/license plate light for driving use or connect to backup light for reversing use only.Save your time and installation fee.",
        price=99.99,
        image="https://m.media-amazon.com/images/I/71tb-RcLRpL._AC_UL320_.jpg"

    )
    automotive8 = Product(
        type_id=7,
        name="2 Pcs Car Assist Handle for Elderly, 4 in 1 Portable Vehicle Support Handle with LED",
        description="HEAVY DUTY - Portable vehicle support handle is made of anti-rus and anti-corrosion high quality forged steel. Could carry 350lbs, ensure safer for getting in and out of the car.",
        price=21.88,
        image="https://m.media-amazon.com/images/I/61c2s6+aR7L._AC_UL320_.jpg"

    )
    automotive9 = Product(
        type_id=7,
        name="HULKMAN Alpha85 Jump Starter 2000 Amp 20000mAh Car Starter for up to 8.5L Gas",
        description="Easier & Safer Start Assurance: Product status is intuitively shown on a 3.3-inch smart screen, so you can start your car easily. Over 9 types of protection, free your worries of misoperation and sparks.Powerful Performer: 2000 Amps peak cranking amp can start the vehicles up to 8.5L Gas/6.0L Diesel",
        price=129.95,
        image="https://m.media-amazon.com/images/I/71qouQwYCQL._AC_UL320_.jpg"

    )
    automotive10 = Product(
        type_id=7,
        name="1800 Amp 12V/24V Car Jump Starter Power Station, Tyrell Chenergy Automotive Battery",
        description="Upgrade Powerful 12V/24V Jump Starter, All-new design with extremely jump starter for powerful engines start. 12V/24V Jump Starter is more powerful and stable than Ordinary 12V Jump starter. ",
        price=299.99,
        image="https://m.media-amazon.com/images/I/71TBv8zCQFL._AC_UL320_.jpg"

    )
    automotive11 = Product(
        type_id=7,
        name="Interior Car Lights Keepsmile Car Accessories Car Led Lights APP Control with Remote",
        description="DIY Modes: Car led lights has 16 million colors, or custom the colors and adjust the brightness through the smart app's color palette, Let you easily create your own car atmosphere.Perfect for decorating cars for Halloween and Christmas.",
        price=14.99,
        image="https://m.media-amazon.com/images/I/71bCyrGXmUL._AC_UL320_.jpg"

    )
    automotive12 = Product(
        type_id=7,
        name="Rear View Mirror Hanging Accessories",
        description="Car Decor Car Ornaments: This swing duck is swinging on your car,and the cute design makes your car which can well eliminate the driver's visual fatigue and increase safety.",
        price=11.99,
        image="https://m.media-amazon.com/images/I/61Rfc-aynGL._AC_UL320_.jpg"

    )








    babies1 = Product(
        type_id=8,
        name="Simple Joys by Carter's Unisex Babies' Short-Sleeve Bodysuit",
        description="100% Cotton Imported Snap closure Machine Wash Six short-sleeve bodysuits in baby-soft cotton featuring stripes, prints, and solids Expandable necklines",
        price=19.80,
        image="https://m.media-amazon.com/images/I/91oN-swVBVL._AC_UL320_.jpg"

    )
    babies2 = Product(
        type_id=8,
        name="Skip Hop Baby Bath Tub, 3-Stage Smart Sling Tub, Moby, Grey",
        description="Our cheerful whale-shaped Moby tub grows with baby through three stages and offers Smart Sling support. The sling locks into two ergonomic positions: higher for full-body support and lower for seated support",
        price=35.49,
        image="https://m.media-amazon.com/images/I/810shJy-REL._AC_UL320_.jpg"

    )
    babies3 = Product(
        type_id=8,
        name="Baby Einstein 4-in-1 Kickin' Tunes Music and Language Play Gym",
        description="The Baby Einstein 4-in-1 Kickin' Tunes gym entertains your baby with 4 modes: Laying, Sitting, Tummy Time and Take-Along; the included piano toy also ages up with your growing baby 70 plus sounds and activities and 25 plus minutes of music for endless entertainment; includes 7 detachable toys: crinkle medallion, triangle rattle, BPA-free textured music note, flash cards, self-discovery mirror, piano toy and tummy time pillow",
        price=44.98,
        image="https://m.media-amazon.com/images/I/81uQmTEJRAL._AC_UL320_.jpg"

    )
    babies4 = Product(
        type_id=8,
        name="Chicco Fit2 Infant & Toddler Car Seat - Cienna",
        description="2-Stage base (included) converts to provide extended leg room and more upright, spacious seating with adjustability for toddlers 9-24m – without taking up extra space in the vehicle!",
        price=319.99,
        image="https://m.media-amazon.com/images/I/81IwcPrpqoL._AC_UL320_.jpg"

    )
    babies5 = Product(
        type_id=8,
        name="Panasonic Baby Monitor with Camera and Audio",
        description="Long Range Baby Monitor Keeps a Close Eye on Baby: 3.5” LCD display for clear audio and video from up to 1500 ft away; rechargeable battery provides up to 13 hrs standby / 5 hrs use",
        price=149.99,
        image="https://m.media-amazon.com/images/I/61QEr7zi3OL._AC_UL320_.jpg"

    )
    babies6 = Product(
        type_id=8,
        name="Simple Joys by Carter's Unisex Toddlers and Babies' Holiday",
        description="For safety, sleepwear should be either flame resistant or snug-fitting. Our polyester/fleece sleepwear is flame resistant and free of chemical treatments Set of two gripper-foot pajamas featuring Christmas patterns and Santa applique Ankle-to-chin zipper with snap-over tab Trusted Carter’s quality, everyday low prices, and hassle-free tag less packaging",
        price=17.90,
        image="https://m.media-amazon.com/images/I/91r6L9rAViL._MCnd_AC_UL320_.jpg"

    )
    babies7 = Product(
        type_id=8,
        name="Simple Joys by Carter's Baby Boys' Short-Sleeve Bodysuit",
        description="Machine Wash Six short-sleeve bodysuits in baby-soft cotton featuring stripes, prints, and solids Expandable lapped necklines Nickel-free snaps on reinforced panels Trusted Carter’s quality, everyday low prices, and hassle-free packaging",
        price=19.69,
        image="https://m.media-amazon.com/images/I/91U4UktkVaL._AC_UL320_.jpg"

    )
    babies8 = Product(
        type_id=8,
        name="New and Improved Baby Brezza",
        description="Patented mixing technology automatically mixes formula and water to perfect consistency. Works with virtually all formula brands and all bottle brands/sizes.Clean your machine after every 4th bottle or when the clean funnel indicator light turns on so the mixing funnel is clear!",
        price=199.99,
        image="https://m.media-amazon.com/images/I/71Z2dCdw9HL._AC_UL320_.jpg"

    )
    babies9 = Product(
        type_id=8,
        name="Bigspinach Soft Pink Elephant",
        description="Soft pink colors make this one of the best girl gifts and infant toys. Perfect for new moms and dads, or parents with teething children. Easily cleaned with dish soap and water, and can even be used after boiling with water. (boiling 1 Minten) ",
        price=7.99,
        image="https://m.media-amazon.com/images/I/71EGd1ZFwOL._AC_UL320_.jpg"

    )
    babies10 = Product(
        type_id=8,
        name="'5'HD Split-Screen Baby Monitor",
        description="Split-Screen HD Display with 2 HD Cameras: Unlike most standard baby monitors, this HD video baby monitor is equipped with 2 HD cameras and SPLIT-SCREEN feature, allowing to see both cameras or babies side by side on the same screen. You are sure to always know what’s going on in your baby’s room!. Connect up to 4 cameras in different rooms.",
        price=145.89,
        image="https://m.media-amazon.com/images/I/51ZYjmhEGsL._AC_UL320_.jpg"

    )
    babies11 = Product(
        type_id=8,
        name="Baby Teething Toys for 0-6",
        description="Features: The balanced texture, not too soft or too hard, allows babies to enjoy the fun of chewing. Various shape bumps can better relieve the discomfort of baby's teething gums. Perfectly handle size for babies to grasp. Safe Material: 100% food grade silicone, Non-Toxic, BPA free and FDA stand.CPSC certified laboratory tested.babies can bite at ease. ",
        price=11.99,
        image="https://m.media-amazon.com/images/I/71tBXWlwC0L._AC_UL320_.jpg"

    )
    babies12 = Product(
        type_id=8,
        name="Plush Sensory Fabric Ball for Babies",
        description="Plush Creations brings you a new plush sensory baby ball. Our beautifully designed plush fabric sensory ball is designed with 8 different textures, patterns, and sounds. The fabric sections of the ball are sure to entice your little one for hours!",
        price=19.79,
        image="https://m.media-amazon.com/images/I/81VUMhSd7aL._AC_UL320_.jpg"

    )







    music1 = Product(
        type_id=9,
        name="The Eagles",
        description="The band's roots go back to their role as defining artists in the phenomenally popular Southern California rock scene of the '70s, a decade in which they delivered four consecutive #1 albums. Their momentous 2004 farewell tour filled stadiums around the world, and this film captures one of the most stellar events from that now-historic global sweep.",
        price=14.99,
        image="https://m.media-amazon.com/images/I/71YAWPIbV2L._AC_UY218_.jpg"

    )
    music2 = Product(
        type_id=9,
        name="Stevie Ray Vaughan - 1984-1989: Lonestar",
        description="The Full, Previously Un-Told Story Of Stevie Ray Vaughan's Glory Years, the period between the release of his debut album and his tragic death in a helicopter crash in 1989.",
        price=9.99,
        image="https://m.media-amazon.com/images/I/91zqPqNyVTL._AC_UY218_.jpg"

    )
    music3 = Product(
        type_id=9,
        name="Music for Yoga",
        description="Award-winning producer and instrumentalist Ben Leinbach has created yet another enchanting compilation with this soothing blend of live instrumentals, meditative chanting, and much more. Escape day-to-day stress while gentle music guides you into a world of imagination, creativity and wonder. Use for yoga, meditation, or just as an amazing ambient background to help you relax and focus.",
        price=11.12,
        image="https://m.media-amazon.com/images/I/71omhWbIYhL._AC_UY218_.jpg"

    )
    music4 = Product(
        type_id=9,
        name="Journey",
        description="On March 14, 2009, Journey returned to Arnel Pineda's homeland and introduced him as their newest lead singer to a crowd of nearly 30,000 at the SM Mall of Asia Concert Grounds. Features songs such as Don't Stop Believin', Stone In Love, When You Love A Woman and Separate Ways.",
        price=4.99,
        image="https://m.media-amazon.com/images/I/81cDNqWAV1L._AC_UY218_.jpg"

    )
    music5 = Product(
        type_id=9,
        name="Country: Portraits of an American Sound",
        description="A visual odyssey through the history of country music as told by legendary artists and the elite photographers who captured the evolving image of the country singer, from rhinestone cowboy to pot-smoking outlaw to stadium-filling megastar.",
        price=12.99,
        image="https://m.media-amazon.com/images/I/91JxfnMv4eL._AC_UY218_.jpg"

    )
    music6 = Product(
        type_id=9,
        name="George Fest",
        description="A live concert tribute to former Beatle George Harrison, held at the Fonda Theatre in Los Angeles on 28 September 2014. The 2014 concert coincided with the reissue of Harrison's Apple Records solo albums.",
        price=4.99,
        image="https://m.media-amazon.com/images/I/71SWTsGAFZL._AC_UY218_.jpg"

    )
    music7 = Product(
        type_id=9,
        name="Classical Piano for Sleep and Relaxation",
        description="A selection of relaxing piano music form the World's mist famous composers; Chopin, Haydn, Debussy, Brahms, Beethoven, Scriabin, Ravel and Schumann. Accompanied by a relaxing waterfall at Olympic National Park. Performed by Nico de Napoli, Edward Roser, Carlos Gardels, Vadim Chaimovich and Donald Betts.",
        price=5.99,
        image="https://m.media-amazon.com/images/I/71Gb4qTWcfL._AC_UY218_.jpg"

    )
    music8 = Product(
        type_id=9,
        name="Fleetwood Mac",
        description="Fleetwood Mac's hugely successful album 'Rumours' has sold over 40 million copies worldwide, was christened Album of the Year at the 1978 Grammy Awards and quickly earned its place in the pantheon of rock music history. This documentary details the making of 'Rumours' and includes exclusive interviews and a wonderful new acoustic edition of 'Never Going Back' from Lindsey Buckingham.",
        price=14.99,
        image="https://m.media-amazon.com/images/I/71PMkyR3AwL._AC_UY218_.jpg"

    )
    music9 = Product(
        type_id=9,
        name="Black Sabbath",
        description="The multi-platinum selling Paranoid is arguably Black Sabbath's finest album, not to mention one of the most seminal Heavy Metal albums of all time. This programme tells the story behind the writing, recording and success of this remarkable and groundbreaking Heavy Metal album.",
        price=4.99,
        image="https://m.media-amazon.com/images/I/71kcFPY358L._AC_UY218_.jpg"

    )
    music10 = Product(
        type_id=9,
        name="Symphony in Colorado",
        description="A selection of the world's favorite classical music from Beethoven, Mozart, Bach, Chopin, Vivaldi, Brahms and more. Accompanied by beautiful nature videos to enhance the senses. Performed by Martha Goldstein, Paul Pitman, Markus Staab, Nico de Napoli, Michel Rondeau, Aya Higuchi, Orchestra Gli Armonici, John Harrison, Us Navy Band, Carlos Gardels. Curated by Oumayma Naciri.",
        price=9.99,
        image="https://m.media-amazon.com/images/I/81-tERsHtdL._AC_UY218_.jpg"

    )
    music11 = Product(
        type_id=9,
        name="Eric Clapton",
        description="Eric Clapton is one of the most influential guitarists of all time. He ranked 2nd in Rolling Stone magazines list of the 100 Greatest Guitarists of All Time and 4th in Gibson's Top 50 Guitarists of All Time. In this documentary feature he is interviewed in depth with contributions from Keith Richards, John Mayall, The Yardbirds, Jack Bruce and many more. It is the definitive Clapton biography.",
        price=7.99,
        image="https://m.media-amazon.com/images/I/71NZFLJGT0L._AC_UY218_.jpg"

    )
    music12 = Product(
        type_id=9,
        name="Stevie Nicks",
        description="For over four decades Stevie Nicks has been responsible for composing some of the best loved and most joyous contemporary songs ever written, as this documentary film recounts. Featuring rare footage, archive and new interviews, plus contributions from those who have worked closely with Stevie such as good friend Keith Olsen, Rumours producer Ken Caillat, and Rick Vito, this will delight fans.",
        price=3.39,
        image="https://m.media-amazon.com/images/I/81WjI58RkZL._AC_UY218_.jpg"

    )








    movies1 = Product(
        type_id=10,
        name="Elf",
        description="Starring: Leon Redbone , Will Ferrell , James Caan and Ray Harryhausen Directed by: Jon Favreau",
        price=3.99,
        image="https://m.media-amazon.com/images/I/81Z+qD3jSoL._AC_UY218_.jpg"

    )

    movies2 = Product(
        type_id=10,
        name="Sandlot",
        description="The best baseball player in the neighborhood helps a new kid with his clumsy ball-handling.",
        price=15.19,
        image="https://m.media-amazon.com/images/I/31ryEwTFh4L._AC_UY218_.jpg"

    )
    movies3 = Product(
        type_id=10,
        name="Into The Woods",
        description="Starring: Meryl Streep , Emily Blunt , Anna Kendrick and James Corden Directed by: Rob Marshall",
        price=3.99,
        image="https://m.media-amazon.com/images/I/A13X4HqoVhL._AC_UY218_.jpg"

    )
    movies4 = Product(
        type_id=10,
        name="Monsters Inc.",
        description="The city of Monstropolis in the monster world is powered by energy from the screams of human children. At the Monsters, Inc., factory, skilled monsters employed as 'scarers' venture into the human world to scare children and harvest their screams, through doors that activate portals to children's bedroom closets",
        price=7.99,
        image="https://m.media-amazon.com/images/I/91MeaUr78gL._AC_UY218_.jpg"
        )
    movies5 = Product(
        type_id=10,
        name="Spiderman No Way Home",
        description="When Dr. Strange's spell to restore Spider-Man's identity goes awry, Peter is forced to overcome his greatest challenge yet.",
        price=21.29,
        image="https://m.media-amazon.com/images/I/91sKumJLa0L._AC_UY218_.jpg"

    )
    movies6 = Product(
        type_id=10,
        name="Home",
        description="In the year's hit comedy, a lovable misfit from another planet meets a girl named Tip. The two unlikely friends embark on the greatest journey of all time...the journey HOME.",
        price=3.99,
        image="https://m.media-amazon.com/images/I/91xU16apY1L._AC_UY218_.jpg"

    )
    movies7 = Product(
        type_id=10,
        name="The Right Stuff",
        description="This adaptation of the non-fiction novel by Tom Wolfe chronicles the first 15 years of America's space program. By focusing on the lives of the Mercury astronauts, including John Glenn (Ed Harris) and Alan Shepard (Scott Glenn), the film recounts the dangers and frustrations experienced by those involved with NASA's earliest achievements. It also depicts their family lives and the personal crises they endured during an era of great political turmoil and technological innovation.",
        price=9.89,
        image="https://m.media-amazon.com/images/I/91hqjqy9MvL._AC_UY218_.jpg"

    )
    movies8 = Product(
        type_id=10,
        name="Encanto",
        description="Walt Disney Animation Studios’ ENCANTO, with all-new songs by award-winner Lin-Manuel Miranda, tells the tale of the Madrigals, an extraordinary family living in a magical house in the Colombian mountains. But when Mirabel, the only ordinary family member, discovers the magic surrounding their home is in danger, she may be her family’s last hope.",
        price=15.89,
        image="https://m.media-amazon.com/images/I/91U-XSNsdoL._AC_UY218_.jpg"

    )
    movies9 = Product(
        type_id=10,
        name="The Martian",
        description="From legendary director Ridley Scott (Alien, Prometheus) comes a gripping tale of human strength and the will to survive, starring Matt Damon as an astronaut stranded on Mars.",
        price=3.99,
        image="https://m.media-amazon.com/images/I/A1j54D2jpxL._AC_UY218_.jpg"

    )
    movies10 = Product(
        type_id=10,
        name="Batman",
        description="A killer targets Gotham's elite sending Batman on an investigation. As evidence mounts, he must forge new relationships, unmask the culprit, and bring justice to corruption.",
        price=22.99,
        image="https://m.media-amazon.com/images/I/91WLf-Pd7ML._AC_UY218_.jpg"

    )
    movies11 = Product(
        type_id=10,
        name="Ant-Man",
        description="Armed with the astonishing ability to shrink in scale but increase in strength, master thief Scott Lang must embrace his inner hero and help his mentor, Dr. Hank Pym, to plan and pull off a heist that will save the world in Marvel Studios' Ant-Man.",
        price=12.99,
        image="https://m.media-amazon.com/images/I/81DlBh6ZaWL._AC_UY218_.jpg"

    )
    movies12 = Product(
        type_id=10,
        name="Shooter",
        description="A former Marine sniper is called back into duty but discovers he's the patsy in a conspiracy to assassinate the U.S. president in this action thriller starring Mark Wahlberg, Kate Mara and Danny Glover.",
        price=13.99,
        image="https://m.media-amazon.com/images/I/81OCGF9V70L._AC_UY218_.jpg"

    )








    health1 = Product(
        type_id=11,
        name="Vitamin D3 50,000 IU Weekly Supplement",
        description="Essential Sunshine Vitamin - Capture all the vitamin D benefits of the sun without harmful UV rays with ForestLeaf vitamin d3 50,000 iu supplements that pack a powerful immune-boosting punch. D3 vitamins deliver more potency than vitamin d supplements.",
        price=19.95,
        image="https://m.media-amazon.com/images/I/71TiS4bkmVS._AC_UY218_.jpg"

    )
    health2 = Product(
        type_id=11,
        name="Vitamin D3, B12 Gummies",
        description="𝗕𝗘𝗦𝗧 𝗩𝗜𝗧𝗔𝗠𝗜𝗡 𝗗𝟯+𝗕𝟭𝟮 𝗦𝗨𝗣𝗣𝗟𝗘𝗠𝗘𝗡𝗧 Dr. Danielle’s Delicious Vegan D3 + B12 Gummies are made from Vegan Lichen and bioactive B12 Methylcobalamin. Few food sources in nature offer vitamin D and most D3 on the market is sourced from lanolin—lamb’s wool fat. Dr Danielle’s gummies offer cellular support with a yummy, chewable gummy, naturally flavored with Strawberry.",
        price=18.95,
        image="https://m.media-amazon.com/images/I/71VbR5EVi5L._AC_UY218_.jpg"

    )
    health3 = Product(
        type_id=11,
        name="What the Health",
        description="An interepid filmmaker on a journey of discovery as he uncovers possibly the largest health secret of our time and the collusion between industry, government, pharmacuetical and health organizations keeping this information from us.",
        price=45.49,
        image="https://m.media-amazon.com/images/I/81xvuze72RL._AC_UY218_.jpg"

    )
    health4 = Product(
        type_id=11,
        name="The Perfect Human Diet",
        description="The Perfect Human Diet is the unprecedented global exploration for a solution to our epidemic of overweight, obesity, and diet-related diseases - the #1 killer in America. This film reveals for the first time, the authentic human diet. Film audiences finally can see what our species truly needs for optimal health and are given a practical template based on scientific facts.",
        price=18.99,
        image="https://m.media-amazon.com/images/I/81FWriZ3AtL._AC_UY218_.jpg"

    )
    health5 = Product(
        type_id=11,
        name="Probiotic Mouthwash",
        description="Riven - Probiotic Mouthwash | Cool Mint Anti-Cavity Dry Mouth Plaque Remover, Fight Bad Breath & Get Rid of Plaque & Gingivitis for Healthier Gum Tissue | Spearmint Flavor | Alcohol Free",
        price=19.99,
        image="https://m.media-amazon.com/images/I/71AQrE2mHJL._AC_UY218_.jpg"

    )
    health6 = Product(
        type_id=11,
        name="Nuts Snack Packs",
        description="Nuts Snack Packs / Mixed Nuts and Trail Mix Healthy Snacks Variety Pack for Adults - 28 Count Healthy Snacks Care Package",
        price=9.99,
        image="https://m.media-amazon.com/images/I/A1STYSC+87L._AC_UY218_.jpg"

    )
    health7 = Product(
        type_id=11,
        name="That Sugar Film",
        description="Damon Gameau embarks on an experiment to document the effects of a high sugar diet on a healthy body.",
        price=14.99,
        image="https://m.media-amazon.com/images/I/A19nOtrjeHL._AC_UY218_.jpg"

    )
    health8 = Product(
        type_id=11,
        name="Super Weight Loss Guided Self Hypnosis",
        description="This 'Super Weight Loss' Guided Self-Hypnosis video was designed to assist the listener in getting motivated to exercise, making healthy food choices, altering emotional eating habits and suppressing appetite. Written and narrated by Anna Thompson, MA, MHP, LMHC, Advanced Clinical Hypnotherapist. Life is short; live it well.",
        price=2.99,
        image="https://m.media-amazon.com/images/I/813Iqa+rOmL._AC_UY218_.jpg"

    )
    health9 = Product(
        type_id=11,
        name="Yoga for the rest of us",
        description="Peggy Cappy designed this workout to improve heart health as well as overall health. Centered around sun salutations, and featuring dynamic movements, relaxation poses, and breathing techniques, you’ll enjoy doing this at home",
        price=4.99,
        image="https://m.media-amazon.com/images/I/61-8nDFwJmL._AC_UY218_.jpg"

    )
    health10 = Product(
        type_id=11,
        name="Grow, Cook, Eat",
        description="Back for a third season of this very practical series aimed at helping people with little or no knowledge of growing their own food, but who like the idea of being able to grow something themselves. With plant-based diets becoming ever more popular, and consumers' increasing awareness of how far their food has traveled, this could not be arriving on our screens at a better time.",
        price=18.99,
        image="https://m.media-amazon.com/images/I/712VW7RcmDL._AC_UY218_.jpg"

    )
    health11 = Product(
        type_id=11,
        name="Bress 'n' Nyam",
        description="From Hot Buttermilk Biscuits and Sweet Potato Pie to Salmon Cakes on Pepper Rice and Gullah Fish Stew, Gullah Geechee food is an essential cuisine of American history. It is the culinary representation of the ocean, rivers, and rich fertile loam in and around the coastal South. From the Carolinas to Georgia and Florida, this is where descendants of enslaved Africans came together to make extraordinary food, speaking the African Creole language called Gullah Geechee.In this groundbreaking and beautiful cookbook, Matthew Raiford pays homage to this cuisine that nurtured his family for seven generations. In 2010, Raiford’s Nana handed over the deed to the family farm to him and his sister, and Raiford rose to the occasion, nurturing the farm that his great-great-great grandfather, a freed slave, purchased in 1874. In this collection of heritage and updated recipes, he traces a history of community and family brought together by food.100 color photographs",
        price=9.18,
        image="https://m.media-amazon.com/images/I/71YiCSS+1-L._AC_UY218_.jpg"

    )
    health12 = Product(
        type_id=11,
        name="Kitchen Cooking Utensils Set",
        description="Kitchen Cooking Utensils Set, 14 Non-Stick Silicone Cooking Kitchen Utensils Spatula Set with Holder, Wooden Handle Silicone Kitchen Gadgets Utensil Set for Nonstick Cookware(White)",
        price=56.89,
        image="https://m.media-amazon.com/images/I/61l6i45cidS._AC_UY218_.jpg"

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
