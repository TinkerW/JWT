from .models import UserInDB
from .hash_password import verify_password
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.heashed_password):
        return False
    return user

from .fake_db import fake_users_db

user = str(input("Введите пользователя: "))
paswd = str(input("Введите пароль: "))
print(authenticate_user(fake_users_db, user, paswd))