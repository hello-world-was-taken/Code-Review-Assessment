count = 0

def multiply(x, y):
    return x * y

def increment_count():
    global count
    count += 1

increment_count()
print(count)