#conditional statement --- if, elif, else
#iterative statement -- for ,while
#transfer statement -- brek, countinue, pass

#for

# li = [10,20,30,40,50]
#
# for var in li:
#     if var<=30:
#         print(var)
#     else:
#         print(var)


# string = 'saradha'
# li = []
# for i in string:
#     li.append(i.capitalize())

# new_string = ''.join(li)
# print(new_string)


# s = 'Banglore is capital of karnataka'
# # op :- 'karnataka of capital is Banglore'
#
# # li = s.split(' ')
# # li.reverse()
# # new_st = ' '.join(li)
# # print(new_st)
# s = 'Banglore is capital of karnataka'
#
# s = s[::-1]
# print(s)
# li = []

# for i in s:
#     li.append(i)
# print(li)
#
# word = ''
# for j in li:
#     if j == ' ':
#         break
#     word = word+j
# print(word)
# word = word[::-1]
# print(word)

# s = 'debashis dev'
# l = []
# for i in s:
#     if i not in l:
#         l.append(i)
# print(l)
# st = ''.join(l)
# print(st)




s = 'debashisssss devdd'
li = []
for i in s:
    li.append(i)
di = []
for i in li:
    if li.count(i)>1:
        di.append(i)
        zi = {i:li.count(i) for i in di}
print(zi)





