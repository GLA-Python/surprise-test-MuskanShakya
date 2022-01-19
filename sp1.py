def expanding():
    a=list(map(int,input().split()))
    ls=[]
    for i in range (len(a)-1):
        if a[i+1]>a[i]:
            c=a[i+1]-a[i]
        else:
            c=a[i]-a[i+1]
        ls.append(c)
    if ls==sorted(ls):
        return True
    else:
        return False
out=expanding()
print(out)
