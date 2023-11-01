from random import choice as rc
from faker import Faker

from app import app
from config import db, bcrypt
from models import User, Review, Manufacturer, Product

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Deleting all records...")
        User.query.delete()
        Review.query.delete()
        Manufacturer.query.delete()
        Product.query.delete()

        users = []
        products = []
        manufacturers = []
        reviews = []

        # Create Users
        for _ in range(10):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                image=fake.image_url(),
                _password_hash=bcrypt.generate_password_hash('password').decode('utf-8')
            )
            users.append(user)

        db.session.add_all(users)

        # Create Manufacturers
        manufacturer_data = [
            {
                "name": "Seventh Generation",
                "description": "Seventh Generation, established in 1988, is dedicated to eco-friendliness. Their mission is to create a sustainable, equitable world for generations to come. They tackle environmental concerns, particularly in packaging, by using recycled materials and designing recyclable packaging for their plant-based products. Their aim is to have all their products and packaging use biobased or post-consumer recycled materials. Moreover, they aspire to become a zero-waste company by 2025. Seventh Generation actively engages in environmental advocacy and community initiatives, supporting the Sierra Club's Ready For 100 campaign and providing grants to nonprofit organizations through the Seventh Generation Foundation. Their commitment extends beyond product delivery, ensuring a lasting positive impact.",
                "image": "https://www.seventhgeneration.com/sites/default/files/legacy/styles/1600w/public/2019-12/sevgenlaundry12784720x48072rgb.jpg",
            },
            {
                "name": "Dr. Bronner’s",
                "description": 'Dr. Bronner’s All-One organic soaps and personal care products are renowned for their eco-friendliness. Guided by six "Cosmic Principles," including "treat the earth like home" and "be fair to suppliers," the company is committed to doing right by the environment. Their organic and fair trade ingredients are certified by leading sustainable organizations. In a bid to reduce environmental impact, all of their plastic bottles are made from 100% post-consumer recycled materials, conserving resources and minimizing landfill waste. Dr. Bronner’s, based in California, also fosters equitable supply chains through fair trade practices. These principles encompass fair prices for farmers, environmental stability, and a firm stance against forced or child labor. Remarkably, the company estimates that their fair trade projects have directly benefited around 10,000 people worldwide, with an additional 10,000 enjoying indirect benefits. Dr. Bronner’s stands as a shining example of a business dedicated to sustainability and social responsibility.',
                "image": "https://rivergear.com/wp-content/uploads/2010/11/Dr-Bronners-3-600x351.jpg",
            },
            {
                "name": "Numi Organic Tea",
                "description": "Numi Organic Tea, headquartered in Oakland, is a remarkable quadruple-bottom line company, integrating people, planet, profit, and purpose into their business model. Their teas, made with ethically sourced organic ingredients, come in sustainable packaging. Their mission includes supporting local and global initiatives through the Numi Foundation, and they've pledged to achieve carbon neutrality by 2023, focusing on emission reduction, renewable energy, and emissions offsetting. Numi Organic Tea stands as a prime example of a company dedicated to sustainability and social responsibility.",
                "image": "https://i.ebayimg.com/images/g/V~4AAOSwbtdkd5ma/s-l1600.jpg",
            },
            {
                "name": "Allbirds",
                "description": "Allbirds, a carbon-neutral business, aims for more than just neutrality. They're committed to reducing their carbon footprint to zero. Their transparency in sustainability is evident through their website, where they share their journey and environmental innovations. As a Certified B Corp, they label their products with associated emissions, making conscious consumption easier. In April 2021, Allbirds open-sourced their carbon footprint tool for the benefit of other companies and consumers.",
                "image": "https://www.allbirds.com/cdn/shop/t/1865/assets/allbirds-logo-fb.jpg?v=92553177456616239951698773342",
            },
            {
                "name": "Outerknown",
                "description": "Outerknown, founded by world champion surfer Kelly Slater in 2015, offers high-quality, sustainable fashion designed to endure various conditions, even in the water. Their clothing is crafted from eco-conscious materials like organic cotton, hemp fibers, and recycled polyester from plastic bottles, ensuring long-lasting durability. This brand caters to adventure and nature lovers with a collection of sweatshirts, jackets, t-shirts, hoodies, shirts, and shorts. Their commitment extends to sustainability, prioritizing both the planet and people.",
                "image": "https://www.outerknown.com/cdn/shop/files/giftcard_2020_1400x1400_02_1440x_ff3b25e5-9a00-45ca-83dc-70a852c4a51c_1440x.png?v=1682538513",
            },
            {
                "name": "Everlane",
                "description": "Everlane, the American clothing retailer headquartered in San Francisco, California, is not only known for its transparent pricing but also for its strong dedication to eco-conscious practices. Their mission goes beyond offering a minimalist, modern aesthetic and quality basics. Everlane's focus on transparency extends to their commitment to ethical sourcing and eco-friendly principles. They meticulously select factories worldwide, often the very ones used by top designer labels, to ensure ethical production practices and maintain the integrity of their supply chain. Additionally, they share the production costs and the origin stories behind each piece of clothing with their customers, fostering transparency in the fashion sector. One of their noteworthy products, Tread by Everlane, is available in a range of seven appealing colors. Everlane's mission revolves around bringing transparency to the fashion industry, and their efforts encompass not only transparent pricing but also eco-conscious materials and practices, making them a brand that stands out in ethical and sustainable fashion.",
                "image": "https://www.thelifestyle-files.com/wp-content/uploads/2020/08/Is-everlane-ethical.jpg",
            },
            {
                "name": "Organic Basics",
                "description": "Organic Basics, based in Copenhagen, is committed to providing comfort and sustainability. They create Earth- and people-friendly basics using recycled, recyclable, organic, and plant-based materials. Their ethical production methods and collaborations ensure minimal environmental impact. They focus on producing essentials that are hard to find second-hand while constantly evolving their designs based on feedback. Organic Basics aims to reshape the fashion industry, advocating for sustainability and a wardrobe that's kind to the planet and its people. They actively offset carbon emissions, support sustainable projects, and work with like-minded partners to create a better future.",
                "image": "https://thehub-io.imgix.net/files/s3/20230908133145-e2c671e8f314f2628c3bd571155b4276.png?fit=crop&w=300&h=300&auto=format&q=60",
            },
            {
                "name": "LYS Beauty",
                "description": "LYS Beauty is on a mission to disrupt the beauty industry while prioritizing eco-friendliness. Their commitment to clean, sustainable formulas and inclusive ranges sets them apart. By creating thoughtfully formulated makeup and skincare solutions, LYS Beauty not only addresses various skin concerns but also values eco-conscious practices. Their dedication to being environmentally responsible adds an extra layer to their mission of empowering and boosting confidence, so you can Love Your Self while loving the planet.",
                "image": "https://cdn.shopify.com/s/files/1/0515/9344/5541/files/lys-logo-checkout.png?height=628&pad_color=fff5ec&v=1615322941&width=1200",
            },
            {
                "name": "ILIA Beauty",
                "description": "ILIA Beauty is at the intersection of nature and science, proving that not all natural ingredients are skin-friendly, and not all synthetics are harmful. Their philosophy of clean beauty combines consciously selected ingredients without compromises. Since their inception in 2011, they've been dedicated to pushing the boundaries of innovation in the industry. In addition to ingredient choices, ILIA Beauty focuses on sustainable packaging. They utilize recycled aluminum, glass components, and responsibly sourced paper. However, they understand that it's not just about the beginning but also the end of a product's lifecycle, ensuring their products have a sustainable afterlife and don't contribute to landfills.",
                "image": "https://images.ctfassets.net/c9o4jciad99f/4m6LdUFpIUoLFEFgQzn1r1/895ea07308c8aa1a5b7c2cd3601d2898/image001.png?w=768",
            },
            {
                "name": "Honest",
                "description": "The Honest Company is on a mission to make a positive change in the world, one product at a time. They are driven by meaningful transparency and thoughtful design. Founded with the purpose of creating safe and effective products for families, The Honest Standard represents their guiding principles and values applied to innovation and development. This standard shapes the way they introduce new products, and it's a commitment that continues to evolve. The company is committed to eco-friendliness and responsible practices, from avoiding animal testing and not using over 5,000 chemicals to utilizing plant-based ingredients and sustainable packaging solutions. They strive to bring safe and effective products that you can trust and that contribute to a better, more environmentally friendly world.",
                "image": "https://www.honest.com/dw/image/v2/BDBW_PRD/on/demandware.static/-/Library-Sites-HC-content/default/dwcd24798a/blog/honestlogo21.jpg?sw=1290",
            },
            {
                "name": "Grove Collaborative",
                "description": "Grove Collaborative offers an extensive range of over 300 non-toxic household products, including cleaning items from sustainable brands. These products are ethically produced, cruelty-free, and safe for your health. They exclusively feature plant-based formulas with essential oils and botanical-based ingredients, with full disclosure on their website. From floor cleaners to dish soaps, Grove Collaborative provides everything for a clean home. They even offer eco-friendly toilet brushes, sponges, dishcloths, and 100% recycled plastic trash bags. As a B Corp certified company, they prioritize social and environmental responsibility, and every shipment is carbon-neutral, underlining their commitment to a greener, healthier planet.",
                "image": "https://www.playbook.media/wp-content/uploads/2019/08/logo-grove-collaborative.png",
            },
            {
                "name": "L’OCCITANE",
                "description": "For more than a decade, L'OCCITANE has been dedicated to sustainability, actively working to reduce waste and minimize their carbon footprint. They embrace eco-refills and use bottles made from 100% recycled plastic as part of their commitment to a greener and more environmentally responsible approach.",
                "image": "https://cdn.freebiesupply.com/logos/large/2x/loccitane-1-logo-png-transparent.png",
            },
            {
                "name": "Blueland",
                "description": "Blueland's journey towards reducing single-use plastic began with a new mom's realization of the environmental impact of plastic waste on our water supply and food. Fueled by the need for eco-friendly household products, Blueland was born. Their mission is straightforward: provide innovative, reusable packaging for convenient, effective, and affordable eco-products, making it easy for everyone to be environmentally conscious. Blueland's CEO and Co-Founder, Sarah Paiji Yoo, leads the charge in addressing the plastic problem. Single-use plastic, designed to last indefinitely, is too often discarded after one use. Much of it finds its way into our oceans, leading to toxic consequences for all. Microplastics have infiltrated our food and water sources, with the average person ingesting a credit card's worth of plastic each week. This environmental crisis extends to our wildlife, as plastic has been discovered in marine turtles, whales, seals, and seabird species, further highlighting the urgency of addressing the plastic problem. Blueland is committed to cleaning up the planet and invites you to join their mission.",
                "image": "https://madesafe.org/cdn/shop/products/BluelandFacialCleanserMADESAFE_533x.png?v=1665679163",
            },
        ]

        for data in manufacturer_data:
            manufacturer = Manufacturer(**data)
            manufacturers.append(manufacturer)

        db.session.add_all(manufacturers)

        # Create Products
        for _ in range(20):
            product = Product(
                name=fake.word(),
                description=fake.sentence(),
                ecoFriendlyFeatures=fake.word(),
                category=fake.word(),
                manufacturer=rc(manufacturers)
            )
            products.append(product)

        db.session.add_all(products)

        # Create Reviews
        for _ in range(30):
            review = Review(
                rating=rc([1, 2, 3, 4, 5]),
                content=fake.paragraph(),
                user=rc(users),
                product=rc(products)
            )
            reviews.append(review)

        db.session.add_all(reviews)

        db.session.commit()