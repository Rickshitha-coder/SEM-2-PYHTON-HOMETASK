'''Date : 17-2-25
Write a function that takes two dictionaries and merges them into one'''
def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1
d1={"Name":"Rickshi","Age":18,"Blood-Group":"O-ve"}
d2={"Gender":"Female","Nationaly":"Indian","Qualification":"BSC CSC (AI)"}
d3 = merge_dicts(d1, d2)
print(d3)

'''Write a function that takes two lists and returns a dictionary with common elements 
as keys and their counts as values.'''
def common_elements(list1, list2):
    l1 = set(list1)
    l2 = set(list2)
    common = l1 & l2
    return {element: list1.count(element) + list2.count(element) for element in common}


list1 = list(map(int,input("Enter the elements in the list:").split()))
list2 = list(map(int,input("Enter the elements in the list:").split()))
print(common_elements(list1, list2))

'''Write a function that takes a list of (key, value) tuples and converts it into a 
dictionary'''
def tuples_to_dict(tuple_list):
    result = {}
    num_tuples = int(input("Enter the number of tuples: "))
    
    for i in range(num_tuples):
        key = input(f"Enter key for pair {i+1}: ")
        value = input(f"Enter value for pair {i+1}: ")
        tuple_list.append((key, value))
    
    for tuple in tuple_list:
        result[tuple[0]] = tuple[1]
    return result

tuple_list = []
print(tuples_to_dict(tuple_list))

