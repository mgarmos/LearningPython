

Texto1='11'
Texto2='55'

# print(Texto1 + Texto2)

# Numero1=11
# Numero2=55




# print(Numero1 / Numero2)
# print(4%3)

# print((4>2)== True)

# class Consumable:
#     def __init__(self):
#         raise NotImplementedError("Do not create raw Consumable objects.")
       

#     def __str__(self):

# print(isinstance(pepe,Consumable))
#         return "{} (+{} HP)".format(self.name, self.healing_value)

# class CrustyBread(Consumable):
#     def __init__(self):
#         self.name='CrustyBread'
#         self.healing_value = 10

# class Banana(Consumable):
#     def __init__(self):
#         self.name='Banana'
#         self.healing_value = 30


# pepe = Banana()

# print(pepe)

lista=['pepe',12,'juan',67]
print(lista)
print(len(lista))

for name in lista:
    if isinstance(name,int):
        print(name)

lista1=[a*2 for a in range(5) if a > 3]
print(lista1)

lista1=[a for a in lista if isinstance(a,str)]
print(lista1)