from src.util.logger import logger

class Sensor:   
    def __init__(self, name: str, state: str, devices: list):
        """
        Initializes a Sensor object.
        :param name: The name of the sensor.
        :param state: The state of the sensor.
        :param devices: The list of devices associated with the sensor.
        """
        self.name = name
        self.state = state
        self.devices = devices

        logger.info(f"Sensor created: Name: {self.name}, Status {self.state}, Devices: {self.devices}")

    def add_devices(self, new_device):
        """
        Adds a new device to the sensor.
        :param new_device: The device to be added to the sensor.
        """
        logger.info(f"A {new_device} was added to Sensor: {self.name}")
        self.devices.append(new_device)


    def not_detect_event(self):
        """
        Turns off all devices associated with the sensor when no event is detected.
        """
        logger.info(f"No event detected in {self.name}")
        for device in self.devices:
            device.off()        

    def detect_event(self):
        """
        Turns on all devices associated with the sensor when an event is detected.
        """
        logger.info(f"Event detected in {self.name}")
        for device in self.devices:
            logger.info(f"{device}")
            device.on()

    def _show_devices(self):
        if (self.devices) == 0:
            return "No devices"
        return [(device.name, device.show_status()) for device in self.devices]


    def __str__(self) -> str:
        """
        Returns a string representation of the Sensor object.
        """
        return f"""[{{name: {self.name},
        state: {self.state},
        devices: {self._show_devices()} 
        }}]"""


class TemperatureSensor(Sensor):
    def __init__(self, name: str, state: str, devices: list, temperature:int):
        """
        Initializes a TemperatureSensor object.
        :param name: The name of the temperature sensor.
        :param state: The state of the temperature sensor.
        :param devices: The list of devices associated with the temperature sensor.
        :param temperature: The current temperature.
        """
        super().__init__(name, state, devices)
        self.temperature = temperature

    def detect_event(self):
        """
        Turns on or off devices based on the temperature reading.
        """
        for device in self.devices:
            if (device.name == "AirCondicioner" and self.temperature > 35) or \
                (device.name == "Window" and self.temperature < 20):
                device.on()
            elif (device.name == "AirCondicioner" and self.temperature < 20) or \
                (device.name == "Window" and self.temperature > 35):
                device.off()
            


