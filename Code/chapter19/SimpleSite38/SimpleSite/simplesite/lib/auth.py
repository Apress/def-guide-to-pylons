from authkit.permissions import ValidAuthKitUser
from authkit.permissions import HasAuthKitRole
from authkit.authorize.pylons_adaptors import authorized

is_valid_user = ValidAuthKitUser()
has_delete_role = HasAuthKitRole(['delete'])

