# #question 1
# def show():
#     a=int(input("Enter radius="))
#     b=3.14*a*a
#     print("Area of circle =",b)
# show()

## question 2
# def perfect():
#   print("List of perfect numbers from 1 to 1000-")
#   for a in range(1, 1001):
#     S=0
#     for b in range(1,a):
#         if(a%b==0):
#             S=S+b
#     if(S==a):
#         print(a)
# perfect()


# #question 3
# def show1(i):
#     n=12
#     if(i==11):
#         return
#     else:
#         print(n*i)
#         show1(i+1)
# i=1
# print("Table of 12-")
# show1(i)

# #question 4
# def show2(a,b):
#     if(b==0):
#         return 1
#     else:
#         A=a*show2(a,b-1)
#         return (A)
# a=int(input("Enter number="))
# b=int(input("Enter power="))
# P=show2(a,b)
# print(P)

#question 5
A={}
def factt(a):
    if(a==1):
        return 1
    else:
        F=a*factt(a-1)
        return(F)
a = int(input("Enter number="))
b=factt(a)
A[a]=b
print("Dictionary -",A)

