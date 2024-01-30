from rest_framework.permissions import BasePermission

class CanAccessSurveys(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # You need to define your custom logic here based on request.user permissions
        # Example: Check if the user has specific permissions to access surveys
        # Replace `has_specific_permission` with your actual permission check logic
        return request.user.quote
    
class CanAddSurveys(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return request.user.survey
    
        
class canRegisterUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return request.user.is_staff
    
