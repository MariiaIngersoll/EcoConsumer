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
        for _ in range(5):
            manufacturer = Manufacturer(
                name=fake.company(),
                description=fake.sentence()
            )
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