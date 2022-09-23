def solution(cacheSize, cities):
    cache = []
    time = 0
    # 캐시사이즈 0일 때 예외처리
    if cacheSize == 0:
        return 5 * len(cities)
    
    for i in range(len(cities)):
        city = cities[i].lower() # 소문자로 바꾸기?
        if city not in cache: # miss
            if len(cache) == cacheSize: 
                # 캐시 교체
                cache.pop(0)
                cache.append(city)
            else:
                cache.append(city)
            time += 5
        else: # hit
            # 순서 맨 뒤로 보내주기(lru니까!)
            temp = cache.index(city)
            cache.append(cache.pop(temp))
            time += 1
        
    return time