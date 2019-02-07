"""empty message

Revision ID: 0ac5d3d652fc
Revises: 
Create Date: 2019-01-15 07:09:52.819820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ac5d3d652fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('file_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_file_name'), 'content', ['file_name'], unique=True)
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('background_image', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phrases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phrase', sa.String(length=200), nullable=True),
    sa.Column('file_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_phrases_file_name'), 'phrases', ['file_name'], unique=True)
    op.create_table('section',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('section_name', sa.String(length=200), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('file_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_section_file_name'), 'section', ['file_name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=True),
    sa.Column('surname', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('social_id', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=200), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('social_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('due_on', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('billing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_billed', sa.Date(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('billing')
    op.drop_table('account')
    op.drop_table('user')
    op.drop_index(op.f('ix_section_file_name'), table_name='section')
    op.drop_table('section')
    op.drop_index(op.f('ix_phrases_file_name'), table_name='phrases')
    op.drop_table('phrases')
    op.drop_table('course')
    op.drop_index(op.f('ix_content_file_name'), table_name='content')
    op.drop_table('content')
    # ### end Alembic commands ###