#how many hashes will be sent 
for i in range (1):
    print("#")
else:
    print("#") # answer is 2

#output
my_list = [1,2,3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
    print(my_list)  #[1,1,1,1,2,3]


my_list = [1,2,3,4]
print(my_list[-3:-2])  #[2]

'''
i = 0 
while 1 <= 3:
    i += 2
    print("*")  #infinite loop *
'''

my_list = [3,1, -2]
print(my_list[my_list[-1]]) # 1


z = 10
y = 0
x = y < z and z > y or y > z and z < y 
print(x)  #True

my_list_1 = [1,2,3]
my_list_2 =[]
for v in my_list_1:
    my_list_2.insert(0,v)
    print(my_list_2)  #[3,2,1]

#how many element will this have
my_list = [i for i in range(-1,2)]
print(my_list)  #3 i.e[-1,0,1]

#sum of vals element after execution
vals = [0, 1, 2]
vals.insert(0,1)
del vals[1]
print(vals)  #3 [1,1,2]

#number of hashes #
var = 1 
while var < 10:
    print("#")
    var = var << 1
    print("#")  #8

#output
my_list = [[0,1,2,3] for i in range(2)]
print(my_list[2][0]) #error

#0utput
a = 1
b = 0 
c = a & b 
d =a| b
e = a ^ b
print(c + d + e)  #2

t= [[3-i for i in range (3)] for j in range (3)]
s =0 
for i in range (3): 
    s += t[i][i]
print(s) #6


var = 0 
while var < 6: 
    var += 1
    if var % 2 == 0:
        continue
print("#") #one

#The second assihgnment
vals = [0,1,2]
vals[0], vals[2] = vals[2], vals[0]
print(vals) #reverses the list

#how many stars

i = 0 
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
print("*") # 1


x = 1
x = x == x
print(x) #True

#which 2 are true

nums = [1,2,3]
vals = nums[-1:-2]
print(vals) # nums longer and two different lists

#select two answers
nums = [1,2,3]
vals = nums
del vals[1:2]
print(vals) #nums is replicated and assigned to vals are of the same list
'''