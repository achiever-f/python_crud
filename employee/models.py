"""
Django Models Module for Employee Management System

This module defines the database structure for the Employee CRUD application.
The Employee model represents an employee record with all necessary personal
and professional information.
"""

from django.db import models

# Create your models here.

class Employee(models.Model):
    """
    Employee Model: Stores employee information in the database
    
    This model represents an employee with personal details, contact information,
    and employment-related data. Each field is designed to capture specific
    aspects of an employee's profile.
    
    Database Table: employee_employee
    """
    
    # Personal Information Fields
    first_name = models.CharField(max_length=30)
    """
    First Name Field: Stores the employee's first name
    
    - Type: CharField (character field)
    - Max Length: 30 characters
    - Validation: Cannot be blank, required field
    - Database: VARCHAR(30) NOT NULL
    """
    
    last_name = models.CharField(max_length=30)
    """
    Last Name Field: Stores the employee's last name
    
    - Type: CharField (character field)
    - Max Length: 30 characters
    - Validation: Cannot be blank, required field
    - Database: VARCHAR(30) NOT NULL
    """
    
    # Contact Information
    email = models.EmailField(unique=True)
    """
    Email Field: Stores the employee's unique email address
    
    - Type: EmailField (validated email format)
    - Constraint: Unique (no duplicate emails allowed)
    - Validation: Must be valid email format, required field
    - Database: VARCHAR(254) UNIQUE NOT NULL
    - Use Case: Primary contact method and login identifier
    """
    
    # Employment Information
    position = models.CharField(max_length=50)
    """
    Position Field: Stores the employee's job title or position
    
    - Type: CharField (character field)
    - Max Length: 50 characters
    - Validation: Cannot be blank, required field
    - Database: VARCHAR(50) NOT NULL
    - Examples: "Software Developer", "Project Manager", "HR Specialist"
    """
    
    hire_date = models.DateField()
    """
    Hire Date Field: Stores when the employee was hired
    
    - Type: DateField (date without time)
    - Validation: Cannot be blank, required field
    - Database: DATE NOT NULL
    - Format: YYYY-MM-DD
    - Use Case: Tracking employee tenure, anniversary calculations
    """
    
    def __str__(self):
        """
        String Representation Method
        
        Returns a human-readable string representation of the Employee object.
        This is used in Django admin, dropdowns, and other UI elements.
        
        Returns:
            str: Full name of the employee (first_name + last_name)
            
        Example:
            >>> employee = Employee(first_name="John", last_name="Doe")
            >>> str(employee)
            'John Doe'
        """
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        """
        Model Meta Class: Provides additional metadata about the Employee model
        
        This inner class defines model-level options and behaviors.
        """
        
        # Default ordering for querysets
        ordering = ['last_name', 'first_name']
        """
        Default Ordering: Specifies how Employee objects should be ordered by default
        
        - Primary: last_name (alphabetical)
        - Secondary: first_name (alphabetical)
        - Effect: Querysets will return employees sorted by last name, then first name
        """
        
        # Verbose names for better admin interface
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        """
        Verbose Names: Human-readable names for the model in Django admin
        
        - verbose_name: Singular form ("Employee")
        - verbose_name_plural: Plural form ("Employees")
        - Used in: Django admin interface, forms, and other UI elements
        """
