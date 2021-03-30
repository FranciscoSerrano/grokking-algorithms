# count down
# > 3...2...1

# def countdown(i):  <-- this runs forever
#     print(i)
#     countdown(i-1)

# countdown(5)

def countdown(i):
    print(i)
    if  i <= 0: # <-- base case
        return
    else: # <-- recursive case
        countdown(i-1)

countdown(5)

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print(fact(5))