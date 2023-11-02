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
        product_data = [
            {
                "name": "All Purpose Cleaner - Lemon Chamomile",
                "description": "Seventh Generation All Purpose Cleaning Spray for cutting grease, grime and dirt everywhere in your home and beyond.",
                "ecoFriendlyFeatures": "Our spray cleaner bottles and sprayheads are 100% recyclable! The bottles (made with 100% recycled plastic) and sprayheads are made from #2 HDPE (high density polyethelene) plastic. You can recycle the bottles with the sprayhead still attached. ",
                "category": "Household Essentials and Cleaning Supplies",
                "image": "https://www.seventhgeneration.com/sites/default/files/styles/650x650_no_focal_point/public/2023-01/732913451630_PDP_Front-2500x2500-a596ffa6-efca-49a1-b16d-28f700ea7f16.png?itok=aCxGOLxq",
                "manufacturer_id": 1,
            },
            {
                "name": "100% Recycled Bathroom Tissue",
                "description": "Bath Tissue is one of life's little necessities. Ours not only does its job well, but helps you consider your impact on the environment.",
                "ecoFriendlyFeatures": "Made from 100% recycled paper.",
                "category": "Household Essentials and Cleaning Supplies",
                "image": "https://www.seventhgeneration.com/sites/default/files/styles/650x650_no_focal_point/public/product-images/pdp-front/732913137039_PDP_front.png?itok=gwg38lg6",
                "manufacturer_id": 1,
            },
            {
                "name": "Hand Wash - Lavender Flower & Mint",
                "description": "Hand soap made with plant-based ingredients, formulated with you and your family in mind.",
                "ecoFriendlyFeatures": "Made from real ingredients, without any dyes, or triclosan. Hand wash bottle made from 100% recyclable plastic.",
                "category": "Personal care",
                "image": "https://www.seventhgeneration.com/sites/default/files/styles/650x650_no_focal_point/public/product-images/pdp-front/732913229307_PDP_front.png?itok=uFs6RTTO",
                "manufacturer_id": 1,
            },  
            {
                "name": "SAL SUDS BIODEGRADABLE CLEANER",
                "description": "Dr. Bronner's Sal Suds Liquid Cleaner is not a soap but instead is a concentrated hard-surface all-purpose cleaner. Perfect for general household cleaning (dishes, floors, laundry, etc.), it cleans and rinses with exceptional power, yet it is mild and gentle on the skin.",
                "ecoFriendlyFeatures": " It is made with plant-based surfactants and natural fir needle and spruce essential oils (no cheap, harsh pine stump oil), without any synthetic dyes or fragrances.",
                "category": "Household Essentials and Cleaning Supplies",
                "image": "https://www.drbronner.com/cdn/shop/files/US-SalSuds-16oz_1800x1800.jpg?v=1688759894",
                "manufacturer_id": 2,
            },
            {
                "name": "PEPPERMINT - ALL-ONE TOOTHPASTE",
                "description": "Dr. Bronner’s All-One Peppermint Toothpaste has a bold peppermint flavor from the organic peppermint oil and the organic menthol crystals that stimulates mouth and gums with a cool, crisp sensation.",
                "ecoFriendlyFeatures": "Vegan & cruelty-free, with no artificial colors or flavors, carrageenan, preservatives, synthetic sweeteners or detergent foaming agents—none! ",
                "category": "Personal Care",
                "image": "https://www.drbronner.com/cdn/shop/products/US-Toothpaste-Tube-5oz-Peppermint-600_1800x1800.jpg?v=1612301187",
                "manufacturer_id": 2,
            },
            {
                "name": "WHOLE KERNEL - VIRGIN COCONUT OIL",
                "description": "Expeller-pressed from carefully dried coconuts, our Regenerative Organic Certified® Coconut Oil has a rich flavor and nutty aroma. ",
                "ecoFriendlyFeatures": "Our farmers in Sri Lanka are implementing regenerative organic prac­tices like mulching, composting and in­tercropping that enrich the soil, promote biodiversity, and seques­ter atmospheric carbon—building resil­ience in the face of a changing climate. ",
                "category": "Food and Beverages",
                "image": "https://www.drbronner.com/cdn/shop/products/US-CoconutOil-14oz-WholeKernel_1800x1800.jpg?v=1647407414",
                "manufacturer_id": 2,
            },
            {
                "name": "Aged Earl Grey",
                "description": "We age organic Assam with real bergamot–an aromatic Italian orange–for several weeks to make this bright, balanced black tea. Each sip brings a robust flavor with subtle citrus notes.",
                "ecoFriendlyFeatures": "Designed to reduce reliance on fossil fuels, our compostable* tea bag wrappers are made from renewable resources. We use sustainably grown FSC® certified paper lined with sugarcane-based Non-GMO PLA and metalized eucalyptus. These plant-based materials ensure complete disintegration and no eco-toxicity when they break down.",
                "category": "Food and Beverages",
                "image": "https://shop.numitea.com/img/product/numis-10170.png",
                "manufacturer_id": 3,
            },
            {
                "name": "Matcha Toasted Rice",
                "description": "A classic blend of genmaicha and matcha teas, Matcha Toasted Rice has a savory, nutty flavor. We blend sencha green tea with toasted rice to make Genmaicha, a traditional Japanese tea. The result is a smooth, rich brew with earthy depth and undertones of brightness.",
                "ecoFriendlyFeatures": "Designed to reduce reliance on fossil fuels, our compostable* tea bag wrappers are made from renewable resources. We use sustainably grown FSC® certified paper lined with sugarcane-based Non-GMO PLA and metalized eucalyptus. These plant-based materials ensure complete disintegration and no eco-toxicity when they break down.",
                "category": "Food and Beverages",
                "image": "https://shop.numitea.com/img/product/numis-10300.png",
                "manufacturer_id": 3,
            },
            {
                "name": "Women's Anytime Tee",
                "description": "An ultra smooth active tee designed to go with the flow, whether that’s a jog turned coffee run or vice versa. Natural materials like Tencel™ Lyocell and merino wool help keep you comfy while you’re on the move.",
                "ecoFriendlyFeatures": "Our Anytime Tee has a carbon footprint of 7.54 kg CO2e. As a carbon neutral business certified by Climate Neutral, we balance our emissions by funding high impact carbon projects.",
                "category": "Clothing and Footwear",
                "image": "https://cdn.allbirds.com/image/fetch/q_auto,f_auto/w_1302,f_auto,q_auto,b_rgb:f5f5f5/https://www.allbirds.com/cdn/shop/products/Anytime_Tee_Natural_White_F_0201_b00716db-8e81-4d7a-9c28-20b0dc653d36.png?v=1693262694",
                "manufacturer_id": 4,
            },
            {
                "name": "Women's Tree Runners",
                "description": "Our breathable, silky-smooth sneaker made with responsibly sourced eucalyptus tree fiber treads lightly in everything you do.",
                "ecoFriendlyFeatures": "These eco-friendly shoes are crafted with sustainable materials such as FSC-certified TENCEL™ Lyocell upper, SweetFoam® midsole made from sugarcane-based green EVA, and recycled plastic bottle laces.",
                "category": "Clothing and Footwear",
                "image": "https://cdn.allbirds.com/image/fetch/q_auto,f_auto/w_1302,f_auto,q_auto,b_rgb:f5f5f5/https://www.allbirds.com/cdn/shop/products/AB00FVM090_SHOE_45_GLOBAL_MENS_TREE_RUNNER_HAZY_INDIGO_BLIZZARD.png?v=1680308578",
                "manufacturer_id": 4,
            },
            {
                "name": "Women's Blanket Shirt",
                "description": "Crafted from a lofty organic cotton twill with buttons made from nuts, it's sturdy yet incredibly soft and breathable. Built for travel. Stands up to wrinkles and the elements.",
                "ecoFriendlyFeatures": "100% organic cotton. Organic cotton cuts out harmful synthetic chemicals used to grow conventional cotton, promoting safer working conditions for farmers and a healthier planet. Natural corozo buttons are made from tagua palm nuts gathered from the forest floor–a solid alternative to plastic.",
                "category": "Clothing and Footwear",
                "image": "https://www.outerknown.com/cdn/shop/products/2310030_Women_s_Blanket_Shirt_WFP_5_ed67aa15-43df-4e3e-87d7-eeecd64941f9_1440x.jpg?v=1680280631",
                "manufacturer_id": 5,
            },
            {
                "name": "Local Straight Fit Pants for Men",
                "description": "Sits at the waist with a slightly higher rise than our slim fit. Relaxed through the thigh and down the leg but holds its shape thanks to durable denim.",
                "ecoFriendlyFeatures": "95% organic cotton 4% recycled polyester 1% spandex. Organic cotton cuts out harmful synthetic chemicals used to grow conventional cotton, promoting safer working conditions for farmers and a healthier planet.",
                "category": "Clothing and Footwear",
                "image": "https://www.outerknown.com/cdn/shop/products/1630005_outerknown_LocalStraightFit_WGR_f_pdp_copy_1440x.jpg?v=1629693137",
                "manufacturer_id": 5,
            },
            {
                "name": "The Puffa Clog",
                "description": "Featuring a leather covered platform wedge and rubber outsole, the wedge is covered with padding—perfect for all-day wearability.",
                "ecoFriendlyFeatures": "The leather for this shoe is sourced from a Leather Working Group Gold-certified tannery. The Leather Working Group (LWG) Audit Standards provide transparency and accountability within the leather supply chain—covering energy and water usage, safe chemical practices, worker health and safety, and wastewater management.",
                "category": "Clothing and Footwear",
                "image": "https://media.everlane.com/images/c_fill,ar_4:5,q_auto,t_ecomm,f_auto/i/2ed0976b_529a/womens-puffa-clog-black",
                "manufacturer_id": 6,
            },
            {
                "name": "The Supima® Micro-Rib Long-Sleeve Crew",
                "description": "Made from an exceptionally soft blend of fine-ribbed Supima® cotton and stretchy elastane for added comfort, The Supima® Micro-Rib Long-Sleeve Crew features a classic crew neckline, long fitted sleeves, and a body-hugging fit throughout.",
                "ecoFriendlyFeatures": "Say hello to Supima®cotton. Everlane is transitioning its existing Pima basics to Supima® domestically sourced cotton with licensing programs giving us full supply chain visibility, right down to the farm level. Grown in the United States in just over 500 farms, Supima®cotton is distinguished by its extra-long fiber length, which gives it more durability and a softer hand feel, plus, it absorbs colors much better than conventional cotton. We routinely invest in new fabric innovations to ensure we’re reducing our impact on the planet. For more information, check out our sustainability initiatives.",
                "category": "Clothing and Footwear",
                "image": "https://media.everlane.com/images/c_fill,ar_4:5,q_auto,t_ecomm,f_auto/i/27f69164_9c80/womens-supima-rib-long-sleeve-crew-white",
                "manufacturer_id": 6,
            },
            {
                "name": "ORGANIC COTTON Core Singlet",
                "description": "A soft, stretchy, and curve-hugging staple. Made from soft organic cotton, this cropped camisole features adjustable straps and a scoop neckline.",
                "ecoFriendlyFeatures": "Organic Cotton is grown without harmful chemicals. This helps sustain the land it is grown on through crop rotations and a natural way of controlling pesticides, making it much lower-impact than regular cotton.",
                "category": "Clothing and Footwear",
                "image": "https://organicbasics.com/cdn/shop/products/dg-organic-basics_women_organic-cotton-stretch_singlet_black_studio_2_copy.jpg?v=1689069873",
                "manufacturer_id": 7,
            },
            {
                "name": "True French-Terry Sweatpants",
                "description": "Smooth on the outside with a soft loop texture on the inside, these french terry sweatpants are made from 100% organic cotton – for all the days you just want to be comfortable.",
                "ecoFriendlyFeatures": "Organic Cotton is grown without harmful chemicals. This helps sustain the land it is grown on through crop rotations and a natural way of controlling pesticides, making it much lower-impact than regular cotton.",
                "category": "Clothing and Footwear",
                "image": "https://organicbasics.com/cdn/shop/products/organic-basics_uni_sweat-pants_grey-melange_studio_1_de37ee97-fe1b-4303-a801-13eef9699d14.jpg?v=1678099264&width=1946",
                "manufacturer_id": 7,
            },
            {
                "name": "NO LIMITS CREAM BRONZER STICK",
                "description": "A creamy and insanely pigmented sculpting bronzer that helps naturally shape and define facial features with a second, skin-like finish.",
                "ecoFriendlyFeatures": "LYS™ is a proud supporter and participant of the sustainability movement, including the implementation of sustainably made product packaging and cartons. LYS proudly uses FSC-certified folding cartons and where possible packaging featuring glass and tubes using 30% Post-Consumer Recycled (PCR) materials to do our part in protecting the environment.",
                "category": "Beauty and Skincare",
                "image": "https://lysbeauty.com/cdn/shop/products/No-Limits-Cream-Bronzer-Stick-Ingredients-Slide-Deep_1296x.jpg?v=1654198635",
                "manufacturer_id": 8,
            },
            {
                "name": "SPEAK LOVE MOISTURE MATTE LIPSTICK",
                "description": "A moisture-rich satin matte lipstick with high-impact color payoff.",
                "ecoFriendlyFeatures": "LYS™ is a proud supporter and participant of the sustainability movement, including the implementation of sustainably made product packaging and cartons. LYS proudly uses FSC-certified folding cartons and where possible packaging featuring glass and tubes using 30% Post-Consumer Recycled (PCR) materials to do our part in protecting the environment.",
                "category": "Beauty and Skincare",
                "image": "https://lysbeauty.com/cdn/shop/products/SlimlineLipstick-CAPOFF-SILO-Sincere-300dpi_1296x.jpg?v=1696264248",
                "manufacturer_id": 8,
            },
            {
                "name": "LASH CONFIDENCE MASCARA",
                "description": "A triple-action precision mascara that instantly volumizes, lengthens, and curls the look of lashes.",
                "ecoFriendlyFeatures": "LYS™ is a proud supporter and participant of the sustainability movement, including the implementation of sustainably made product packaging and cartons. LYS proudly uses FSC-certified folding cartons and where possible packaging featuring glass and tubes using 30% Post-Consumer Recycled (PCR) materials to do our part in protecting the environment.",
                "category": "Beauty and Skincare",
                "image": "https://lysbeauty.com/cdn/shop/files/LashConfidence-Capsoff-SILO_300dpi_1296x.jpg?v=1685042486",
                "manufacturer_id": 8,
            },
            {
                "name": "SECURE SKIN GRIPPING SERUM PRIMER",
                "description": "A lightweight, serum primer that minimizes the look of pores and excess oil for a flawless base.",
                "ecoFriendlyFeatures": "LYS™ is a proud supporter and participant of the sustainability movement, including the implementation of sustainably made product packaging and cartons. LYS proudly uses FSC-certified folding cartons and where possible packaging featuring glass and tubes using 30% Post-Consumer Recycled (PCR) materials to do our part in protecting the environment.",
                "category": "Beauty and Skincare",
                "image": "https://lysbeauty.com/cdn/shop/products/2435352-Hero_1296x.jpg?v=1611622067",
                "manufacturer_id": 8,
            },
            {
                "name": "Bright Start Retinol Alternative Eye Cream",
                "description": "Bright Start is clinically proven to refresh and revive tired eyes instantly—and reduce dark circles, puffiness, fine lines, and wrinkles over time. Light-reflecting pearl illuminates, and the cooling ceramic tip doubles as a massage tool for a moment of calm as you begin your day.",
                "ecoFriendlyFeatures": "We strive towards more sustainable packaging through the use of recycled aluminum, glass components, and responsibly sourced paper. But it isn’t enough—that’s only the beginning of the product’s lifecycle. We believe end-of-life is far more important, to ensure products don’t end up in a landfill.",
                "category": "Beauty and Skincare",
                "image": "https://cdn.shopify.com/s/files/1/0127/2332/files/IMG-3401.jpg?v=1695324158&width=640&format=webp",
                "manufacturer_id": 9,
            },
            {
                "name": "Multi-Stick",
                "description": "A buildable wash of color for cheeks and lips—now with 12 swipe-and-go shades.",
                "ecoFriendlyFeatures": "We strive towards more sustainable packaging through the use of recycled aluminum, glass components, and responsibly sourced paper. But it isn’t enough—that’s only the beginning of the product’s lifecycle. We believe end-of-life is far more important, to ensure products don’t end up in a landfill.",
                "category": "Beauty and Skincare",
                "image": "https://cdn.shopify.com/s/files/1/0127/2332/products/Multi-Stick_Open_Dreamer-White.jpg?v=1649203303&width=640&format=webp",
                "manufacturer_id": 9,
            },
            {
                "name": "HYDROGEL CREAM",
                "description": "This award-winning, bestselling, lightweight, moisture-release water cream refreshes and cools on application as it leaves a dewy finish. Infused with Jojoba + Squalane to help hydrate and soothe thirst, while 2 sizes of Hyaluronic Acid help soften and firm skin (reducing the appearance of fine lines). Drink up, babes.",
                "ecoFriendlyFeatures": "Jar, disc and cap are made from 30% post consumer recycled plastic Our sustainable cartons are environmentally friendly, FSC-certified, and made from 100% recycled, PCW (pre/post-consumer waste) materials.",
                "category": "Beauty and Skincare",
                "image": "https://www.honest.com/dw/image/v2/BDBW_PRD/on/demandware.static/-/Sites-HC-master-catalog/default/dw2151f742/images/large/Hydrogel-Cream/Hydrogel-2023-Refresh/hydrogel_hero.jpg?sw=2000&sh=2000&sm=fit",
                "manufacturer_id": 10,
            },
            {
                "name": "PRIME + PERFECT MASK",
                "description": "This antioxidant-rich, moisturizing mask is the morning smoothie your complexion craves. Black Currant Extract + Ice Wine helps make skin appear firmer and more supple (yas), while Vitamin E + Superfruits nourish and replenish dull, tired skin. PS. We like to apply it and have our coffee while it does its thing.",
                "ecoFriendlyFeatures": "Tube is made from aluminum. Cap is made from 100% virgin polypropylene. Our sustainable cartons are environmentally-friendly, FSC-certified, and made from 100% recycled, PCW (pre/post-consumer waste) materials.",
                "category": "Beauty and Skincare",
                "image": "https://www.honest.com/dw/image/v2/BDBW_PRD/on/demandware.static/-/Sites-HC-master-catalog/default/dwc986b767/images/large/Prime-Perfect-Mask/BeautyRestagePrimePerfect/primaryonswipe.jpg?sw=2000&sh=2000&sm=fit",
                "manufacturer_id": 10,
            },
            {
                "name": "SHAMPOO + BODY WASH, SENSITIVE",
                "description": "2-in-1 shampoo + body wash leaves skin + hair soft and clean. Tear-free and gentle for babe, but great for the whole fam. Made with Aloe + Chamomile Extract. Designed for all skin types, and gentle enough for baby.",
                "ecoFriendlyFeatures": "MADE WITHOUT: Parabens, Phthalates, Dyes, Synthetic Fragrances, Formaldehyde Donors, SLS/SLES. It is recyclable, promoting environmental responsibility.",
                "category": "Personal care",
                "image": "https://www.honest.com/dw/image/v2/BDBW_PRD/on/demandware.static/-/Sites-HC-master-catalog/default/dwf154db02/images/large/Shampoo-and-Body-Wash/SBW-10oz-Restage22/Sensitive-Hero.jpg?sw=2000&sh=2000&sm=fit",
                "manufacturer_id": 10,
            },
            {
                "name": "Organic Pumpkin Spice Latte Powder",
                "description": "Pumpkin Spice Latte made with real pumpkin. Blume swapped the syrups, dairy, and caffeine for whole superfood ingredients, so you can sip back with a barista-worthy PSL you can feel good drinking. Combining organic pumpkin and Canadian maple for a warm cup of velvety goodness. ",
                "ecoFriendlyFeatures": "Deliciously vegan and organic perfect for eco-conscious consumers. Support a women-owned business while enjoying this clean, plastic-neutral product.",
                "category": "Food and Beverages",
                "image": "https://images.grove.co/upload/f_auto,fl_progressive,h_1160,ar_1:1,c_pad,b_white/v1698080274/tv7mmk84hqzwse2qg4vx.png",
                "manufacturer_id": 11,
            },
            {
                "name": "GROVE CO. Reusable Cleaning Glass Spray Bottle - Slide & Snap",
                "description": "A Reusable Cleaning Glass Spray Bottle - Slide & Snap with a unique silicone sleeve that allows you to label what’s inside your bottle for customizing your cleaning routine. Plastic-free and crafted to be sustainably powerful for a healthy home and planet.",
                "ecoFriendlyFeatures": "It’s designed with Grove Co. cleaning concentrates in mind, and it’s sustainably crafted from responsible, lead-free, partially recycled materials for the long run to help you clean and care for your home without the plastic waste.",
                "category": "Household Essentials and Cleaning Supplies",
                "image": "https://images.grove.co/upload/f_auto,fl_progressive,h_1160,ar_1:1,c_pad,b_white/v1683946201/op1olky00wz3viowgump.jpg",
                "manufacturer_id": 11,
            },
            {
                "name": "Swedish Dishcloths - Lemons",
                "description": "A reusable sponge cloth to clean up spills and messes, providing a more eco-friendly alternative to paper towels and sponges.",
                "ecoFriendlyFeatures": "Made of cellulose and cotton, our reusable dish cloths eliminate single-use consumption from your home, providing a more eco-friendly solution for household cleaning.",
                "category": "Household Essentials and Cleaning Supplies",
                "image": "https://images.grove.co/upload/f_auto,fl_progressive,h_1160,ar_1:1,c_pad,b_white/v1607368259/is4abjytzmo1eysazvj2.jpg",
                "manufacturer_id": 11,
            },
            {
                "name": "Almond Shower Oil Refill",
                "description": "Gently cleanse and soften skin with this waste-reducing refillable.  Cleanse as you soften and comfort skin with this sweet almond oil-infused formula. ",
                "ecoFriendlyFeatures": "Now packaged in a bottle crafted with 100% recycled second-life plastic, and is recyclable!",
                "category": "Personal Care",
                "image": "https://imagena.loccitane.com/dw/image/v2/BDQL_PRD/on/demandware.static/-/Sites-occ_master/default/dwdfb1c94e/US/29RH500A23.png?sw=500&sh=500",
                "manufacturer_id": 12,
            },
            {
                "name": "Laundry Essentials Kit",
                "description": "Tackle laundry day and ditch the plastic-wrapped detergent pods with our full lineup of plastic-free laundry essentials. Get a powerful clean with our plastic-free Laundry Detergent Tablets, a boost of stain-removing power with our Oxi Laundry Booster, and reduce wrinkles, static, and dry time with our Dryer Balls.",
                "ecoFriendlyFeatures": "100% plastic-free. Clean ingredients. Concentrated clean.",
                "category": "Household Essentials and Cleaning Supplies",
                "image": "https://cdn.sanity.io/images/d864s8gp/production/f9e961495fdcfad363a2557e9a43df25d2b87d99-1790x1790.jpg?w=900&q=100&fit=clip&auto=format&dpr=2",
                "manufacturer_id": 13,
            },
            {
                "name": "Clean Skin Duo",
                "description": "Turn your self care into planet care with a clean routine that’s made for you and the planet. Clean up from tip to toe with ingredients and packaging you can feel good about. Buy your bottles once and refill them forever with refill powder packs. This kit makes 3 full bottles of Body Wash (1 Waterlily Dew, 1 Coconut Milk, 1 Sandalwood Sage) and 1 full bottle of Facial Cleanser (Fragrance-Free).",
                "ecoFriendlyFeatures": "Using only natural and Made Safe certified ingredients like oat, Vitamin E, and kaolin clay, our personal care products are formulated to be gentle and non-irritating. No ingredients you can’t pronounce, no harsh irritants and no single-use plastic.",
                "category": "Personal Care",
                "image": "https://cdn.sanity.io/images/d864s8gp/production/490b765d3548199892753f9a160d3a1208b2216c-1790x1790.jpg?w=900&q=100&fit=clip&auto=format&dpr=2",
                "manufacturer_id": 13,
            },
            {
                "name": "Hand Soap Refills",
                "description": "Reduce, reuse, refill with our bestselling hand soap scents. Take your pick from three classic scents or opt for our limited edition packs and say goodbye to single-use plastic. Just fill with water, drop in a tablet and voila! hydrating, foamy goodness at your fingertips.",
                "ecoFriendlyFeatures": "Made with plant-based and planet-friendly ingredients. ",
                "category": "Personal Care",
                "image": "https://cdn.sanity.io/images/d864s8gp/production/b09ff565fe9b1ccbb5047f2873774b7b0ce61017-1790x1790.jpg?w=900&q=100&fit=clip&auto=format&dpr=2",
                "manufacturer_id": 13,
            },
        ]

        for data in product_data:
            product = Product(**data)
            products.append(product)

        db.session.add_all(products)


        # Create Reviews
        review_content_list = [
            "I love how effective this cleaner is in my kitchen, but I also appreciate the eco-friendly packaging. It's a winner!",
            "I found the lemon chamomile scent to be overpowering, and the cleaner didn't perform as well as I expected.",
            "This is a fantastic all-purpose cleaner. The fact that it's eco-friendly is a huge bonus.",
            "High-quality bathroom tissue that's gentle on the environment. It's a staple in our household!!!!",
            "Would not recommend this product. Terrible quality.",
            "I'm a fan of this hand wash! It's gentle on my hands, and the fact that the bottle is recyclable makes me feel good about using it.",
            "The scent of lavender and mint was too strong for my liking. I found it overpowering.",
            "The peppermint flavor is refreshing, and I love that this toothpaste is cruelty-free and doesn't contain artificial additives.",
            "The texture of this toothpaste is gritty, which I found uncomfortable to use.",
            "I absolutely love this tee! It's not only comfortable but also eco-friendly. I appreciate that the brand is carbon neutral and supports high-impact carbon projects.",
            "The tee is comfortable, but the sizing is a bit off. It runs larger than expected.",
            "These sneakers are a game-changer. They're super comfortable, and the sustainable materials used, like eucalyptus tree fiber and sugarcane-based green EVA, make me feel good about my choice.",
            "I had high hopes for these sneakers, but they didn't provide the support I needed for running.",
            "I love the versatility of this 2-in-1 shampoo and body wash. It's gentle and tear-free, making it perfect for my little one, but the whole family enjoys using it. The absence of harmful chemicals like parabens, phthalates, and synthetic fragrances is a huge plus.",
            "This product is fantastic for sensitive skin. It leaves hair and skin soft and clean without any irritation. I appreciate that it's recyclable, supporting environmental responsibility.",
            "While this shampoo + body wash is great for sensitive skin, I found the scent to be too mild. I prefer products with a more refreshing fragrance.",
            "I love this organic pumpkin spice latte powder! It's the perfect way to enjoy the cozy flavors of fall. I appreciate that it's made with real pumpkin and Canadian maple, making it a healthier choice for my morning pick-me-up. Plus, it's vegan and supports a women-owned business",
            "This pumpkin spice latte powder is a game-changer. I can enjoy the classic PSL flavors without the guilt, thanks to its organic and vegan ingredients. It's the perfect blend of warmth and velvety goodness",
            "While I appreciate the eco-friendly aspects of this product, I found the taste to be a bit lacking. It's not as rich and flavorful as I expected.",

        ]

        user1 = User.query.filter(User.id == 1).first()
        user2 = User.query.filter(User.id == 2).first()
        user3 = User.query.filter(User.id == 3).first()
        user4 = User.query.filter(User.id == 4).first()
        user5 = User.query.filter(User.id == 5).first()
        user6 = User.query.filter(User.id == 6).first()
        user7 = User.query.filter(User.id == 7).first()
        user8 = User.query.filter(User.id == 8).first()
        user9 = User.query.filter(User.id == 9).first()
        user10 = User.query.filter(User.id == 10).first()

        product1 = Product.query.filter(Product.id == 1).first()
        product2 = Product.query.filter(Product.id == 2).first()
        product3 = Product.query.filter(Product.id == 3).first()
        product4 = Product.query.filter(Product.id == 4).first()
        product5 = Product.query.filter(Product.id == 5).first()
        product6 = Product.query.filter(Product.id == 6).first()
        product7 = Product.query.filter(Product.id == 7).first()
        product8 = Product.query.filter(Product.id == 8).first()
        product9 = Product.query.filter(Product.id == 9).first()
        product10 = Product.query.filter(Product.id == 10).first()
        product11 = Product.query.filter(Product.id == 11).first()
        product12 = Product.query.filter(Product.id ==12).first()
        product13 = Product.query.filter(Product.id == 13).first()
        product25 = Product.query.filter(Product.id == 25).first()
        product26 = Product.query.filter(Product.id == 26).first()



        review = Review(
            rating=5,
            content=review_content_list[0],
            product_id=product1.id,
        )

        reviewUser2 = Review(
            rating=3,
            content=review_content_list[1],
            product_id=product1.id,
        )

        reviewUser7 = Review(
            rating=4,
            content=review_content_list[2],
            product_id=product1.id,
        )

        reviewBathroomTissue = Review(
            rating=5,
            content=review_content_list[3],
            product_id=product2.id,
        )

        reviewBathroomTissue2 = Review(
            rating=1,
            content=review_content_list[4],
            product_id=product2.id,
        )

        reviewHandWash1 = Review(
            rating = 5,
            content=review_content_list[5],
            product_id=product3.id,
        )

        reviewHandWash2 = Review(
            rating = 1,
            content=review_content_list[6],
            product_id=product3.id,
        )

        reviewToothpase1 = Review(
            rating = 5,
            content=review_content_list[7],
            product_id=product5.id,
        )

        reviewToothpase2 = Review(
            rating = 2,
            content=review_content_list[8],
            product_id=product5.id,
        )

        reviewAnytimeTea1 = Review(
            rating = 5,
            content=review_content_list[9],
            product_id=product9.id,
        )

        reviewAnytimeTea2 = Review(
            rating = 3,
            content=review_content_list[10],
            product_id=product9.id,
        )

        reviewRunners1 = Review(
            rating = 5,
            content=review_content_list[11],
            product_id=product10.id,
        )

        reviewRunners2 = Review(
            rating = 4,
            content=review_content_list[12],
            product_id=product10.id,
        )

        reviewSensetiveShampoo1 = Review(
            rating = 4,
            content=review_content_list[13],
            product_id=product25.id,
        )

        reviewSensetiveShampoo2 = Review(
            rating = 4,
            content=review_content_list[14],
            product_id=product25.id,
        )

        reviewSensetiveShampoo3 = Review(
            rating = 2,
            content=review_content_list[15],
            product_id=product25.id,
        )
        
        reviewPumpkinLatte1 = Review(
            rating = 5,
            content=review_content_list[16],
            product_id=product26.id,
        )

        reviewPumpkinLatte2 = Review(
            rating = 2,
            content=review_content_list[17],
            product_id=product26.id,
        )
        reviewPumpkinLatte3 = Review(
            rating = 2,
            content=review_content_list[18],
            product_id=product26.id,
        )

        
        

        user1.reviews.extend([review, reviewBathroomTissue, reviewAnytimeTea2])
        user2.reviews.extend([reviewAnytimeTea1, reviewUser2, reviewHandWash2, reviewSensetiveShampoo3])
        user7.reviews.extend([reviewUser7, reviewBathroomTissue2,reviewPumpkinLatte1])
        user3.reviews.extend([reviewHandWash1,reviewToothpase2, reviewSensetiveShampoo2])
        user4.reviews.extend([reviewToothpase1,reviewSensetiveShampoo1,reviewPumpkinLatte2])
        user6.reviews.extend([reviewRunners1,reviewPumpkinLatte3])
        user5.reviews.append(reviewRunners2)
        db.session.commit()