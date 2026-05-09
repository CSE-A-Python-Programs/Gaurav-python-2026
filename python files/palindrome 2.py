s = "gag"

if all(s[i] == s[-i-1] for i in range(len(s)//2)):
    print("Yes")
else:
    print("No")