def longest_unique_students(students):
    max_len=0
    for i in range(len(students)):
        visited_stu=set()
        count=0
        for j in range(i,len(students)):
            if students[j] in visited_stu:
                break
            visited_stu.add(students[j])
            
            count+=1
        max_len=max(max_len,count)
    return max_len
students=[1,2,3,5,6,7,7]

print("1st question",longest_unique_students(students))

"""2222def longest_max_sum(discounts):
    curr=0
    maximum=0
    for i in range(len(discounts)):
        curr=max(curr+discounts[i],discounts[i])
        maximum=max(curr,maximum)
    return maximum
discounts=[-1,2,3,4,-2]
print(longest_max_sum(discounts))"""

"""333333def trapping_rain(water):
    left=0
    right=len(water)-1
    
    leftmax=0
    rightmax=0
    res=0
    
    while left<right:
        if water[left]<water[right]:
            if water[left]>=leftmax:
                leftmax=water[left]
            else:
                res+=leftmax-water[left]
            left+=1
        else:
            if water[right]>=rightmax:
                rightmax=water[right]
            else:
                res+=rightmax-water[right]
            right-=1  
    return res
water=[4,2,0,3,2,5]
print(trapping_rain(water))"""



"""def performance(scores):
    curr=0
    maximum=0
    for num in scores:
        curr=max(curr+num,num)
        maximum=max(curr,maximum)
    return maximum
scores=[4,-2,1,0,5,-4]
print(performance(scores))"""

"""def product(scores):
    maximum=-29334343
    for i in range(len(scores)):
        prod=1
        for j in range(i,len(scores)):
            prod*=scores[j]
            maximum=max(maximum,prod)
    return maximum
scores=[0,-2,4,3,7]
print(product(scores))"""


"""def longest_unique(ids):
    
    maxi=0
    for i in range(len(ids)):
        visited_set=set()
        count=0
        for num in ids:
            if num in visited_set:
                break
            visited_set.add(num)
            count+=1
        maxi=max(count,maxi)
    return maxi
ids=[1,2,4,2,1,5]
print(longest_unique(ids))"""

"""def specific_target(nums,k):
    count=0
    for i in range(len(nums)):
        tot=0
        for j in range(i,len(nums)):
            tot+=nums[j]
            if tot==k:
                count+=1
    return count
nums=[1,2,3,4,-1,-2]
k=9
print(specific_target(nums,k))"""

"""def hospital(intervals):
    intervals.sort()
    merged=[intervals[0]]
    for current in intervals[1:]:
        last=merged[-1]
        if current[0]<=last[1]:
            last[1]=max(last[1],current[1])
        else:
            merged.append(current)
    return merged
intervals=[[1,2],[2,5],[4,6],[7,8]]
print(hospital(intervals))
"""































                
        
    
    
    
    
    
    
    
    
    
    