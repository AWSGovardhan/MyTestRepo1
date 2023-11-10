def FontDeco(fn):
    def selectFont():
        print("font selected!")
    return selectFont

def ImageDeco(fn):
    def selectImage():
        print("image selected")
    return selectImage

# @FontDeco
# @ImageDeco
# def normFn():
#     print('normal fn called')

@ImageDeco #First assigned decorator only will be applied
@FontDeco
def normFn():
    print('normal fn called')


normFn()