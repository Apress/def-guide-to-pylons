from metadata_test import engine, page_table

print "\nSQL Expression Example\n"
ins = page_table.insert(
    values=dict(name=u'test', title=u'Test Page', content=u'Some content!')
)
print ins
result = ins.execute()
print result


