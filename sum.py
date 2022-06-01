
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 38, 35, 7]
sum = 0
for i in numbers:
  if i>20 and i<40:
    sum+=1
print(sum)




numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i= 0
numbers.sort()
print(numbers)
for i in range(len(numbers)):
    print(numbers[-1],"is max")
    break


places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
for i in range(len(places)):
    print(places[-i-1])
    i-=1


l_st= list(input("enter num or name: ")) 
a = l_st.copy()
l_st.reverse()
# print(l_st.reverse)
if l_st==a:
  print("its palindrome")
else:
  print("no its not")


number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i = 0
sum = []
while i<len(n):
    j = 0
    add = []
    while j<i:
        if n[i]+n[j]==number:
            add.append(n[i])
            add.append(n[j])
            j+=1
            sum.append(add)           

        j+=1
    i+=1
print(sum)

for i in n:
    for j in n:
        if i+j == number:
            add.append(i)
            add.appemd[j]
        
            sum.append(add)
    
print(sum)



list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
list3 = []
i=0
while i<len(list2):
    if  list1[i] not in list2:
       list3.append(list1[i])
    i+=1
print("these element are not present", list3)


number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i = 0
pair = []
while i<len(n):
  c = []
  j = 0
  while j<len(n):
    if n[i]+n[j]==30:
      c.append(n[i])
      c.append(n[j])
      pair.append(c)
    j+=1
  i+=1
print(pair)


this question made me mad
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i = 0
pair= []
for i in n: #while i<len(n)
  c=[]
  for j in n:# while j<len(n)
    if i+j==30:
      c.append(i)
      c.append(j)
      pair.append(c)
print(pair)




marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i = 0
j = 0


while i<len(marks):
  j = 0
  sum1=0
  while j<len(marks[i]):
    sum1+=marks[i][j]
    avg = sum1/len(marks[i])
    j+=1
  i+=1
  print("sum of year",":",i,"-",sum1,"and",avg)
  print("avg of year ",i,avg)




a = [12 ,23,43,55]
i = 0
s=0
b=[]
while i<len(a):
  dig = a[i]%10
  c = (a[i]//10)
  s=dig+c
  i+=1
  #print(s,end=", ")
  b.append(s)
print(b)


ITERATE BOTH LIST TOGETHER ::
a = [12,32,45,57,89,90]
b = ["Hope","nav","pogo","vaishali","abhi","gullu"]
i = 0
while i<len(a):
  print(str(a[i]),b[i])
  i+=1


list1=[]
i = 1
b = int(input("enter how many times you want list: "))
while i<=b:
  a = input("enter a num: ")
  list1.append(a)
  i+=1
print(list1)
j=0
count=0
count1 =0
sum=0
sum1 = 0
while j<len(list1):
  if int(list1[j])%2==0:
    count+=1
    sum+=int(list1[j])
    avg = sum/len(list1)
    print(list1[j],"even")
  else:
    count1+=1
    sum1+=int(list1[j])
    avg1 = sum1/len(list1)
    print(list1[j],"odd")
  j+=1
print(count,"count of even num")
print(count1,"count of odd")
print(sum,"sum of even num")
print(sum1,"sum of odd")
print(avg,"avg of even num")
print(avg1,"avg of odd")




kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
print(len(kitna_paisa_hai))
i = 0
count=0
count1=0
count2=0
while i<len(kitna_paisa_hai):
  if len(str(kitna_paisa_hai[i]))>=8:
    count+=1
    #print(count,"crorepati")
    print("crorepati")
  elif len(str(kitna_paisa_hai[i]))>5 and len(str(kitna_paisa_hai[i]))<8:
    count1+=1
    #print(count1,"lakhpati")
    print("lakhpati")
  elif len(str(kitna_paisa_hai[i]))<=5:
    count2+=1
    #print(count2,"dilwale")
    print("dilwale")
  i+=1
print(count,"crorepati")
print(count1,"lakhpati")
