# this countdown function.

def countdown(x):
    if x == 0:
        print("Zeroooooo!")
        return
    else:
        print(x,": ")
        countdown(x-1)

# choose number
countdown(20)
