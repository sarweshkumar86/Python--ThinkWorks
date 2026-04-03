marks = {"harry": 34, "jack": 45, "lily": 94}   # dictionary (key:value)

# print(marks, type(marks))

print(marks["lily"])   
# 94 → access value using key "lily"

marks["harry"] = 3     
# update value of key "harry"
# Reason:
# dictionary allows modification (mutable)

print(marks)           
# {'harry': 3, 'jack': 45, 'lily': 94}