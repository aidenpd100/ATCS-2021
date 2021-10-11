names = ['John', 'Sarah', 'Dave', 'Joe']

def crowd_test():
    if len(names) > 3:
        print('The room is crowded')

crowd_test()

names.remove('John')
names.remove('Dave')
crowd_test()