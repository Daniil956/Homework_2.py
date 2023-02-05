S = int(input("Enter number S: "))
P = int(input("Enter number P: "))

x = int(S-((S**2-4*P)**0.5))//2
y = int(S+((S**2-4*P)**0.5))//2
print(x, y)
