import bcrypt

class PasswordHandler:
    def encrypt_password(self, password_plain: str) -> str:
        hashed = bcrypt.hashpw(password_plain.encode("utf-8"), salt=bcrypt.gensalt(rounds=12))
        return hashed

    def check_password(self, password_plain: str, password_hashed: str) -> bool:
        return bcrypt.checkpw(password_plain.encode("utf-8"), password_hashed)
