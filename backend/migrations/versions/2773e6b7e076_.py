"""empty message

Revision ID: 2773e6b7e076
Revises: 
Create Date: 2022-01-06 23:26:35.085410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2773e6b7e076'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mbti', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('image_link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('compatibility',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_mbti', sa.String(length=10), nullable=False),
    sa.Column('compatible_mbti', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('kor_title', sa.String(length=50), nullable=False),
    sa.Column('eng_title', sa.String(length=70), nullable=False),
    sa.Column('image_link', sa.Text(), nullable=True),
    sa.Column('pub_year', sa.Integer(), nullable=True),
    sa.Column('director', sa.String(length=30), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('story', sa.Text(), nullable=True),
    sa.Column('run_time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('img_url', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('pw', sa.String(length=60), nullable=False),
    sa.Column('mbti', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('actor_in_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('actor_name', sa.String(length=20), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=True),
    sa.Column('answers', sa.String(length=20), nullable=False),
    sa.Column('submitted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character_in_movie',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('character_id', 'movie_id')
    )
    op.create_table('movie_genre',
    sa.Column('genre', sa.String(length=20), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('genre', 'movie_id')
    )
    op.create_table('option',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('mbti_indicator', sa.String(length=5), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('satisfaction',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('user_rating', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('satisfaction')
    op.drop_table('option')
    op.drop_table('movie_genre')
    op.drop_table('character_in_movie')
    op.drop_table('answer')
    op.drop_table('actor_in_movie')
    op.drop_table('user')
    op.drop_table('question')
    op.drop_table('movie')
    op.drop_table('compatibility')
    op.drop_table('character')
    # ### end Alembic commands ###
