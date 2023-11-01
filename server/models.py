from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from config import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    content = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='reviews')

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship('Product', back_populates='reviews')

    def __repr__(self):
        return f'<Review content: {self.content}>'
    
    serialize_rules = (
        "-user_id",
        "-product_id",
        "-product.reviews",
        "-product.users",
        "-product.manufacturer",
        "-product.description",
        "-product.image",
        "-user",

    )

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    image = db.Column(db.String)
    _password_hash = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='user')
    products = db.relationship('Product', secondary='reviews', back_populates='users', viewonly=True)

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Please provide a valid email")
        return email

    def __repr__(self):
        return f'<User username is {self.username}>'

    serialize_rules = (
        '-_password_hash',
        '-reviews',
        '-products',
    )

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    ecoFriendlyFeatures = db.Column(db.String)
    category = db.Column(db.String)
    image = db.Column(db.String)

    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'))
    manufacturer = db.relationship('Manufacturer', back_populates='products')

    reviews = db.relationship('Review', back_populates='product', viewonly=True)
    users = db.relationship('User', secondary='reviews', back_populates='products', viewonly=True)

    def __repr__(self):
        return f'<Product name is {self.name}'
    
    serialize_rules = (
        "-reviews",
        "-users",
        "-manufacturer.image",
        "-manufacturer.products",
        "-manufacturer.description",
        "-manufacturer.id",
        "-id",
        "-manufacturer_id",
    )

class Manufacturer(db.Model, SerializerMixin):
    __tablename__ = 'manufacturers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)

    products = db.relationship('Product', back_populates='manufacturer')

    serialize_rules = (
        "-products.reviews",
        "-products.manufacturer",
        "-products.manufacturer_id",
        "-products.users",
        "-products.id",
    )

    def __repr__(self):
        return f'<Manufacturer name is {self.name}'