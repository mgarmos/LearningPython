import time, word
timestr = time.strftime("%Y%m%d-%H%M%S")
print (timestr)

#with open("Output.txt", "w") as text_file:
#    text_file.write("Writting test")
    
file = open("test.txt", "r")
for word in file:
  #print(word)
  sillables = [word.strip() for word in word.split(',')]
  for sillable in sillables:
    print(sillable)
file.close()


print(type(word.dupleSyllablesChoice))