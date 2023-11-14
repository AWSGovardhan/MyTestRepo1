# print("name of the module is {}".format(__name__))

if __name__ == '__main__':
    print('Running directly')
else:
    print("Running indirectly")
    print("name of the module is {}".format(__name__))