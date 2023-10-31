#!/usr/bin/env python3
from flask import request, make_response, session, abort
from flask_restful import Resource

from config import app, db, api
from models import User

from flask_restful import Resource
from config import api, db


@app.route('/')
def index():
    response_body = '<h1>Welcome to EcoConsumer!</h1>'
    response =  make_response(
        response_body,
        200
    )
    return response


class Signup(Resource):
    def post(self):
        json_data = request.get_json()

        username = json_data.get('username')
        email = json_data.get('email')
        password = json_data.get('password')

        if username and password:
            new_user = User(
                username=username,
                email = email,
            )
            new_user.password_hash = password
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id
        
            response = make_response(new_user.to_dict(), 201)
            return response
        

api.add_resource(Signup, "/api/signup/")

class Login(Resource):
    def post(self):
        json_data = request.get_json()
        username = json_data.get('username')
        password = json_data.get('password')
        user = User.query.filter(User.username == username).first()
        
        if user:
            if user.authenticate(password):
                session['user_id'] = user.id
                response = make_response(user.to_dict(), 200)
                return response
        return {'Incorrect username or password'}, 401
    
api.add_resource(Login, '/api/login/')

class CheckSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            response = make_response(user.to_dict(), 200)
            return response
        except:
            abort(401, "Please log in")

api.add_resource(CheckSession, '/api/check_session/')

class Logout(Resource):
    def delete(self):
        session.clear() 
        response = make_response('', 204)
        return response
    
api.add_resource(Logout, '/api/logout/')

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200
    
api.add_resource(Users, '/api/users/')