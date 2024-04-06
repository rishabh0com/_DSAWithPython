a1 = [1, 2, 4, 7, 8, 9]
a2 = [6, 9, 13, 14]
res = []

i, j = 0,0

while (i < len(a1) and j < len(a2)):
    if a1[i] < a2[j]:
        res.append(a1[i])
        i += 1;
        
    
    else:
        res.append(a2[j])
        j += 1;
        
        
while(i < len(a1)):
    res.append(a1[i]);
    i += 1
while(j < len(a2)):
    res.append(a2[j]);
    j += 1
       

print(res)
