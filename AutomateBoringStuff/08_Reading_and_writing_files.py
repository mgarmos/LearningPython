import os


#  Creando rutas dependiendo del sistema operativo
ruta = os.path.join('usr', 'bin', 'spam')
print(ruta)

print(os.path.relpath("./"))

# The Current Working Directory
pathActual = os.getcwd()
print(pathActual)

os.chdir('D:\\')
pathActual = os.getcwd()
print(pathActual)

# Creating New Folders with os.makedirs()
# os.makedirs('D:\\delicious\\walnut\\waffles')



path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path))
# print(os.path.dirname(path))

# Finding File Sizes and Folder Contents
# print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
# print(os.listdir('C:\\Windows\\System32'))

# Total size of a dir
totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
    # totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
# print("totalSize: {}".format(totalSize))

# The File Reading/Writing Process
# Opening Files with the open() Function
def readingFiles(ruta=r'D:\LearningPython\AutomateBoringStuff\FicheroPrueba.txt'):
    helloFile = open(ruta)
    helloContent = helloFile.readlines()
    helloFile.close
    print(helloContent)


def writingFiles(ruta=r'D:\LearningPython\AutomateBoringStuff\bacon.txt'):

    baconFile = open(ruta, 'w')
    baconFile.write('Hello world!\n')
    baconFile.close()

    baconFile = open(ruta, 'a')
    baconFile.write('Bacon is not a vegetable.')
    baconFile.close()

readingFiles()
writingFiles(r'D:\LearningPython\AutomateBoringStuff\bacon.txt')
readingFiles(r'D:\LearningPython\AutomateBoringStuff\bacon.txt')
