from metadata_test import engine, page_table

print "\nSQL Expression Example\n"

connection = engine.connect()
ins = page_table.insert(
    values=dict(name=u'test', title=u'Test Page', content=u'Some content!')
)
print ins
result = connection.execute(ins)
print result

print "\nSelecting Results\n"

from sqlalchemy.sql import select

s = select([page_table])
result = connection.execute(s)
for row in result:
    print row

# s = select([page_table], (page_table.c.id<=10) & (page_table.c.name.like(u't%')))
from sqlalchemy.sql import and_, or_, not_
s = select([page_table], and_(page_table.c.id<=10, page_table.c.name.like(u't%')))
s = s.order_by(page_table.c.title.desc(), page_table.c.id)
result = connection.execute(s)
print result.fetchall()

connection.close()


