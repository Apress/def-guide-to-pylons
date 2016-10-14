import datetime
from sqlalchemy import schema, types, orm

metadata = schema.MetaData()

def now():
    return datetime.datetime.now()

from sqlalchemy.ext.declarative import declarative_base

# Assign the same metadata object we created earlier.
Base = declarative_base(metadata=metadata)

# We still need the pagetag table because we don't want to explicitly define a
# Pagetag class but still
# need to specify the table in the relation between pages and tags.
pagetag_table = schema.Table('pagetag', metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('pagetag_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer, schema.ForeignKey('page.id')),
    schema.Column('tagid', types.Integer, schema.ForeignKey('tag.id')),
)

class Page(Base):
    __tablename__ = 'page'

    id = schema.Column(types.Integer,
        schema.Sequence('page_seq_id', optional=True), primary_key=True)
    content = schema.Column(types.Text(), nullable=False)
    posted = schema.Column(types.DateTime(), default=now)
    title = schema.Column(types.Unicode(255), default=u'Untitled Page')
    heading = schema.Column(types.Unicode(255))
    comments = orm.relation("Comment", backref="page")
    tags = orm.relation("Tag", secondary=pagetag_table)

class Comment(Base):
    __tablename__ = 'comment'

    id = schema.Column(types.Integer,
        schema.Sequence('comment_seq_id', optional=True), primary_key=True)
    pageid = schema.Column(types.Integer,
    schema.ForeignKey('page.id'), nullable=False)
    content = schema.Column(types.Text(), default=u'')
    name = schema.Column(types.Unicode(255))
    email = schema.Column(types.Unicode(255), nullable=False)
    created = schema.Column(types.TIMESTAMP(), default=now())

class Tag(Base):
    __tablename__ = 'tag'

    id = schema.Column(types.Integer,
        schema.Sequence('tag_seq_id', optional=True), primary_key=True)
    name = schema.Column(types.Unicode(20), nullable=False, unique=True)

page_table = Page.__table__

