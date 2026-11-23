def number_valid(test):
    try:
        test=int(test)
        return True
    except:
        print('This is not a integer, please re-enter')