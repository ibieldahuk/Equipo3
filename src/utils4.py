#from typing import ChainMap

#4- Crear una clase que represente al perfil usuario que ademas tenga una relacion (herencia) con estas dos clases:
#administrador y reportero (solo tiene lectura de datos).El usuario tiene objeto carrito de compras.El administrador puede ver 
# a todos los usuarios y lo que tenga adentro.El reporter solo ve todos los carritos de compra.

class Carrito(): #clase que representa a los carritos q son atributos de los usuarios
    capacidad = 0
    
    def __init__(self, tamaño=5) -> None:
        self.capacidad = tamaño
        self.carrito = []
    
    def agregar_item(self, item):
        if (len(self.carrito) == self.capacidad):
            print("El carrito esta completo")
        else:
            self.carrito.append(item)
        
    def borrar_item(self, item):
        if len(self.carrito) == 0:
            print("El carrito no tiene ningún item")
        else:
            self.carrito.remove(item)
            
ejemplo1 = Carrito()
ejemplo1.agregar_item('Manzana')
ejemplo1.agregar_item('Pera')
ejemplo1.agregar_item('Banana')
print(ejemplo1.carrito)
ejemplo1.borrar_item('Manzana')
print(ejemplo1.carrito)

ejemplo2 = Carrito()
ejemplo2.agregar_item('Olla')
ejemplo2.agregar_item('Cacerola')
print(ejemplo2.carrito)

class Storage(): #lista de los carritos de los usuarios. Es el almacén
    almacen = []
    ocupacion = 0
    
    def __init__(self, carrito) -> None:
        self.almacen = [carrito]

    def cantidad_items(self) -> int:
        self.ocupacion = len(self.almacen)
        return self.ocupacion
    
    def agregar_carrito(self, carrito) -> None:
        self.almacen.append(carrito)
        self.ocupacion += 1
    
    def sacar_carrito(self, carrito) -> None:
        self.almacen.remove(carrito)
        self.ocupacion -= 1
    
    def __str__(self) -> str:
        cadena = ""
        for carrito in self.almacen:
            cadena += "\nCarrito:"
            for item in carrito.carrito:
                cadena += " -" + item
        return cadena

stor1 = Storage(ejemplo1)
stor1.agregar_carrito(ejemplo2)
print(stor1)

"""
class UserTemplate:  #clase abstracta
    Perfil=""
    
    def __init__(self,uname,email,URiAvatar) -> None:
         self.uname=uname
         self.email=email
         self.URiAvatar=URiAvatar
         
    def __str__(self) -> str:
        pass
        
    def muestra_carrito(self, uname) -> None:
        pass
    
    def muestra_usuarios(self, uname) -> None:
        pass
    
    def __str__(self) -> str:
        pass
    
class Users: #es la lista de usuarios
    Usuarios =[]
    
    def __init__(self) -> None:
        pass

    def AgregaUsuario(self,Usuarios) -> None:
        Usuarios.append((UserTemplate.uname,UserTemplate.email))
    
    def __str__(self,Usuarios) -> str:
        cadena= "Los usuarios son:" + " "
        for i in range(len(Usuarios)):
            cadena= cadena + Usuarios[i] + ", "
        return

class Admin(UserTemplate):
    Perfil = "A"
    
    def __init__(self, uname, email, URiAvatar, Stor:Storage) -> None:
        super().__init__(uname, email, URiAvatar)    

    def muestra_carritos(Stor) -> None:
       print("Los carritos contienen: ", Stor )
    
    def muestra_usuarios(self, list) -> None:
        print("Los usuarios son: " ,list )
    
    def __str__(self) -> str:
        return super().__str__()
    
class Reporter(UserTemplate):
    Perfil = "R"
    
    def __init__(self, uname, email, URiAvatar, Stor:Storage) -> None:
        super().__init__(uname, email, URiAvatar)
    
    def muestra_carrito(self, Stor) -> None:
        print("Los carritos contienen: ", Stor )
    
    def muestra_usuarios(self) -> None:
        print ("Función no permitida para el tipo de usuario")

    def __str__(self) -> str:
        return super().__str__()
    
class Usuario(UserTemplate):
    Perfil = "U"
    Ucarrito = carrito(10)
    
    def __init__(self, uname, email, URiAvatar,stor:Storage) -> None:
        super().__init__(uname, email, URiAvatar)
        stor.agregaCarrito(self.Ucarrito)
    
    def muestra_carrito(self) -> None:
       # return super().muestra_carrito(uname)
       print("El carrito contiene: " + "{}", self.Ucarrito)
    
    def muestra_usuarios(self) -> None:
       #return super().muestra_usuarios()
       print ("Soy el Usuario: " + self.uname)
    
    def __str__(self) -> str:
        return super().__str__()
    
class UserCrate(UserTemplate):
    def __init__(self, uname, email, URiAvatar,type,stor) -> None:
        self.uname=uname
        self.email=email
        self.URiAvatar=URiAvatar
        if (type=="A"):   
            Admin(uname,email,URiAvatar,stor)
        elif(type=="R"):
            Reporter(uname,email,URiAvatar,stor)
        elif(type=="U"):
            Usuario(uname,email,URiAvatar,stor)
        else:
            print("Tipo de usuario incorrecto")
"""