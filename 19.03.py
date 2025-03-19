'''PYTHON PATTERN PROGRAM
                         1      2      3      4  
                   8      7      6      5  
          9     10     11     12  
16     15     14     13  ''''


pattern = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 3, 0, 4],
    [0, 0, 0, 0, 0, 0, 8, 0, 7, 0, 6, 0, 5],
    [0, 0, 0, 9, 0, 10, 0, 11, 0, 12],
    [16, 0, 15, 0, 14, 0, 13]
]
for row in pattern:
    for zero in row:
        if zero== 0:
            print("   ", end="")  
        else:
            print(f"{zero:2} ", end=" ") 
    print()  
