
class Syllable:

	def __init__(self):
		raise NotImplementedError("Do not create raw Syllable objects.")

	def __str__(self):
		return self.name
		
	def getName(self):
		return self.name
		
class A1(Syllable):
	def __init__(self):
		self.name = "DU"
		self.duration = [1]

class A2(Syllable):
    def __init__(self):
        self.name = "DU DE"
        self.rithm = [0.5,0.5]
		
class A3(Syllable):
    def __init__(self):
        self.name = "DU-Ta DE-Ta"
        self.rithm = [0.25, 0.25, 0.25, 0.25]

class A4(Syllable):
    def __init__(self):
        self.name = "DU DE-Ta"
        self.rithm = [0.5, 0.25, 0.25]

class A5(Syllable):
    def __init__(self):
        self.name = "DU-Ta DE"
        self.rithm = [0.25, 0.25, 0.5]

class B1(Syllable):
    def __init__(self):
        self.name = "DU"
        self.rithm = [3]
		
class B2(Syllable):
    def __init__(self):
        self.name = "DU DA DI"
        self.rithm = [3]

class B3(Syllable):
    def __init__(self):
        self.name = "DU-Ta DA DI"
        self.rithm = [3]

class B4(Syllable):
    def __init__(self):
        self.name = "DU DA-Ta DI"
        self.rithm = [3]

class B5(Syllable):
    def __init__(self):
        self.name = "DU DA DI-Ta"
        self.rithm = [3]

class B6(Syllable):
    def __init__(self):
        self.name = "DU-Ta DA-Ta DI-Ta"
        self.rithm = [3]		