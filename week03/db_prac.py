from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#퀴즈1
matrix = db.movies.find_one({'title': '매트릭스'})
#print(matrix['star'])

#퀴즈2
target_star=matrix['star']
print(target_star)
same_stars = list(db.movies.find({'star': target_star}, {'_id': False}))
for s in same_stars:
    print(s['title'])

#퀴즈3
#db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '9.39'}})


# # 한 개 찾기 - 예시
# user = db.users.find_one({'name': 'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age': 21}, {'_id': False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name': 'bobby'})

