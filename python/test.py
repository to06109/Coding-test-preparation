def d(n):
    
    con = 0
    s = str(n)
        
    for a in s:
            
        con += int(a)

    return n+con

original_list  = list(range(1, 10001))
c_list = list()

for z in range (1, 10001):
    c_list.append(d(z))

result = set(original_list) - set(c_list)

for r in sorted(result):
    print(r)