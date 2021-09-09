from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (hasattr(obj, "owner") and obj.owner == request.user) or (
            hasattr(obj, "user") and obj.user == request.user
        )
