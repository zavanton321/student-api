from rest_framework import permissions


class IsRegistrator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.registrator == request.user
