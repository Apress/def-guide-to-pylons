# -- This is some code to test the book sample:

from sqlalchemy import schema, types
from sqlalchemy.engine import create_engine

metadata = schema.MetaData()

page_table = schema.Table('page', metadata,
    schema.Column('id', types.Integer, primary_key=True),
    schema.Column('name', types.Unicode(255), default=u''),
    schema.Column('title', types.Unicode(255), default=u'Untitled Page'),
    schema.Column('content', types.Text(), default=u''),
)

engine = create_engine('sqlite:///:memory:', echo=True)
# engine = create_engine('mysql://user:pass@example.com/testdb', echo=True)
metadata.bind = engine
metadata.create_all(checkfirst=True)

connection = engine.connect()

class Request(object):
    params = {
        'name':'New Page', 
        'title':"New Page'); DROP TABLE page; --",
    }
request = Request()

class SomeController:

    # -- The code in the book starts here

    # This is really BAD, don't do it!
    def create(self):
        name = request.params['name']
        title = request.params['title']
        sql = "INSERT INTO page (name, title) VALUES ('%s', '%s')" % (name, title)
        connection.execute(sql)
        return "Page added"

    # -- and ends here

controller = SomeController()
controller.create()

connection.close()


