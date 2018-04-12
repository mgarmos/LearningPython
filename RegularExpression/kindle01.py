import re

BOUNDARY = u"==========\r\n"

def get_sections(filename):
	""" Returns all the sections"""
	with open(filename, 'rb') as f:
		content = f.read().decode('utf-8')
	content = content.replace(u'\ufeff', u'')
	content = content.replace(u'\u2666',u'')
	content = content.replace(u'\u2015',u'')
	return content.split(BOUNDARY)
	
def get_clip(section):
    clip = {}

    lines = [l for l in section.split(u'\r\n') if l] # Elimina las lineas en blanco
    if len(lines) != 3:
        return

    clip['book'] = lines[0]
    match = re.search(r'(\d+)-\d+', lines[1])
    if not match:
        return
    position = match.group(1)

    clip['position'] = int(position)
    clip['content'] = lines[2]

    return clip	
	
	
sections = get_sections('My Clippings.txt')
for section in sections:
	print(get_clip(section))


# contador = 0
# salida = open("resultado.txt","w")
# for line in get_sections('My Clippings.txt'):
	# contador += 1
	# salida.write("[" +  str(contador) + "]")
	# for word in line:
		# salida.write(word)
# salida.close
