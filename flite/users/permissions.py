from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of objects to see them
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user

class HasBankAccount(permissions.BasePermission):
    """
    View-level permission to only allow Users with bank accounts access a view
    """

    def has_permission(self, request, view):
        return request.user.accounts.count() >= 1


