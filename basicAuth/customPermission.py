from rest_framework.permissions import BasePermission

# cehck custom library in geeky shows video
class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # if request.method =='POST':
            #     return False
            return True
        return False