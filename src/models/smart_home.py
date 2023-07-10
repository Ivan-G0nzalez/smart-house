
from abc import ABC
import logging
from src.util.config_util import GlobalConfig


# Configuración del formato del mensaje de registro
log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
formatter = logging.Formatter(log_format)

# Configuración del handler de archivo con el formato personalizado
file_handler = logging.FileHandler(GlobalConfig.get_log_filename())
file_handler.setFormatter(formatter)

class Room(ABC):
    def __init__(self, sensors: list) -> None:
        self.sensors = sensors
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)
        self.logger.info(f'{self.__class__.__name__} was created with the sensor {self.sensors}')

    def add_sensor(self, sensor):
        self.sensors.extend(sensor)

    def __repr__(self) -> str:
        return f"{self.name}, and there is {len(self.sensors)} sensors {self.sensors}" 

class LivingRoom(Room):
    def __init__(self, sensors) -> None:
        super().__init__(sensors)
        self.name = "Living Room"

class Bedroom(Room):
    def __init__(self,sensors) -> None:
        super().__init__(sensors)
        self.name = "BedRoom"    

class Bathroom(Room):
    def __init__(self, sensors) -> None:
        super().__init__(sensors)
        self.name = "Bathroom"

class Kitchen(Room):
    def __init__(self, sensors) -> None:
        super().__init__(sensors)
        self.name = "Kitchen"
        
class SmartHouse:
    def __init__(self, room:list[Room]) -> None:
        self.rooms = room

    def add_room(self, room:Room)-> None:
        self.rooms.append(room)   


