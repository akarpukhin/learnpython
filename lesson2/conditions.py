def age_validation(age):
    if age.isdigit():
        return int(age)
    elif age == 'exit':
        exit()
    print(age + ': не возраст')


def main(age):
    if age <= 6 and age > 0:
        print('иди в сад!')

    elif age > 6 and age < 17:
        print('иди в школу!')

    elif age >=17 and age <=22:
        print('пора в универ')

    elif age > 22 and age <= 60:
        print('Работай подлец!')

    else:
        print('ты вообще живой ?')


if __name__ == "__main__":
    while True:
        age = input('Введите возраст: ')
        age = age_validation(age)
        if isinstance(age, int):
            main(age)
        continue