def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print("time is up")


def countdown_recursive(start=10):
    if(countdown_recursive.isfirst = True):
        if (start > 0):
            countdown_recursive.count = start
            countdown_recursive.isfirst = False
            print(start)
            continue
        else:
            print('time is up')
    if countdown_recursive.isfirst = False:
        countdown_recursive.count -= 1
        if(countdown_recursive.count > 1):
            print(countdown_recursive.count)
            continue
        else:
            print('time is up')

    else:
        countdown_recursive.isfirst = True