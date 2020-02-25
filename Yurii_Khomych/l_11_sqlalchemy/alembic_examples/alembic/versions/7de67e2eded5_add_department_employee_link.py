"""add department_employee_link

Revision ID: 7de67e2eded5
Revises: 38b0b83a83b1
Create Date: 2019-11-02 11:31:28.302373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7de67e2eded5"
down_revision = "38b0b83a83b1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "department_employee_link",
        sa.Column("department_id", sa.Integer(), nullable=False),
        sa.Column("employee_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["department_id"], ["department.id"],),
        sa.ForeignKeyConstraint(["employee_id"], ["employee.id"],),
        sa.PrimaryKeyConstraint("department_id", "employee_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("department_employee_link")
    # ### end Alembic commands ###
