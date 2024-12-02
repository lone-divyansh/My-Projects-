from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department
from django.http import HttpResponse
from django.contrib import messages

# Index view
def index(request):
    return render(request, 'index.html')

# Display all data
def display_data(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    context = {
        'employees': employees,
        'departments': departments
    }
    return render(request, 'display_data.html', context)

# View employees
def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'view_employees.html', {'employees': employees})

# Add employee (with basic form processing)
def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')  # Add this line to get gender from form
        address = request.POST.get('address')
        department_id = request.POST.get('department')
        
        if name and dob and gender and address and department_id:  # Include gender in validation
            department = get_object_or_404(Department, id=department_id)
            new_employee = Employee(
                name=name,
                dob=dob,
                gender=gender,
                address=address,
                department=department
            )
            new_employee.save()
            messages.success(request, 'Employee added successfully.')
            return redirect('view_employees')
        else:
            messages.error(request, 'All fields are required.')
    
    departments = Department.objects.all()
    return render(request, 'add_employee.html', {'departments': departments})

# Remove employee
def remove_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        if employee_id:
            employee = get_object_or_404(Employee, id=employee_id)
            employee.delete()
            messages.success(request, 'Employee removed successfully.')
            return redirect('view_employees')
        else:
            messages.error(request, 'Invalid employee ID.')
    
    employees = Employee.objects.all()
    return render(request, 'remove_employee.html', {'employees': employees})

# Filter employees based on criteria
def filter_employee(request):
    name_query = request.GET.get('name')
    department_query = request.GET.get('department')
    
    # Start with all employees
    filtered_employees = Employee.objects.all()

    # Filter by name if a name query is provided
    if name_query:
        filtered_employees = filtered_employees.filter(name__icontains=name_query)
    
    # Filter by department if a department query is provided
    if department_query:
        filtered_employees = filtered_employees.filter(department__name__icontains=department_query)

    return render(request, 'filter_employee.html', {
        'employees': filtered_employees,
        'name_query': name_query,
        'department_query': department_query
    })
