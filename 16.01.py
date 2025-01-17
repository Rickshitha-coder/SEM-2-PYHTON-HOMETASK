'''DATE:17.01.2025
1.Sum of all items in a dictionary'''
my_dict = {'a':1,'b': 2,'c': 3}
total_sum = sum(my_dict.values())
print(total_sum)
'''2.Construct a pattern using a nested loop
Pattern: 
1
2 2
3 3 3
4 4 4 4'''

n=int(input())
for i in range(1, n+1):
    for j in range(i):
        print(i,end="")
    print()



