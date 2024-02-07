def generate_squares(N):
    for i in range(1, N + 1):
        yield i ** 2

squares_generator = generate_squares(int(input()))

for square in squares_generator:
    print(square,end=" ")
print()



def even(n):
    for i in range(0,n+1):
        if(i%2==0):
            yield i

n=int(input())
generator=even(n)

for i in generator:
    print(i,end="")
    if i != n and i + 2 <= n:
            print(",", end=" ")
print()



def repeat(n):
    for i in range(0,n+1):
        if(i%3==0 and i%4==0):
            yield i

generator = repeat(int(input()))

for i in generator:
    print(i,end=" ")
print()



def square(a,b):
    for i in range(a,b+1):
        yield i**2

squares = square(int(input()),int(input()))

for i in squares:
    print(i,end=" ")
print()




def numbers(n):
    for i in range(0,n+1):
        yield i

generator = numbers(int(input()))

for i in generator:
    print(i,end=" ")
print()