"""
Problem : print sub strings 
"""

def subStrings(n,arr):
    
    for i in range(n):
        sub = []
        for j in range(i,n):
            sub.append(arr[j])
        print(sub);
        
        
        
subStrings(3,[1,2,3])