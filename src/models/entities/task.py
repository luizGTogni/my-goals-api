# pylint: disable=not-callable
import enum
import uuid
from sqlalchemy import Column, String, UUID, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.models.settings.base import Base

class StatusTaskEnum(str, enum.Enum):
    TODO = "todo"
    DONE = "done"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(length=150), nullable=False)
    description = Column(String(length=300), nullable=False, unique=True)
    goal_id = Column(UUID(as_uuid=True), ForeignKey("goals.id", ondelete="CASCADE"), nullable=False)
    status = Column(Enum(StatusTaskEnum), default=StatusTaskEnum.TODO, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )
    goal = relationship("Goal", back_populates="tasks")

    def __repr__(self):
        return (
            f"<Task id={self.id} " +
            f"title='{self.title}' " +
            f"description='{self.description}' " +
            f"status='{self.status}'>"
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "goal": self.goal.to_dict(simplified=True),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
