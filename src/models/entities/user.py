# pylint: disable=not-callable
import uuid
from sqlalchemy import Column, String, UUID, DateTime
from sqlalchemy.sql import func
from src.models.settings.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(length=150), nullable=False)
    username = Column(String(length=100), nullable=False, unique=True)
    email = Column(String(length=200), nullable=False)
    password = Column(String(), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return (
            f"<User id={self.id} " +
            f"name='{self.name}' " +
            f"username='{self.username}' " +
            f"email='{self.emai}'>"
        )
