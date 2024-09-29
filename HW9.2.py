# start

number_list: list[int] = []

while True:
    number: int = int(input('enter a number between 10-0:'))
    if number == -999:
        break
    if number >= 10 or number <= 0:
        print('number not in range...')
    else:
        number_list.append(number)

for number in number_list:
    if number_list.count(number) > 0:
        print(number, 'entered', number_list.count(number), 'times')

print(number_list)
# end
