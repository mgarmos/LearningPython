"""
Open a file and read it
"""
filepath = "D:/Usuarios/Magarami/Desktop/Hello.txt"  

with open(filepath) as fp:  
	line = fp.readline()
	cnt = 1
	while line:
		print("Line {}: {}".format(cnt, line.strip()))
		line = fp.readline()
		cnt += 1


