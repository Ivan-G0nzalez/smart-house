import logging
from abc import ABC
from src.util.config_util import GlobalConfig

# Configuración del formato del mensaje de registro
log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
formatter = logging.Formatter(log_format)

# Configuración del handler de archivo con el formato personalizado
file_handler = logging.FileHandler(GlobalConfig.get_log_filename())
file_handler.setFormatter(formatter)

class SmartHouseDevices(ABC):
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)
        
    def on(self):
        if self.status:
            self.logger.info(f"{self.name} is already On")    
        else:
            self.status = True
            self.logger.info(f"{self.name} is now On")

    def off(self):
        if self.status == False:
            self.logger.info(f"{self.name} is already off")  
        else:
            self.status = False
            self.logger.info(f"{self.name} is now off")  

    def show_status(self):
        return "on" if self.status else "off"

    def __repr__(self) -> str:
        return f"""{{name:{self.name},
        status:{"on" if self.status else "off"} }}"""
    
    def __str__(self) -> str:
        return self.name


class Light(SmartHouseDevices):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Light"
        self.status = False
        self.logger.info(f"{self.__class__.__name__} Creacted, Status: {self.status}")

        

class Television(SmartHouseDevices):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Television"
        self.status = False
        self.logger.info(f"{self.__class__.__name__} Creacted, Status: {self.status}")


class Aircondicioner(SmartHouseDevices):
    def __init__(self) -> None:
        super().__init__()
        self.name = "AirCondicioner"
        self.status = False
        self.logger.info(f"{self.__class__.__name__} Creacted, Status: {self.status}")


class Camera(SmartHouseDevices):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Camera"
        self.status = False
        self.logger.info(f"{self.__class__.__name__} Creacted, Status: {self.status}")

class Window(SmartHouseDevices):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Window"
        self.status = False
        self.logger.info(f"{self.__class__.__name__} Creacted, Status: {self.status}")


    def show_status(self):
        return "open" if self.status else "closed"