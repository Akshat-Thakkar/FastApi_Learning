from passlib.context import CryptContext

pw_context= CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hashing:
    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password."""
        return pw_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """Hash a plain password."""
        return pw_context.hash(password)