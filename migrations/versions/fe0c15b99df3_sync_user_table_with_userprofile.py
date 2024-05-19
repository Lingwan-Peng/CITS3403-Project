"""sync User table with userProfile

Revision ID: fe0c15b99df3
Revises: 6ce81da9e8cb
Create Date: 2024-05-18 21:46:12.751310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe0c15b99df3'
down_revision = '6ce81da9e8cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('superior_post_id',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_password_hash', sa.String(length=256), nullable=False))
        batch_op.add_column(sa.Column('user_phone', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('user_dob', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('user_bio', sa.Text(), nullable=True))
        # batch_op.create_unique_constraint(None, ['user_phone'])
        batch_op.drop_column('user_password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_password', sa.VARCHAR(length=20), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('user_bio')
        batch_op.drop_column('user_dob')
        batch_op.drop_column('user_phone')
        batch_op.drop_column('user_password_hash')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('superior_post_id',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    # ### end Alembic commands ###