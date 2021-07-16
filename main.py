from usina import Usina
from Q3 import Leitor_do_sensor
from Q3 import Controlador_do_atuador
from Q3 import Subsistema

Usina1 = Usina()
controlador = Controlador_do_atuador()

sensor = Usina.get_sensor
atuador = Usina.get_actuator
leitor = Leitor_do_sensor(sensor)


Subsistema1 = Subsistema(leitor, controlador)
