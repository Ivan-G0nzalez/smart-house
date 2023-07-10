from src.models.smart_house_devices import *
from src.models.smart_home import * 
from src.sensor import *
from src.util.classes_creator import Builder


class TestSensor:
    def test_sensor(self):
        """
        Check that `detect_event` method of `Sensor` object turns on
        associated `Light` object
        """
        light1_room1 = Light()
        light2_room1 = Light()
        camera_room1 = Camera()
        movement_sensor_room1 = Sensor("Movement", "on", [light1_room1, light2_room1, camera_room1])
        assert not light1_room1.status 
        movement_sensor_room1.detect_event()
        assert light1_room1.status 

    def test_temperature_sensor(self):
        """
        Check that `detect_event` method of `TemperatureSensor` 
        object turns on associated `AirConditioner` object and turns off
        associated `Window` object when temperature is above a threshold
        """
        air_conditioner_room = Aircondicioner()
        window_room = Window()
        temperature_sensor = TemperatureSensor("Temperature Sensor", "on", [air_conditioner_room, window_room], 40)
        temperature_sensor.detect_event()
        assert air_conditioner_room.status
        assert not window_room.status

    def test_create_sensor(self):
        """
        Check that `create_sensor` method of `CreateSensor` class 
        returns a `TemperatureSensor` object with the same name as
        the one specified in the input dictionary
        """

        sensor = {
            'sensor': {
                'name': 'Temperature',
                'state': 'on',
                'devices': [
                    {'name': 'aircondicioner', 'status': False},
                    {'name': 'Window', 'status': False}
                ],
                "temperature": 40
            }
        }
        new_sensor = Builder.create_sensor(sensor) 
        assert isinstance(new_sensor, TemperatureSensor)
        assert sensor['sensor']['name'] == 'Temperature'

