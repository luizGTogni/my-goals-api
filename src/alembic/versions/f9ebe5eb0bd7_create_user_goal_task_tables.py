# pylint: disable=no-member
"""create user, goal, task tables

Revision ID: f9ebe5eb0bd7
Revises: 
Create Date: 2025-08-23 14:48:52.086451

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'f9ebe5eb0bd7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column(
        'created_at',
        sa.DateTime(timezone=True),
        server_default=sa.text('now()'),
        nullable=False
    ),
    sa.Column(
        'updated_at',
        sa.DateTime(timezone=True),
        server_default=sa.text('now()'),
        nullable=False
    ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('goals',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('status', sa.Enum('UNCOMPLETED', 'COMPLETED', name='statusenum'), nullable=False),
    sa.Column(
        'created_at',
        sa.DateTime(timezone=True),
        server_default=sa.text('now()'),
        nullable=False
    ),
    sa.Column(
        'updated_at',
        sa.DateTime(timezone=True),
        server_default=sa.text('now()'),
        nullable=False
    ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.create_table('tasks',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('goal_id', sa.UUID(), nullable=False),
    sa.Column('status', sa.Enum('TODO', 'DONE', name='statustaskenum'), nullable=False),
    sa.Column(
        'created_at',
        sa.DateTime(timezone=True),
        server_default=sa.text('now()'),
        nullable=False
    ),
    sa.Column(
        'updated_at',
        sa.DateTime(timezone=True),
        server_default=sa.text('now()'),
        nullable=False
    ),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("tasks", "status")
    op.drop_column("goals", "status")
    status_enum = sa.Enum("UNCOMPLETED", "COMPLETED", name="statusenum")
    status_task_enum = sa.Enum("TODO", "DONE", name="statustaskenum")
    status_enum.drop(op.get_bind())
    status_task_enum.drop(op.get_bind())
    op.drop_table('tasks')
    op.drop_table('goals')
    op.drop_table('users')
