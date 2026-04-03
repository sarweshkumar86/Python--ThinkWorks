marks = [5, 2, 21, 5, 7]          # original list
extra_marks = [53, 23, 32]        # another list

print(marks)  
# Output: [5, 2, 21, 5, 7] → original list

# marks.append(63)
# This adds 63 at the end of list
# Output would be: [5, 2, 21, 5, 7, 63]

# marks.pop()
# This removes last element
# Output would be: [5, 2, 21, 5]

marks.extend(extra_marks)  
# extend adds all elements of extra_marks into marks
# Reason:
# extend() takes each element and adds one by one
# same as: marks = marks + extra_marks

print(marks)
# Output: [5, 2, 21, 5, 7, 53, 23, 32]