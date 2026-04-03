a = (3, 2, 22, 13)   # tuple (immutable → cannot change)

print(a)        # (3, 2, 22, 13)

print(a[2])     # 22 → index starts from 0

a[3] = 32       # ❌ Error → tuple does not support item assignment
                # Reason:
                # tuple is immutable → once created, values cannot be changed

b = (3,)        # single element tuple
                # Reason:
                # comma is mandatory, otherwise it becomes int
                # (3)  → number  
                # (3,) → tuple