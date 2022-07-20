#Test
#Find smallest element in a list.
def smlstVal(lst):
    myVal = lst[0]
    for i in lst:
        if i < myVal:
            myVal=i
    return myVal
    
list1=[6,8,9,3,2,1,5]
miniVal=smlstVal(list1)
print(miniVal)


#Find largest element in a list.
def grtstVal(lst):
    val = lst[0]
    for i in lst:
        if i > val:
            val = i
    return val
    
mylst=[5,7,85,48,93,28]
result=grtstVal(mylst)
print(result)



mylst.sort()
print("smallest val if this element", *mylst[:1])

mylst.sort()
print("largest val if this element", mylst[-1])




#Print list elements with its index.
def myfun(lst):
    for i in range(len(lst)):
        print(i , end = " ")
        print(lst[i])
mylst=[2,3,4,5,6,7]
myfun(mylst)



#Write a function to return the multiplication of list elements.
def multiplicationwithlst(lst):
    multi = 1
    for i in range(len(lst)):
        multi = multi * lst[i]
    return multi
    
list1=[3,4,5,6]
result=multiplicationwithlst(list1)
print(result)



#Write a function to multiply each element by 2.
def myfun(list1):
    for i in list1:
        i = i * 2
        print(i)
    
lst=[3,4,5,6]
myfun(lst)
    

#Write a function to return the sum of all items in the list.
def mysum(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum
    #for i in range(len(lst)):
        #sum = sum + lst[i]
   # return sum
   
mylst=[2,3,4,5,6,7]
myresult=mysum(mylst)
print(myresult)


# Write a function to subtract -1 in each elements of the list.
def myfun(lst):
    for i in lst:
        i = i - 1
        print(i)
    
list1=[2,3,4,5]
myfun(list1)
print(x)




# Print list elements with its index.
def myfunc(lst,val):
    for i in range(len(lst)):
        if lst[i] == val:
            print(i,end = " ")
            print(lst[i])
        
lst1=[2,3,4]
myfunc(lst1,3)


# Find even in list.
'''def Evenfun(lst):
    for i in lst:
        if i % 2 == 0:
            x = i
            
    return x
lst1=[4,8,3,9,10,87,24]    
Evenvl=Evenfun(lst1)
print(Evenvl)'''
            

        
'''def myevnfun():       
    list1=[4,20,48,3,5,8,9,20]
    for i in list1:
        if i % 2==0:
            print(i,end = " ")
        
myevnfun()'''


'''def myfun():
    list1=[4,3,2,8,10,29,28]
    n = 0

    while n < len(list1):
        if list1[n]%2==0:
            print(list1[n],end=" ")
        
        n += 1
myfun()'''


def rngevnfun():
    start=int(input("enter starting number"))
    end=int(input("enter last number"))
    
    for i in range(start, end + 1):
        
        if i % 2 == 0:
            print(i, end = " ")
            
rngevnfun()

'''lst=[3,4,5,8,9,28,43]
lst.sort()
print("largest val", lst[-2])



def scndLval(lst,n):
    mx = lst[0]
    for i in lst:
        if i > mx:
            mx = i
    return mx

lst1=[4,8,4,9,2,10,30,43]    
nthLval=scndLval(lst1,2)
print(nthLval[-n])



# nth largest element 
lst=[3,4,7,29,49,39,28]
n = 3

lst.sort()
print("nth largstval",lst[-n])'''



def myfun(lst,n):
    lst.sort()
    return lst[-n:]

lst1=[3,5,8,7,9]
x=myfun(lst1,3)
print(x)


# Write a function which takes three arguments index1, index2 and list.
# You need to swap the values in index1 and index2 of list.
def swpfun(lst):
    x=len(lst)
    temp=lst[0]
    lst[0] = lst[x - 1]
    lst[x - 1] = temp
    
lst1=[5,10,8,90,65,3]
swpfun(lst1)
print(lst1)




def sumFun(lst):
    sum = 0
    for i in lst:
        sum = sum + i
        
    return sum
        
        
lst1=[4,6,8,29,89]
val=sumFun(lst1)
print(val)


def myfun(lst):
    newlst=[]
    for i in lst:
        newlst.append(i*2)
        
    for j in range(len(lst)):
        lst[j] = 2*lst[j]
    
    return newlst
    
mylst=[4,5,3,2,6]
newval=myfun(mylst)
print(newval)
print(mylst)

#Write a program for linear search.
def Searchelement(lst,number):
    for i in lst:
        if i == number:
            return True
    return False

lst=[5,6,9,39,20]
srchval=Searchelement(lst,10)
print(srchval)


# Write a function which will take two arguments - "mylist" and "number".
# The function will return a new list which contains only values which are grater than "number" in "mylist".
def graterVal(lst,val):
    newLst = []
    for i in lst:
        if i > val:
            newLst.append(i)
    return newLst
            
Newlst=graterVal(lst,10)
print(Newlst)


def max(a,b):
    if a == b:
        return "same" 
    elif a>b:
        return a
    else:
        return b


def minList(lst):
    minValue = lst[0]
    
    for i in lst:
        if i < minValue:
            minValue = i
            
    return minValue
    
list1=[5,6,7,3,6,10]
print(minList(list1))
smallestValue = minList(list1)

print(smallestValue)
        
    
#Class to show inheritance and polymorphism.
class Parent1:
    name = "Base"
    def __init__(self):
        self.name1 = "BaseClass"
    def dog(self):
        print(self.name1)
        
class Parent2:
    def cow(self):
        print("this is a cow")
    
class Derived(Parent1,Parent2):
    def cat(self):
        print("this is a cat")
        
d1=Derived()
d1.dog()
d1.cow()
d1.cat()

pObj = Parent1()
print(pObj.name)
print(pObj.name1)
pObj.dog()
 



mylist=[3,2,5,4,8,9,1]
for i in range(len(mylist)):
    for j in range(0,len(mylist)-i-1):
        if mylist[j] > mylist[j+1]:
            temp = mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
print(mylist)

print("%%%%%%%%%%%%%$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%")


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-i -1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst
                
    print("my sorted list")
list1=[2,1,5,3,7,6,9,1,92,45,12,34]
x=bubble_sort(list1)
print(x)


print("%%%%%%%%%%%%%$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%")



size=int(input("enter the size of list"))
mylst=[]
for i in range(size):
    lstval=int(input("enter the number"))
    mylst.append(lstval)
    
    
for i in range(size):
    for j in range(0,size-i-1):
        if mylst[j]>mylst[j+1]:
            temp=mylst[j]
            mylst[j]=mylst[j+1]
            mylst[j+1]=temp
print("my sorted list are")
print(mylst)



