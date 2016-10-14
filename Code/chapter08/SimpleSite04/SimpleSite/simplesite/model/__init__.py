"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from simplesite.model import meta

# Add these two imports:
import datetime
from sqlalchemy import schema, types

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)

    # We are using SQLAlchemy 0.5 so transactional=True is replaced by 
    # autocommit=False
    sm = orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)

    meta.engine = engine
    meta.Session = orm.scoped_session(sm)

def now():
    return datetime.datetime.now()

page_table = schema.Table('page', meta.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('page_seq_id', optional=True), primary_key=True),
    schema.Column('content', types.Text(), nullable=False),
    schema.Column('posted', types.DateTime(), default=now),
    schema.Column('title', types.Unicode(255), default=u'Untitled Page'),
    schema.Column('heading', types.Unicode(255)),
)

comment_table = schema.Table('comment', meta.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('comment_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer,
        schema.ForeignKey('page.id'), nullable=False),
    schema.Column('content', types.Text(), default=u''),
    schema.Column('name', types.Unicode(255)),
    schema.Column('email', types.Unicode(255), nullable=False),
    schema.Column('created', types.TIMESTAMP(), default=now()),
)

pagetag_table = schema.Table('pagetag', meta.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('pagetag_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer, schema.ForeignKey('page.id')),
    schema.Column('tagid', types.Integer, schema.ForeignKey('tag.id')),
)

tag_table = schema.Table('tag', meta.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('tag_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(20), nullable=False, unique=True),
)

class Page(object):
    pass

class Comment(object):
    pass

class Tag(object):
    pass

orm.mapper(Comment, comment_table)
orm.mapper(Tag, tag_table)
orm.mapper(Page, page_table, properties={
    'comments':orm.relation(Comment, backref='page'),
    'tags':orm.relation(Tag, secondary=pagetag_table)
})

