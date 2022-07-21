import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))

    print('The search results for the given file extensions are :')
    for name in result:
        print(name)


file_extension = input('Enter the extension of file you are looking to search :')
Dir_Path = input('Enter the dir path you would like to search the file :')
find(file_extension, Dir_Path)
