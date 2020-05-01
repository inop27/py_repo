n = int(input())

boss_list = map(int, input().split())

employee_list = [0] * (n - 1)

for boss in boss_list:
	employee_list[boss - 1] += 1
	
for employee in employee_list:
	print(employee)
