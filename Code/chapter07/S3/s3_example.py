from boto.s3.connection import S3Connection
from boto.s3.key import Key
conn = S3Connection('<aws access key>', '<aws secret key>')
bucket = conn.create_bucket('pylonsbook')
k = Key(bucket)
k.key = 'foobar'
k.set_contents_from_filename('foo.png')
k.get_contents_to_filename('bar.png')

