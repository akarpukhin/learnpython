def get_summ(first_name, second_name, middle_name=''):	
	
	if len(middle_name) < 1:
		fio = first_name + ' ' + second_name
	else:	
		fio = first_name + ' ' + second_name + ' ' + middle_name
	
	return fio.upper()


first = input("Твое Имя : ")
second = input("Твоя Фамилия : ")
third = input("Твоя Отчество : ")

print(get_summ(first, second, third))