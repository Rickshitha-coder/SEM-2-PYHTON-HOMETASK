'''Date: 19-12-24 Task : Code
Seven different symbols represent Roman numerals with the following values:
Symbol Value
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
Roman numerals are formed by appending the conversions of decimal place 
values from highest to lowest. Converting a decimal place value into a Roman 
numeral has the following rules:
If the value does not start with 4 or 9, select the symbol of the maximal value 
that can be subtracted from the input, append that symbol to the result, subtract 
its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol 
subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV 
and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 
4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to 
represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple 
times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral'''
roman =[ 
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
n=int(input("Enter the number to convert into a roman number"))
ans=""
for val,letter in roman:
    while n>=val:  #493>=400 93>=90 3>=1 2>=1 1>=1
        ans+=letter # CD CDXC CDXCI CDXCII CDXCIII
        n-=val #493-400=93  93-90=3 3-1=2  2-1=1 1-1=0
print("The roman for the given integer is:",ans)



'''Roman to Number'''
roman =[ 
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
roman_int=input("Enter the roman number")#CXX
number=0
i=0
while i<len(roman_int):#0<3
    for value,letter in roman:
        if roman_int[i:i+len(letter)]==letter: #roman_int[0:1]==letter
            number+=value #0+100=100 100+10=110 110+10=120
            i+=len(letter)#0+1=1 1+1=2 2+1=3
            break
print(number)
