import random

class Pattern:
    
    def __init__(self):
        raise NotImplementedError("Do not create raw Pattern objects.")

    def __str__(self):
        return self.name



    def getNotes(self):
        # scala  = [60, 62, 64, 65, 67, 69]  # MIDI note number
        scala  = [60]  # MIDI note number
        notes = []
        note = []
        for duration in self.rithm:
            note = []
            note.append(random.choice(scala))
            note.append(duration)
            notes.append(note)
        return notes


class A1(Pattern):
    def __init__(self):
        self.name = "Du"
        self.rithm = [2]

class A2(Pattern):
    def __init__(self):
        self.name = "Du-dei"
        self.rithm = [1,1]
		
class A3(Pattern):
    def __init__(self):
        self.name = "Du-da-dei-da"
        self.rithm = [0.5, 0.5, 0.5, 0.5]

class A4(Pattern):
    def __init__(self):
        self.name = "Du-deida"
        self.rithm = [1, 0.5, 0.5]

class A5(Pattern):
    def __init__(self):
        self.name = "Duda-du"
        self.rithm = [0.5, 0.5, 1]

class I1(Pattern):
    def __init__(self):
        self.name = "Inicio"
        self.rithm = [1,1,1,1]					
