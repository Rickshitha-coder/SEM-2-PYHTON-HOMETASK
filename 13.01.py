'''There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its
next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around
the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is
guaranteed to be unique.
Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.'''


n=int(input("Enter the number of gas stations"))
gas_l=[]
cost_l=[]
for i in range(n):
    gas=int(input("Enter the amount of gas "))
    cost=int(input("Enter the cost for each stations"))
    gas_l.append(gas)
    cost_l.append(cost)
print(gas_l)
print(cost_l)
start=0
s=True
s_i=0
for i in range(len(gas_l)):
    if gas_l[i]>cost_l[i]:
        start+=gas_l[i]
        s_i=i
        s=True
    else:
        s=False
if not s:
    print("No start available")
    

if s:
    def tank():
        global s_i
        tank=start#4
        while s_i<len(gas_l)-2:
            
            tank=tank-cost_l[s_i]+gas_l[s_i+1]#4-1+5=8#8-2+
            s_i=s_i+1
        else:
            tank=tank-cost_l[s_i]+gas_l[s_i+1]#4-1+5=8#8-2+
            s_i=n-s_i+1
            return s_i
    ans=tank()
    print(ans)


'''There are n children standing in a line. Each child is assigned a rating value given in the integer array
ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.'''

n=int(input("Enter the number of students:"))
s=[]
for i in range(n):
    ratings=int(input("Enter the ratings:"))
    s.append(ratings)
can=[1]*n
for i in range(1,len(s)):
    if s[i]>s[i-1]:
        can[i]=can[i-1]+1
for i in reversed(range(len(s)-1)):
    if s[i]>s[i+1]:
        can[i]=can[i+1]+1
        
        
print(sum(can))
