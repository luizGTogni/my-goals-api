# pylint: disable=not-callable
import enum
import uuid
from sqlalchemy import Column, String, UUID, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.models.settings.base import Base

class StatusEnum(str, enum.Enum):
    UNCOMPLETED = "uncompleted"
    COMPLETED = "completed"

class Goal(Base):
    __tablename__ = "goals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(length=150), nullable=False)
    description = Column(String(length=300), nullable=False, unique=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.UNCOMPLETED, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )

    owner = relationship("User", back_populates="goals")
    tasks = relationship(
        "Task",
        back_populates="goal",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def __repr__(self):
        return (
            f"<Goal id={self.id} " +
            f"title='{self.title}' " +
            f"description='{self.description}' " +
            f"status='{self.status}'>"
        )
