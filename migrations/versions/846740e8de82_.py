"""empty message

Revision ID: 846740e8de82
Revises: da01a22e06c9
Create Date: 2020-10-24 17:24:25.440182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '846740e8de82'
down_revision = 'da01a22e06c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_business_email'), 'business', ['email'], unique=True)
    op.create_index(op.f('ix_business_name'), 'business', ['name'], unique=True)
    op.create_index(op.f('ix_business_username'), 'business', ['username'], unique=True)
    op.create_table('business_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=256), nullable=True),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_post_timestamp', table_name='post')
    op.drop_table('post')
    op.add_column('user', sa.Column('first_name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=64), nullable=True))
    op.drop_column('user', 'about_me')
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DATETIME(), nullable=True))
    op.add_column('user', sa.Column('about_me', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    op.drop_table('comment')
    op.drop_table('business_comment')
    op.drop_index(op.f('ix_business_username'), table_name='business')
    op.drop_index(op.f('ix_business_name'), table_name='business')
    op.drop_index(op.f('ix_business_email'), table_name='business')
    op.drop_table('business')
    # ### end Alembic commands ###
