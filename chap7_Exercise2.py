# input data in dictionary by user 
user={}
name=input("What is your name?: ")
age=int(input("What is your age?: "))
fav_movies=input("Favourite movies are separated by , : ").split(',')
fav_songs=input("Favourite songs are separated by , : ").split(',')
user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs
# print(user)
for key,value in user.items():
    print(f"{key} : {value}")