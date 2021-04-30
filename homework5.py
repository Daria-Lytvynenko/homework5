if __name__ == '__main__':
#Task1. The greatest number
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers
    import random
    number_list=[]
    i=0
    while i<10:
        x = random.randint(0, 1000000)
        number_list.append(x)
        i+=1
    print(number_list)
    print(max(number_list))
#Task 2. Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial
# lists without any duplicates. Constraints: use only while loop and random module to generate numbers
    number_list1=[]
    number_list2=[]
    i=0
    while i<10:
        x1= random.randint(1, 10)
        x2=random.randint(1, 10)
        number_list1.append(x1)
        number_list2.append(x2)
        i+=1
    print(number_list1, number_list2)
    number_list3=list(set(number_list1).intersection(set(number_list2)))
    print(number_list3)
#Task 3. Extracting numbers. Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list. Constraint: use only while loop for iteration
    number_list4 = [7]
    i = 7
    while i < 100:
        i += 7
        if i%5==0:
            i+=7
        if i > 100:
            break
        number_list4.append(i)
    print(number_list4)