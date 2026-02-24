#conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==
#<
'''a=2
b=4
if a<b:
    print("true")'''
#>
'''a=2
b=4
if a>b:
    print("true")'''
#>=
'''a=2
b=4
if a>=b:
    print("true")'''
#<=
'''a=2
b=4
if a<=b:
    print("true")'''
#!=
'''a=2
b=4
if a!=b:
    print("true")'''
#a==b
'''a=2
b=4
if a==b:
    print("true")'''

'''a=4
b=4
if a==b:
    print("true")'''
#a>b
'''a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("greater")'''

#a>40
'''a=int(input("a value"))
if a>40:
    print("greater")'''

#string only (==)
'''a="python"
if a=="python":
    print("true")'''

'''a=input("name")
if a=="pooja":
    print("valid")'''

#if-condition by using logical operators
#and,or,not

#and
'''a=5
b=9
if a<b and a>b:
    print("less")'''


'''a=7
b=11
if a<=b and b>=a:
    print("less")'''
#or
'''a=5
b=6
if a!=b or b<=a:
    print("true")'''

'''a=5
b=6
if a<=b or b<=a:
    print("true")'''

'''a=20
b=10
if a<b or b>a:
    print("true")'''

#not
'''a=4
b=8
if not a<b:
    print("true")'''


'''a=4
b=8
if not a>b:
    print("true")'''
#runtime

'''a=int(input("a value is"))
b=int(input("b value is"))
if a<b or b>a:
    print("Correct")'''

#if-condition by using identify operators
#is, is not

#int
'''a=7
if type(a) is not int:
    print("it is int")'''

'''a=7
if type(a) is int:
    print("it is int")'''

#float

'''a=7.7
if type(a) is float:
    print("it is float")'''

'''a=7.7
if type(a) is not float:
    print("it is float")'''
#string
'''a="simha"
if type(a) is str:
    print("it is string")'''

'''a="simha"
if type(a) is not str:
    print("it is string")'''
#complex

'''a=8+28j
if type(a) is complex:
    print("it is complex")'''

'''a=8+28j
if type(a) is not complex:
    print("it is complex")'''
#boolean
'''a=True
if type(a) is bool:
    print("it is bool")'''

'''a=True
if type(a) is not bool:
    print("it is bool")'''
#runtime
'''a=int(input("a value is"))
if type(a) is int:
    print("Yes it is int")'''

'''a=int(input("a value is"))
if type(a) is not int:
    print("Yes it is int")'''
#if-condition by using membership operators
#in,not in
'''a=[2,3,4,5,6,7,8,9,10]
if 2 in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 2 not in a:
    print("true")'''

'''a=int(input("a value in"))
if not a:
    print("yes")'''

'''a=[1,2,3,4,5,6,7,8,9,20]
b=int(input("value"))
if b in a:
    print("the value is",b)'''
#if-else conditions by using comparision operators
'''a=6
b=8
if a<b:
    print("less")'''

'''a=6
b=8
if a>b:
    print("less")
else:
    print("true")'''

'''a=6
b=8
if a<b:
    print("less")
else:
    print("false")'''


'''a=3
b=9
if a!=b:
    print("not equal")
else:
    print("equal")'''


'''a=9
b=3
if a==b:
    print("not equal")
else:
    print("equal")'''
#runtime if else

'''a=int(input())
b=int(input())
if a>b:
    print("trule")
else:
    print("false")'''
#if-else conditions by using logical operators
'''a=6
b=12
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=7
if a!=b or b==a:
    print("equal")
else:
    print("not equal")'''

'''a=9
b=10
if not b>a:
    print("false")
else:
    print("true")'''

'''a=int(input())
b=int(input())
if a>b or b<a:
    print("true")
else:
    print("false")'''
#if-else by identity operators
#is, is not
#string
'''a="python"
if type(a) is str:
    print("yes")
else:
    print("no")'''

'''a="python"
if type(a) is not str:
    print("yes")
else:
    print("no")'''
#int
'''a=22
if type(a) is int:
    print("yes")
else:
    print("no")'''

'''a=22
if type(a) is not int:
    print("yes")
else:
    print("no")'''
#float
'''a=2.2
if type(a) is int:
    print("yes")
else:
    print("no")'''

'''a=2.2
if type(a) is not int:
    print("yes")
else:
    print("no")'''
#complex
'''a=2
if type(a) is complex:
    print("yes")
else:
    print("no")'''

'''a=2+6j
if type(a) is not int:
    print("yes")
else:
    print("no")'''
#boolean
'''a=True
if type(a) is bool:
    print("yes")
else:
    print("no")'''

'''a=False
if type(a) is not bool:
    print("yes")
else:
    print("no")'''
#if-else conditions by using membership operators
#in,not in
'''a=[1,2,3,4,5,6,7]
if 5 in a:
    print("Value is there")
else:
    print("value is not there")'''

'''a=[1,2,3,4,5,6,7]
if not 5 in a:
    print("Value is there")
else:
    print("value is not there")'''

#runtime
'''a=[1,2,3,4,5,6,7]
b=int(input("a value is"))
if b in a:
    print("the value is",b)
else:
    print("false")'''
      
'''a=[1,2,3,4,5,6,7]
b=int(input("a value is"))
if not b in a:
    print("the value is",b)
else:
    print("false")'''
#if-elif-else
'''a=8
b=12
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''
    
'''a=8
b=12
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=8
b=12
if a>b:
    print("less")
elif b==a:
    print("greater")
else:
    print("true")'''

'''a=8
b=12
if a>b:
    print("less")
elif b==a:
    print("greater")
elif a<b:
    print("false")
else:
    print("true")'''
#logical operators
#and, or, not
'''a=8
b=12
if b>a and a>b:
    print("less")
elif b==a or a!=b:
    print("greater")
elif not a<b:
    print("false")
else:
    print("true")'''

'''a=10
b=20
if a>b and a==b:
    print("greater")
elif a>=b or b>a:
    print("lesser")
elif not a!=b:
    print("greater")
else:
    print("lesser")'''
#membership operators
'''a=[12,20,30,40,50]
if 50 in a:
    print("greater")
elif 20 not in a:
    print("true")
else:
    print("lesser")'''








    


























