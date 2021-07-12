"""
https://www.hackerrank.com/challenges/frequency-queries
"""

def freqQuery(queries):
    arr={}
    res=[]
    for i,j in queries:
        if i==1:
            if j in arr:
                arr[j]+=1
            else:
                arr[j]=1
        elif i==2:
            if j in arr:
                if arr[j]>0:
                    arr[j]-=1
        elif i==3:
            if j in arr.values():
                res.append(1)
            else:
                res.append(0)
    return res