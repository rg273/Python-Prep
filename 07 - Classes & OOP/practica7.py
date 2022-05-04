from cgi import print_directory

class vehiculo:
    def __init__(self, color, tipodevehiculo,cilindradodevehiculo):
        self.color = color
        self.tipodevehiculo = tipodevehiculo
        self.cilindradodevehiculo = cilindradodevehiculo
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self,vel):
        self.velocidad += vel
        print(self.velocidad)        
    def Frenar(self,freno):
        self.velocidad -= freno
        print(self.velocidad)
    def Doblar(self,grado):
        if grado > 0: 
            self.direccion += grado
        else: self.direccion -=grado
        print(self.direccion)
    def Detalles(self):
        print("Marca:",self.tipodevehiculo,"\nCilindrado:",self.cilindradodevehiculo,"\nColor: ",self.color,"\nA que velocidad se encuentra: ",self.velocidad,"\nA donde se dirige: ",self.direccion)

miauto = vehiculo("rojo","bmw",2.1)
mimoto = vehiculo("gris","bmw", 1.6)
micamion = vehiculo("negro","Mercedes Benz" , 3.6)
print(miauto.tipodevehiculo)


micamion.Acelerar(100)
micamion.Doblar(50)
micamion.Frenar(100)
micamion.Detalles()


def varios(param1, param2, **otros):
    print (param1,param2, otros)

varios(1, 2, tercero = 3)