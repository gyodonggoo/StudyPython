dict_a = {
    "name" : "어벤저스 엔드게임",
    "type" : "히어로 무비",
    "cast" : ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"],
    "director" : ["안소니 루소", "조 루소"],
    "release" : 2018
}

print(dict_a)
print(dict_a["director"][1])

dict_a["type"] = "장르 변경"
dict_a["cameo"] = "스탠 리"

print(dict_a)

del dict_a["release"]
print(dict_a)

# print(dict_a["release"]) # 에러

key = "cast"
if key in dict_a:
    print("cast", dict_a[key])
else:
    print("cast 없음")