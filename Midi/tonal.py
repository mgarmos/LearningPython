

    
class Tone:

    Do = 60
    Re = 62
    Mi = 64
    Fa = 65
    So = 67
    La = 69
    Ti = 71

    def __init__(self):
        raise NotImplementedError("Do not create raw Syllable objects.")

    def __str__(self):
        return self.name
        
    def getName(self):
        return self.name

    def getNotes(self):
        return self.notes
        
class T1(Tone):
    def __init__(self):
        self.name = "DU"
        self.notes = [Tone.Do, Tone.Mi, Tone.So]
        print(Tone.Do)

def main():
    tonalPattern = T1()
    print(T1.getNotes())
  
if __name__== "__main__":
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    