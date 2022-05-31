# Trying yield

def return_squeard(min, max):
    for i in range(min, max):
        yield i**2

result = return_squeard(1, 5)

print(next(result))
print(next(result))
print(next(result))

