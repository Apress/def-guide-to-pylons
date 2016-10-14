from authkit.permissions import *

# User has the 'admin' role:
HasAuthKitRole('admin')

# User has the 'admin' or 'editor' role:
HasAuthKitRole(['admin', 'editor'])

# User has the both 'admin' and 'editor' roles:
HasAuthKitRole(['admin', 'editor'], all=True)

# User has no roles:
HasAuthKitRole(None)

# User in the 'pylons' group:
HasAuthKitGroup('pylons')

# User in the 'pylons' or 'django' groups:
HasAuthKitGroup(['pylons', 'django'])

# User not in a group:
HasAuthKitGroup(None)

# Combine permissions
And(HasAuthKitRole('admin'), HasAuthKitGroup('pylons'))

# Only allow access from 127.0.0.1 or 10.10.0.1
permission = FromIP(["127.0.0.1", "10.10.0.1"])

# Only allow access between 6pm and 8am
from datetime import time
permission = BetweenTimes(start=time(18), end=time(8))


