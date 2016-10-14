from authkit.users import md5

passwords = [
    'password1',
    'password2',
    'password3',
    'password4',
    'password5',
]
for password in passwords:
    print md5(password, "some secret string")

