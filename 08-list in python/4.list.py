# Q. Write a Python program to display part of a list using slicing.


nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # [20, 30, 40] → index 1 to 3
print(nums[:3])    # [10, 20, 30] → start default 0
print(nums[2:])    # [30, 40, 50] → end default last

print('............................................')

# Q. Write a Python program to reverse a list using slicing.

nums = [10, 20, 30, 40]

print(nums[::-1])   # [40, 30, 20, 10]


print('............................................')

# Q. Write a Python program to sort a list.

nums = [40, 10, 30, 20]

nums.sort()

print(nums)   # [10, 20, 30, 40]

print('............................................')


# Q. Write a Python program to reverse a list.
nums = [10, 20, 30]

nums.reverse()

print(nums)   # [30, 20, 10]




# Write a Python program to add element in list.
nums = [10, 20]

nums.append(30)

print(nums)   # [10, 20, 30]


# Q. Write a Python program to insert element at specific position.
nums = [10, 30]

nums.insert(1, 20)

print(nums)   # [10, 20, 30]