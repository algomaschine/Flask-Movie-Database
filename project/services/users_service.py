from flask import abort
from project.dao.base import BaseDAO

from project.tools import security

class UsersService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao


    def get_one(self, email):
        user = self.dao.get_one(email)
        return user


    def get_one_by_id(self, uid):
        user = self.dao.get_one_by_id(uid)   
        return user 


    def login(self, data):
        
        user = self.get_one(data['email'])

        if user is None:
            abort(404, description='User not found')

        if not security._compare_passwords(user.password, data['password']):
            abort(401, description='Wrong password')

        return security._generate_tokens(user.id, data['password'])


    def create(self, data):
        data["password"] = security._get_password_hash(data["password"])
        return self.dao.create(data)


    def update(self, uid, data):
        if data is None:
            abort(400, description='No data given')
        return self.dao.update(uid, data), 'OK', 200


    def update_password(self, uid, data):

        user = self.get_one_by_id(uid)

        if not security._compare_passwords(user.password, data['password']):
            abort(401, description='Wrong password')

        new_password = security._get_password_hash(data.get("new_password"))
        
        self.dao.update_password(user, new_password)

        return 'OK', 200
