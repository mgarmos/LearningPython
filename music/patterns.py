class Pattern:
    def __init__(self):
        raise NotImplementedError("Do not create raw Pattern objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

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

class A4(Pattern):
    def __init__(self):
        self.name = "Duda-du"
        self.rithm = [0.5, 0.5, 1]			
