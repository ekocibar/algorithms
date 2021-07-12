"""
https://www.hackerrank.com/challenges/fraudulent-activity-notifications
"""


def activityNotifications(expenditure, d):
    freq = {}
    notify=0
    def find(idx):
        total_count = 0
        for i in range(201):
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i
    for i in range(len(expenditure)-1):
        if expenditure[i] in freq:
            freq[expenditure[i]]+=1
        else:
            freq[expenditure[i]]=1
        #print(f"i: {i},val: {expenditure[i]}, freq: {freq}")
        if i>=d-1:
            if d%2 ==0:
                median = (find(d//2)+find(d//2+1))/2
            else:
                median = find(d/2)
            #print("median: ",median)
            if expenditure[i+1]>= (median*2) :
                notify +=1
                print("notify: ",notify)
            #remove the previous element from dictionary
            freq[expenditure[i-d+1]]-=1

    return notify

# COSTLY SOLUTION
from statistics import median

def activityNotifications2(expenditure, d):
    count = 0
    if d > len(expenditure):
        return 0

    for i, transaction in enumerate(expenditure):
        if i < d:
            continue
        current_median = median(expenditure[i-d:i])
        if transaction >= 2*current_median:
            count += 1

    return count