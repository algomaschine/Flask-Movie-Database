from flask import abort, Response
from project.dao.base import BaseDAO
from project.tools import security


class UsersService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get_one(self, email):
        """
        Gets a user from the database by email.
        """
        user = self.dao.get_one(email)
        return user

    def get_one_by_id(self, uid):
        """
        Gets a user from the database by id.
        """
        user = self.dao.get_one_by_id(uid)   
        return user 

    def login(self, data):
        """
        Checks the user data, returns a token pair if success.
        """
        try:
            user = self.get_one(data['email']) 
        except:
            abort(404, description='User not found')
            
        if not security._compare_passwords(user.password, data['password']):
            abort(401, description='Wrong password')
        return security._generate_tokens(user.id, data['password'])

    def create(self, data):
        """
        Calls the password hashing function and sends the new user's data
        with a hashed password to create a new user in the database.
        """
        try:
            data["password"] = security._get_password_hash(data["password"])
            return self.dao.create(data)
        except:
            abort(500, description='No password')

    def update(self, uid, data):
        """
        If data not empty, sends it
        to update the user's data in the database.
        """
        if data is None:
            abort(400, description='No data given')
        try:
            return self.dao.update(uid, data)
        except:
            abort(400, description='User not found')

    def update_password(self, uid, data):
        """
        Compares the provided password with the user's password, 
        calls the password hashing function and sends the new
        password hash to update the user's password in the database.
        """
        user = self.get_one_by_id(uid)
        password_hash = user.password
        if not security._compare_passwords(password_hash, data['password']):
            abort(401, description='Wrong password')

        new_password = data["new_password"]
        if not new_password:
            abort(401, description='No new password given')
        new_password = security._get_password_hash(new_password)
        self.dao.update_password(uid, new_password)
        return Response('OK', status=200)
