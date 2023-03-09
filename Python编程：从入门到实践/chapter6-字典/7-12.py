dict1 = {"first_name":"jack","last_name":"smith","age":18,"city":"Beijing"}
dict2 = {"first_name":"tom","last_name":"mack","age":26,"city":"NewYork"}
dict3 = {"first_name":"ray","last_name":"mary","age":23,"city":"Shanghai"}
list1 = [dict1,dict2,dict3]
for i in list1:
    print(i)


pet1 = {"breed":"dog","master":"jack"}
pet2 = {"breed":"cat","master":"tom"}
pet3 = {"breed":"dog","master":"ray"}
list2 = [pet1,pet2,pet3]
for i in list2:
    print(i)


favorite_places = {"mack":"Beijing","tom":"Shanghai","ray":"NewYork,Chengdu"}
for x in favorite_places.items():
    print(x)


#6-10  相似


cities = {"Beijing":{"country":"China","population":"100","fact":"big"},
          "Shanghai":{"country":"China","population":"200","fact":"huge"},
          "Chengdu":{"country":"China","population":"30","fact":"hot"}}
for i in cities.items():
    print(i)