from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


hashed_pass = str(input("Введите пароль: "))
print(get_password_hash(hashed_pass))
set_password = str(input("Логин: "))
print(verify_password(set_password, hashed_pass))