#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100

#make an empty total var
total = 0
#the range is from [0, 101) and moving 2 at a time
for num in range(0, 101, 2):
    #print(num)
    total += num
print(total)
