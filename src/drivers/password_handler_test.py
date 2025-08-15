from .password_handler import PasswordHandler

def test_password_handler():
    handle = PasswordHandler()
    password_plain = "123456"
    password_hashed = handle.encrypt_password(password_plain)

    assert handle.check_password(password_plain, password_hashed)
