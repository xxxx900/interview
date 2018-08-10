import math
import functools

second_configuration = int(input('input your configuration : '))*1000


my_data = [
    "1,10000,40",
    "1,10002,45",
    "1,11015,50",
    "2,10005,42",
    "2,11051,45",
    "2,12064,42",
    "2,13161,42",
]


data_list1 = list()
data_list2 = list()

for d in my_data:
    data = list(map(int,d.split(',')))
    if data[0] == 1:
        data_list1.append(data)
    else:
        data_list2.append(data)

begging_num = (data_list1[0][1]) if data_list1[0][1] <= data_list2[0][1] else data_list2[0][1]

last_num = (data_list1[-1][1]) if data_list1[-1][1] >= data_list2[-1][1] else data_list2[-1][1]
last_num = math.ceil(last_num/1000)*1000

num_config = list(range(begging_num,last_num,second_configuration))

data_one = 0
data_two = 0

for index in range(len(num_config)):
    temp_list = []

    for lone in data_list1[data_one:]:
        time_stamp = lone[1]
        if time_stamp < num_config[index]+999:
            temp_list.append(lone[-1])
            data_one += 1
        else:
            break

    for ltwo in data_list2[data_two:]:
        time_stamp = ltwo[1]
        if time_stamp < num_config[index]+999:
            temp_list.append(ltwo[-1])
            data_two += 1
        else:
            break

    mean = functools.reduce(lambda x, y: x + y, temp_list)/len(temp_list)
    mean = "{:.2f}".format(mean).rstrip('0').rstrip('.')
    print("{}-{}:{}".format(num_config[index], num_config[index] + 999,
                        mean))

