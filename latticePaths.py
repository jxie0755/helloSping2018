def latticePath(x,y,n):
    if x==n and y==n:
        return 1
    idx = 0
    if x<n:
        idx = idx + latticePath(x+1,y,n)
    if y<n:
        idx = idx + latticePath(x,y+1,n)
    return idx

print(latticePath(0,0,10))

