def add_permission(val, permission):
    val = val | (1<<permission)
    return val

def remove_permission(val, permission):
    val = val & ~(1<<permission)
    return val

initial = 0

# 001 for read
# 011 for write
# 111 for share
initial = add_permission(initial, 0) ## add read permission
print(f"added read permission {bin(initial)}")

initial = add_permission(initial, 1) ## add write permission
print(f"added read permission {bin(initial)}")

initial = add_permission(initial, 2) ## add share permission
print(f"added read permission {bin(initial)}")

initial = remove_permission(initial, 0) ## remove read permission
print(f"remove read permission {bin(initial)}")

initial = remove_permission(initial, 1) ## remove write permission
print(f"remove read permission {bin(initial)}")

initial = remove_permission(initial, 2) ## remove share permission
print(f"remove read permission {bin(initial)}")