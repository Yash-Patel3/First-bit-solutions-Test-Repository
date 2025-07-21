employees = int(input("Enter the number of employees: "))

salaryofallemployees = 0  

for i in range(1, employees + 1):
    salary = int(input(f"Enter the salary of employee {i}: "))
    
    if salary > 20000:
        da = 0.15 * salary
        ta = 0.18 * salary
        hra = 0.20 * salary
    else:
        da = 0.10 * salary
        ta = 0.12 * salary
        hra = 0.15 * salary

    totalsalary = salary + da + ta + hra
    salaryofallemployees += totalsalary

print("Total salary of all employees :", salaryofallemployees)
