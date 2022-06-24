from rest_framework import permissions

class AdminCanAdd(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_admin:
            return True
        else: 
            return False