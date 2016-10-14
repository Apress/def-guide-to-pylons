from filesystem import model
from pylons import config
import os.path
import filesystem.lib.helpers as h

def test_filesystem():
    png = model.load_file('foo.png')
    model.save_file('bar.png', png)
    assert model.list_files() == ['foo.png', 'bar.png']

def test_os():
    path = os.path.join(config['app_conf']['attachments'], 'foo.png')
    size = os.path.getsize(path)
    assert size == 4841L
    assert h.size_to_human(size) == '4&nbsp;KB'

