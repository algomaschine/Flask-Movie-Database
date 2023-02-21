from project.models import User

class UsersDAO:
    def __init__(self, session):
        self.session = session


    def get_one(self, email):
        """
        Gets user from the database by email.
        """
        return self.session.query(User).filter(User.email == email).first()


    def get_one_by_id(self, uid):
        """
        Gets user from the database by id.
        """
        return self.session.query(User).get(uid)


    def create(self, data):
        """
        Creates a new user in the database.
        """
        new_user = User(**data)

        self.session.add(new_user)
        self.session.commit()
        
        return new_user


    def update(self, uid, data):
        """
        Updates the user's data in the database.
        """
        user = self.get_one_by_id(uid)

        user.name = data.get("name")
        user.surname = data.get("surname")
        user.favorite_genre = data.get("favorite_genre")

        self.session.add(user)
        self.session.commit()

        return user


    def update_password(self, user, password):
        """
        Updates the user's password in the database.
        """
        user.password = password

        self.session.add(user)
        self.session.commit()
    