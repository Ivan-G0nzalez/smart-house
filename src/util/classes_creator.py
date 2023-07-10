from src.models.smart_house_devices import *
from src.models.smart_home import *
from src.sensor import *

class Builder:
    @staticmethod
    def create_device_from_str(input_device:str):
        device_type = input_device.capitalize()

        if device_type in globals():
            return globals()[device_type]()
        else:
            logger.error(f"No device class found for {input_device}")
            return None

    @staticmethod
    def create_device_instance_from_dict(device_class_name:dict):
        device_type = device_class_name["name"].capitalize()
        device_status = device_class_name["status"]

        if device_type in globals():
            device_class = globals()[device_type]()
            device_class.status = device_status
            return device_class    

        else:
            logger.error("Class not founded")
            return        

    @staticmethod
    def create_devices(devices_list_without_format:list[dict]):
        if not devices_list_without_format:
            return [] 
        
        list_device_formated = []

        for device in devices_list_without_format:
            list_device_formated.append(Builder.create_device_instance_from_dict(device))
        
        return list_device_formated    
    
    @staticmethod
    def create_room(room_name: str) -> Room:
        room = "".join([word.capitalize() for word in room_name.split(" ")])
        room = globals()[room]([])
        return room

    @staticmethod
    def create_sensor_2(name, state, devices, temperature=None) -> Sensor:
        """
        Creates a new Sensor object or TemperatureSensor object based on the name parameter.
        :param name: The name of the sensor.
        :param state: The state of the sensor.
        :param devices: The list of devices associated with the sensor.
        :param temperature: The current temperature (optional).
        :return: A new Sensor or TemperatureSensor object.
        """
        if name.capitalize() == "Movement":
            return Sensor(name, state, devices)
        else:
            return TemperatureSensor(name, state, devices, temperature)

    @staticmethod
    def create_sensor(data_dictionary:dict) -> Sensor:
        """
        Create a new sensor object from a dictionary of sensor data.
        Args: data_dictionary (dict): A dictionary containing the sensor data.
        Returns: Sensor: A new sensor object.
        """
        sensor = data_dictionary.get("sensor")
        type_sensor = sensor.get("name")
        state = sensor.get("state")
        devices = sensor.get("devices")

        if type_sensor.capitalize() == "Movement":
            created_devices = Builder.create_devices(devices)
            return Sensor(type_sensor, state, created_devices)
        else:
            temperature = sensor.get("temperature")
            created_devices = Builder.create_devices(devices)
            return TemperatureSensor(type_sensor, state, created_devices, temperature)


