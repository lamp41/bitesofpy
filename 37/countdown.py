def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    if (start > 0):
        print(start)
        start = start - 1
        return countdown_recursive(start)
    else:
        print('time is up')
        return 0
                
countdown_recursive(4)