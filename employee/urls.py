"""
URLPattrList: Maps url patterns to view functions

Each URL pattern consists of:
- URL pattern
- Target view function
- Optional name for template referencing

These support the full CRUD lifecycle:
1. READ: Display individual employee form
2. CREATE: Show creation form and process creation data
3. UPDATE: Show update form and process update data
4. DELETE: Remove employee records
"""

from django.urls import path
from . import views

# Define URL patterns for the employee application
urlpatterns = [
	# Home Page - Display all employees
	path('', views.home, name='home'),
	# Create Employee Form Display
	path('create/', views.create_view, name='create'),
	# Create Employee Form Processing
	path('create_employee/', views.create_employee, name='create_employee'),
	# Update Employee Form Display
	path('update/<int:id>/', views.update_view, name='update'),
	# Update Employee Form Processing
	path('update_employee/<int:id>/', views.update_employee, name='update_employee'),
	# Delete Employee
	path('delete/<int:id>/', views.delete, name='delete'),
]
