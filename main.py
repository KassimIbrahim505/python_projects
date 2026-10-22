firstName = 'kassim'
lastName = 'Ibrahim'
employee_name = firstName + ' ' + lastName
employee_age = 25 
employee_department = "IT Support Officer"
address = "123 Main Street"
address += " Kololo Avenue"
employee_card = "IT-2026-003"
salary = 500000
employee_details = f'Employee Name: {employee_name} | Age: {employee_age} | Address: {address}'
employee_info = 'Employed as: ' + employee_department  + ' | Employee card Numeber: ' + employee_card + 'Salaary: ' + str(salary)

print(employee_details)
print(employee_info)
