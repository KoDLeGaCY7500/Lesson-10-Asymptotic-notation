# def printno(n):
#     iteration=0
#     print("The total number entered by the user is ",n)

#     iteration+=1
#     print("Total number of iterations done by the computer",iteration)

# printno(10)
# printno(200000)

#Activity 2

# def ontime(n):
#     iteration=0
#     for i in range(1,n+1):
#         iteration+=1
#     print("when n is",n,"iteration=",iteration)

# ontime(10)
# ontime(1200)

#Activity 03

def test(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iteration+=1

        print("")
    print("when n is",n,"iteration is ",iteration)
test(5)