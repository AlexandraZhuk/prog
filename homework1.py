a=int(input())
b=int(input())
c=int(input())
if a%b==c:
    print ("a даёт остаток с при делении на b")
elif a*c+b==0:
    print ("c является решением линейного уравнения ax+b=0")
else:
    print ("свойства не выполняются")
