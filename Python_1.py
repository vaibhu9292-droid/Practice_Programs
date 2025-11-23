# Loops in python

#  While Loop

count = 1 #iterator

while count<=5:
    print("Hello World",count)
    count +=1

print(count)

# Question - 1
n = int(input("Enter number :"))
i = 1
while i<=10:
    
    print(n*i)
    i+=1

# Question-2

# Traverse
nums = [1,4,9,16,25,36,49,64,81,100]

i=0
while i<len(nums):
    print(nums[i])
    i+=1

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i<len(nums):
    if nums[i]==x:
        print("Found at idx",i)
    i+=1
