from authkit.permissions import ValidAuthKitUser
from authkit.permissions import HasAuthKitRole

is_valid_user = ValidAuthKitUser()
has_delete_role = HasAuthKitRole(['delete'])

