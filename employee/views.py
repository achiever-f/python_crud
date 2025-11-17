"""
Django Views Module for Employee Management System

This module contains all view functions for the Employee CRUD application.
Each view handles specific HTTP requests and returns appropriate responses
for creating, reading, updating, and deleting employee records.

Views:
- home: Display all employees in a table format
- create_view: Show the employee creation form
- create_employee: Process employee creation form submission
- update_view: Show the employee update form with existing data
- update_employee: Process employee update form submission
- delete: Delete an employee record

HTTP Methods:
- GET: For displaying forms and data
- POST: For submitting form data (create, update operations)
"""

# Django shortcuts for common view operations
from django.shortcuts import render, redirect, get_object_or_404
# Import the Employee model for database operations
from .models import Employee

# Create your views here.

def home(request):
    """
    Home View: Display all employees in a table format
    
    This view handles GET requests to the home page and displays all employee
    records from the database in a tabular format.
    
    HTTP Method: GET
    URL Pattern: '' (root URL)
    Template: home.html
    
    Args:
        request (HttpRequest): The HTTP request object
        
    Returns:
        HttpResponse: Renders the home.html template with all employee data
        
    Context Variables:
        employees (QuerySet): All Employee objects from the database
        
    Example:
        GET / -> Returns table with all employees
    """
    # Retrieve all employee records from the database
    employees = Employee.objects.all()
    
    # Render the home template with employee data
    return render(request, 'home.html', {'employees': employees})

def create_view(request):
    """
    Create View: Display the employee creation form
    
    This view displays a blank form for creating a new employee.
    It only handles GET requests to show the form.
    
    HTTP Method: GET
    URL Pattern: 'create/'
    Template: create.html
    
    Args:
        request (HttpRequest): The HTTP request object
        
    Returns:
        HttpResponse: Renders the create.html template with an empty form
        
    Note:
        The actual form submission is handled by create_employee view
    """
    # Render the create employee form template
    return render(request, 'create.html')

def create_employee(request):
    """
    Create Employee View: Process employee creation form submission
    
    This view handles POST requests from the employee creation form.
    It validates the form data and creates a new employee record in the database.
    
    HTTP Method: POST
    URL Pattern: 'create_employee/'
    Template: create.html (for validation errors)
    Redirect: '/' (home page) on successful creation
    
    Args:
        request (HttpRequest): The HTTP request object containing POST data
        
    Returns:
        HttpResponse: Redirects to home page on success, or renders form again on failure
        
    Form Fields Expected:
        - first_name (str): Employee's first name (required)
        - last_name (str): Employee's last name (required)
        - email (str): Employee's unique email address (required)
        - position (str): Employee's job position (required)
        - hire_date (date): Employee's hire date (required)
        
    Validation:
        All fields must be provided and non-empty
        
    Example:
        POST /create_employee/ with form data -> Creates new employee and redirects home
    """
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Extract form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        hire_date = request.POST.get('hire_date')
        
        # Validate that all required fields are provided
        if first_name and last_name and email and position and hire_date:
            # Create new employee record in the database
            Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                position=position,
                hire_date=hire_date
            )
            # Redirect to home page after successful creation
            return redirect("/")
    
    # If validation fails or request is not POST, show the form again
    return render(request, 'create.html')

def update_view(request, id):
    """
    Update View: Display the employee update form with existing data
    
    This view displays a pre-filled form for updating an existing employee.
    It retrieves the employee record and populates the form with current data.
    
    HTTP Method: GET
    URL Pattern: 'update/<int:id>/'
    Template: update.html
    
    Args:
        request (HttpRequest): The HTTP request object
        id (int): The primary key of the employee to update
        
    Returns:
        HttpResponse: Renders update.html with employee data
        
    Context Variables:
        employee (Employee): The Employee object to be updated
        
    Error Handling:
        Returns 404 error if employee with given ID doesn't exist
        
    Example:
        GET /update/5/ -> Shows update form for employee with ID 5
    """
    # Retrieve employee object or return 404 if not found
    employee = get_object_or_404(Employee, id=id)
    
    # Render the update template with employee data
    return render(request, 'update.html', {'employee': employee})

def update_employee(request, id):
    """
    Update Employee View: Process employee update form submission
    
    This view handles POST requests from the employee update form.
    It validates the form data and updates the existing employee record.
    
    HTTP Method: POST
    URL Pattern: 'update_employee/<int:id>/'
    Template: update.html (for validation errors)
    Redirect: '/' (home page) on successful update
    
    Args:
        request (HttpRequest): The HTTP request object containing POST data
        id (int): The primary key of the employee to update
        
    Returns:
        HttpResponse: Redirects to home page on success, or renders form again on failure
        
    Form Fields Expected:
        - first_name (str): Employee's first name (required)
        - last_name (str): Employee's last name (required)
        - email (str): Employee's unique email address (required)
        - position (str): Employee's job position (required)
        - hire_date (date): Employee's hire date (required)
        
    Validation:
        All fields must be provided and non-empty
        
    Error Handling:
        Returns 404 error if employee with given ID doesn't exist
        
    Example:
        POST /update_employee/5/ with form data -> Updates employee and redirects home
    """
    # Retrieve employee object or return 404 if not found
    employee = get_object_or_404(Employee, id=id)
    
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Extract updated form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        hire_date = request.POST.get('hire_date')
        
        # Validate that all required fields are provided
        if first_name and last_name and email and position and hire_date:
            # Update employee object with new data
            employee.first_name = first_name
            employee.last_name = last_name
            employee.email = email
            employee.position = position
            employee.hire_date = hire_date
            
            # Save changes to database
            employee.save()
            
            # Redirect to home page after successful update
            return redirect("/")
    
    # If validation fails or request is not POST, show the form again
    return render(request, 'update.html', {'employee': employee})

def delete(request, id):
    """
    Delete View: Delete an employee record
    
    This view handles the deletion of an employee record from the database.
    It retrieves the employee, deletes it, and redirects to the home page.
    
    HTTP Method: GET
    URL Pattern: 'delete/<int:id>/'
    Redirect: '/' (home page)
    
    Args:
        request (HttpRequest): The HTTP request object
        id (int): The primary key of the employee to delete
        
    Returns:
        HttpResponse: Redirects to home page after deletion
        
    Error Handling:
        Returns 404 error if employee with given ID doesn't exist
        
    Security Note:
        In production, this should be a POST request with CSRF protection
        to prevent accidental deletions via GET requests
        
    Example:
        GET /delete/5/ -> Deletes employee with ID 5 and redirects home
    """
    # Retrieve employee object or return 404 if not found
    employee = get_object_or_404(Employee, id=id)
    
    # Delete the employee record from the database
    employee.delete()
    
    # Redirect to home page after successful deletion
    return redirect("/")
