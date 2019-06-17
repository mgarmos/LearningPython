import random

class Pattern:

    
    def __init__(self):
        raise NotImplementedError("Do not create raw Pattern objects.")

    def __str__(self):
        return self.name



    def getNotes(self):
        # scala  = [60, 62, 64, 65, 67, 69]  # MIDI note number
        Hand_Clap = 39
        Side_Stick = 37
        Short_Whistle = 71

        scala  = [Side_Stick]  # MIDI note number
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
        self.name = "DU"
        self.rithm = [1]

class A2(Pattern):
    def __init__(self):
        self.name = "DU·DE"
        self.rithm = [0.5,0.5]
		
class A3(Pattern):
    def __init__(self):
        self.name = "DU-Ta·DE-Ta"
        self.rithm = [0.25, 0.25, 0.25, 0.25]

class A4(Pattern):
    def __init__(self):
        self.name = "DU·DE-Ta"
        self.rithm = [0.5, 0.25, 0.25]

class A5(Pattern):
    def __init__(self):
        self.name = "DU-Ta·DE"
        self.rithm = [0.25, 0.25, 0.5]

class I1(Pattern):
    def __init__(self):
        self.name = "Inicio"
        self.rithm = [1,1,1,1]

class B1(Pattern):
    def __init__(self):
        self.name = "DU"
        self.rithm = [3]
		
class B2(Pattern):
    def __init__(self):
        self.name = "DU·DA·DI"
        self.rithm = [1,1,1]

class B3(Pattern):
    def __init__(self):
        self.name = "DU-Ta·DA·DI"
        self.rithm = [0.5,0.5,1,1]

class B4(Pattern):
    def __init__(self):
        self.name = "DU·DA-Ta·DI"
        self.rithm = [1,0.5,0.5,1]

class B5(Pattern):
    def __init__(self):
        self.name = "DU·DA·DI-Ta"
        self.rithm = [1,1,0.5,0.5]

class B6(Pattern):
    def __init__(self):
        self.name = "DU-Ta·DA-Ta·DI-Ta"
        self.rithm = [0.5,0.5,0.5,0.5,0.5,0.5]
