marks = {"harry": 34, "jack": 45, "lily": 94}   # dictionary

print(marks.keys())    
# dict_keys(['harry', 'jack', 'lily'])
# Reason: returns all keys

print(marks.values())  
# dict_values([34, 45, 94])
# Reason: returns all values

# marks.clear()
# would remove all elements → {}

marks.pop("lily")      
# removes key "lily" with its value
# Reason: pop(key) deletes that key-value pair

print(marks)           
# {'harry': 34, 'jack': 45}