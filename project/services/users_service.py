from flask import abort, Response
from typing import Dict
from project.dao.base import BaseDAO
from project.tools import security
from project.exceptions import ItemNotFound, NotAuthorized, BadRequest


class UsersService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_one(self, email: str) -> object:
        """
        Gets a user from the database by email.
        """
        user = self.dao.get_one(email)
        if not user:
            raise ItemNotFound(f'User not found')
        return user

    def get_one_by_id(self, uid: int) -> object:
        """
        Gets a user from the database by id.
        """
        user = self.dao.get_one_by_id(uid)   
        if not user:
            raise ItemNotFound(f'User not found')
        return user 

    def login(self, data: Dict) -> Dict:
        """
        Checks the user data, returns a token pair if success.
        """
        try:
            user_email = data['email']
        except:
            raise BadRequest(f"No email given")
        
        user = self.get_one(data['email']) 
        if not user:
            raise ItemNotFound(f'User not found')
            
        if not security._compare_passwords(user.password, data['password']):
            raise NotAuthorized(f"Wrong password")
        return security._generate_tokens(user.id, data['password'])

    def create(self, data: Dict) -> object:
        """
        Calls the password hashing function and sends the new user's data
        with a hashed password to create a new user in the database.
        """
        try:
            data["password"] = security._get_password_hash(data["password"])
            return self.dao.create(data)
        except AttributeError:
            raise BadRequest(f"Password should be a string")

    def update(self, uid: int, data: Dict) -> object:
        """
        If data not empty, sends it
        to update the user's data in the database.
        """
        try:
            return self.dao.update(uid, data)
        except:
            raise ItemNotFound(f"User doesn't exist")

    def update_password(self, uid: int, data: Dict) -> None:
        """
        Compares the provided password with the user's password, 
        calls the password hashing function and sends the new
        password hash to update the user's password in the database.
        """
        user = self.get_one_by_id(uid)
        password_hash = user.password
        if not security._compare_passwords(password_hash, data['password']):
            raise NotAuthorized(f"Wrong password")

        try:
            new_password = data["new_password"]
        except:
             raise BadRequest(f"No new password given")
            
        new_password = security._get_password_hash(new_password)
        self.dao.update_password(uid, new_password)
        return Response('OK', status=200)
