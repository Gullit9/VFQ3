from usina import Usina
class Leitor_do_sensor:
    def __init__(self, sensor):
        self.sensor = sensor

    def altura_dagua(self):
        altura = 80/255*self.sensor+10
        return(altura)
    
class Controlador_do_atuador:

    def abrir_comporta(self, leitor):
        if leitor.altura_dagua() > 70:
            print("Altura maxima atingida")
            return(True)
        else:
            return(False)

class Subsistema:
    def __init__(self, leitor, controlador):
        self.leitor = leitor
        self.controlador = controlador

        vetor = []

        booleano = self.controlador.abrir_comporta(self.leitor.altura_dagua) 
        Usina.set_actuator(booleano)

        while (Usina.get_actuator(booleano) == True):
            self.leitor.sensor = Usina.get_sensor()
            booleano = self.controlador.abrir_comporta(self.leitor.altura_dagua) 
            Usina.set_actuator(booleano)
            vetor = vetor.append(self.leitor.altura_dagua)
            
            
            
            
        
        
