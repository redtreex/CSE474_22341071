def calculate_tax(a, s, job_des):
    job_des = job_des.lower()
    if a < 18 or job_des == 'president' or s < 10000:
        return 0
    if s < 20000:
        return salary * 0.05
    else:
        return salary * 0.1


age = int(input())
salary = int(input())
occupation = input()

print(calculate_tax(age, salary, occupation))
