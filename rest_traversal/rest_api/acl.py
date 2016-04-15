from pyramid import security


class StaffAcl(object):

    def __call__(self):
        return [
            (security.Allow, 'g:staff', security.ALL_PERMISSIONS),
            (security.Deny, security.Everyone, security.ALL_PERMISSIONS)
        ]
