import random
# def solution(users, emoticons):
#     plus = 0 # 이모티콘 플러스 가입자
#     price = 0 # 판매액
#     arr = [10, 20, 30, 40] # 할인율
#     s = []

#     def final(s):
#         print(s)
#         nonlocal plus, price

#         temp_plus = 0
#         temp_price = 0
#         for user in users:
#             # print("user", user)
#             total_price = 0
#             user_rate, user_price = user
    
#             for idx in range(len(emoticons)):
#                 if s[idx] >= user_rate: # 이모티콘 구매
#                     total_price += int(emoticons[idx] * (1 - round(s[idx] / 100, 1)))
#             if total_price >= user_price: # 플러스 서비스 가입
#                 temp_plus += 1
#             else:
#                 temp_price += total_price
#         # print("1-", total_price, temp_plus, temp_price)
#         if temp_plus > plus:
#             plus = temp_plus
#             price = temp_price
#         elif temp_plus == plus and temp_price > price:
#             price = temp_price  
#         print("2-", plus, price)    

#     def back():
#         if len(s)==len(emoticons):
#             final(s)
#             return
        
#         for i in range(4):
#             s.append(arr[i])
#             back()
#             s.pop()
#     back()
#     answer = [plus, price]
#     return answer

# 테스트 함수 작성


# for z in range(50):
#     users = []
#     for i in range(2):
#         rate = random.randrange(1, 40)
#         price = random.randrange(100, 10000, 100)
#         users.append([rate, price])

#     emoticons = []
#     for _ in range(3):
#         price2 = random.randrange(100, 10000, 100)
#         emoticons.append(price2)
#     print(users, emoticons)
#     print(solution(users, emoticons))
#     print("-----------------------------------------")

# users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
# emoticons = [1300, 1500, 1600, 4900]
# print(solution(users, emoticons))


print(int(1000 * (1 - round(30 / 100, 1))))