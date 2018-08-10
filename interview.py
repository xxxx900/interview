# class Calcul():
#     def __init__(self,price,payment):
#         self.price = price
#         self.payment = payment
#         self.myDollarbill = {
#                              '50': 0,
#                              '10': 0,
#                              '5': 0,
#                              '1': 0,
#                              '0.5': 0,
#                              '0.25': 0,
#                              '0.10': 0,
#                              '0.05': 0,
#                              '0.01': 0,
#                              }
#
#     def calChange(self):
#         self.change = round(self.payment - self.price,2)
#         if(self.change>0):
#             return self.change
#         else:
#             return 'You paid less than the price.'
#
#     def calDollarBill(self):
#         for bill in self.myDollarbill.keys():
#             curBill = float(bill)
#             while(curBill<=self.change):
#                 self.myDollarbill[bill] +=1
#                 self.change -= curBill
#
#     def dump(self):
#         print(self.myDollarbill)
#
# try:
#     # price, payment = input("price, payment").split(' ')
#     # myCal = Calcul(float(price),float(payment))
#     myCal = Calcul(12.21,20)
#     myCal.calChange()
#     myCal.calDollarBill()
#     myCal.dump()
# except Exception as e:
#     print(e)
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# class A():
#     def __init__(self):
#         pass
#     def set(self,name):
#         self._name = name
#     def get(self):
#         return self._name
#     a = property(get,set)
#
# a = A()
# a.set("hello")
# print(a.get())
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# s = 3.142
# a = open("Hello.txt","w")
# print("it from print Yes", file=a)
# a.writelines("Hellow")
# a.write("asdfasdfasd")

# try:
#     if '1' != 1:
#         raise Exception("some error")
#     else:
#         print("what")
# except Exception("some error") as e:
#     print(e)


# a = {0:"hello"}
# print(a[0])
#
# if 0 in a:
#     print("Correct")
# else:
#     print("No")


# import threading


# a = input("").split(',')
# my_data = [
#     (1,10000,40,),
#     (1,10002,45,),
#     (1,11015,50,),
#     (2,10005,42,),
#     (2,11051,45,),
#     (2,12064,42,),
#     (2,13161,42,),
# ]

my_data = [
    "1,10000,40",
    "1,10002,45",
    "1,11015,50",
    "2,10005,42",
    "2,11051,45",
    "2,12064,42",
    "2,13161,42",
]

# import numpy as np
#
# time_config = int(input('Time configuration per milliseconds'))
# time_config = 1
# range_config = range(0,100000,time_config*10000)
#
# np_first_row = np.empty(shape=[0,3])
# np_second_row = np.empty(shape=[0,3])
#
# for data in my_data:
#     data_row = data.split(',')
#     if data_row[0] == '1':
#         np_first_row = np.append(np_first_row, data, axis=0)
#     else:
#         np_second_row = np.append(np_second_row, data, axis=0)
#
# print(np_first_row)

