import os
from pylons import config

def load_file(filename):
    path = os.path.join(config['app_conf']['attachments'], filename)
    fp = open(path, 'rb')
    data = fp.read()
    fp.close()
    return data

def save_file(filename, data):
    path = os.path.join(config['app_conf']['attachments'], filename)
    fp = open(path, 'wb')
    fp.write(data)
    fp.close()

def list_files():
    path = os.path.join(config['app_conf']['attachments'])
    return os.listdir(path)


