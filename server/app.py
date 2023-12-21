#!/usr/bin/env python3
from flask import request, make_response, session, abort, render_template
from flask_restful import Resource

from config import app, db, api
from models import User, Manufacturer, Product, Review

from flask_restful import Resource


# @app.route('/')
# def index():
#     response_body = '<h1>Welcome to EcoConsumer!</h1>'
#     response =  make_response(
#         response_body,
#         200
#     )
#     return response


class Signup(Resource):
    def post(self):
        json_data = request.get_json()
        username = json_data.get('username')
        email = json_data.get('email')
        password = json_data.get('password')
        image = json_data.get('image')

        if username and password:
            new_user = User(
                username=username,
                email = email,
                image = image,
                
            )
            new_user.password_hash = password
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id
        
            response = make_response(new_user.to_dict(), 201)
            return response
        

api.add_resource(Signup, "/api/signup")

class Login(Resource):
    def post(self):
        json_data = request.get_json()
        username = json_data.get('username')
        password = json_data.get('password')
        user = User.query.filter(User.username == username).first()

        if user and user.authenticate(password):
            session['user_id'] = user.id
            response = make_response(user.to_dict(), 200)
            return response
        else:
            return {'error': 'Authentication failed'}, 401

api.add_resource(Login, '/api/login')

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')

        if user_id is not None:
            user = User.query.filter_by(id=user_id).first()
            if user:
                response = make_response(user.to_dict(), 200)
                return response
            else:
                abort(401, "User not found")
        else:
            abort(401, "Please log in")

api.add_resource(CheckSession, '/api/check_session')

class Logout(Resource):
    def delete(self):
        session.clear() 
        response = make_response('', 204)
        return response
    
api.add_resource(Logout, '/api/logout')

class UsersResource(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200
    
api.add_resource(UsersResource, '/api/users')

class ManufacturersResource(Resource):
    def get(self):
        manufacturers = Manufacturer.query.all()
        return [manufacturer.to_dict() for manufacturer in manufacturers], 200
    
api.add_resource(ManufacturersResource, "/api/manufacturers")

class ManufacrurerResource(Resource):
    def get(self, manuf_id):
        manuf = Manufacturer.query.filter_by(id = manuf_id).first()

        response = make_response(
            manuf.to_dict(),
            200
        )
        return response
    
api.add_resource(ManufacrurerResource, "/api/manufacturers/<int:manuf_id>")

class ProductsResource(Resource):
    def get(self):
        products = Product.query.all()
        return [product.to_dict() for product in products], 200

api.add_resource(ProductsResource, "/api/products")

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id = product_id).first()

        response = make_response(
            product.to_dict(),
            200
        )
        return response
    
api.add_resource(ProductResource, "/api/products/<int:product_id>")

class ReviewsResource(Resource):
    def get(self):
        reviews = Review.query.all()
        return [review.to_dict() for review in reviews], 200
    
    def post(self):
        review_data = request.get_json()
        content = review_data.get('content')
        rating = review_data.get('rating')
        user_id = review_data.get('user_id')
        product_id = review_data.get('product_id')

        new_review = Review(
            content = content,
            rating= rating,
            user_id=user_id,
            product_id=product_id,
        )
        db.session.add(new_review)
        db.session.commit()

        return new_review.to_dict(), 201

api.add_resource(ReviewsResource, "/api/reviews")

class ReviewResource(Resource):
    def patch(self, product_id, review_id):
        data = request.get_json()

        selected_review = Review.query.filter_by(id=review_id, product_id=product_id).first()

        if not selected_review:
            return {"error": "Review not found"}, 404

        # Update only if the data is present in the request
        if 'content' in data:
            selected_review.content = data['content']
        if 'rating' in data:
            selected_review.rating = data['rating']

        db.session.commit()

        response = make_response(
            selected_review.to_dict(),
            200
        )
        return response

    def delete(self, product_id, review_id):
        deleted_review = Review.query.filter_by(id=review_id, product_id=product_id).first()

        if not deleted_review:
            return {"error": "Review not found"}, 404

        db.session.delete(deleted_review)
        db.session.commit()

        response = make_response(
            "Deletion completed",
            204
        )

        return response
    
api.add_resource(ReviewResource, "/api/products/<int:product_id>/reviews/<int:review_id>")

@app.route('/')
@app.route("/companies/:companyId")
@app.route("/products/:productId")
@app.route("/login")
@app.route("/signup")
@app.route("/products")
@app.route("/companies")
def index(id=0):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    