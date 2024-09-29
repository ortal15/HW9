# START
import statistics

temp: list[float] = [-20.0, 39.1, 18.5]
temps: float = 0
while not temps == -999:
    temps: float = float(input('Enter the temperature: '))
    if temps <= -50.0 or temps >= 50.0:
        continue
    temp.append(temps)
    print(temp)
# e
print('max temperature', max(temp))
print('min temperature', min(temp))
# f
number_in_temp: bool = False
for temps in temp:
    if temps == 18.5:
        number_in_temp = True
print('if 18.5 in the list', 18.5 in temp)
# g
print('How many times are there -20?', temp.count(-20))
# h
print('avg temperature', sum(temp) / len(temp))
# i
for temps in temp:
    print(f'temperature{temps}', end=' ')
    print()
# j
if 39.1 in temp:
    print('index(39.1):', temp.index(39.1))
# k
del temp[0]
print('without 0 index', temp)
# l
del temp[1: -1: 2]
print('without even index', temp)
# m
number_in_temp: bool = False
for temps in temp:
    if temps == 18.5:
        temp.remove(18.5)
print('after temp.remove(18.5)', temp)
# n
last_temp = temp.pop()
print('temp after pop last: ', temp)
# o
new_list = temp.copy()
print('sort list', new_list.sort())
# p
reversed_list = temp.copy()
print('reversed list', reversed_list.sort(reverse=True))

# end
