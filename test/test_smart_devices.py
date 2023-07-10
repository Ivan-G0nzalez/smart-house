from src.models.smart_house_devices import *
from src.models.smart_home import * 
from src.sensor import *
from src.util.classes_creator import *

class TestSmartHouseDevices:
    def test_intance_smart_house(self):
        # Test that an instance of SmartHouseDevices can be created
        house = SmartHouseDevices()
        assert isinstance(house, SmartHouseDevices), "Cannot create instance of SmartHouseDevices"

    def test_light_on_or_off(self):
        # Test that a Light object can be turned on or off
        light = Light()
        light.on()
        assert light.status == True, "Cannot turn Light on"
        light.off()
        assert light.status == False, "Cannot turn Light off"

    def test_TV_on_or_off(self):
        # Test that a Television object can be turned on or off
        television = Television()
        television.on()
        assert television.status == True, "Cannot turn Television on"
        television.off()
        assert television.status == False, "Cannot turn Television off"

    def test_temperature_on_or_off(self):
        # Test that an Aircondicioner object can be turned on or off
        air_condicioner = Aircondicioner()
        air_condicioner.on()
        assert air_condicioner.status == True, "Cannot turn Aircondicioner on"
        air_condicioner.off()
        assert air_condicioner.status == False, "Cannot turn Aircondicioner off"    

    def test_window_open_or_close(self):
        # Test that a Window object can be opened or closed
        window = Window()
        window.on()
        assert window.status == True, "Cannot open Window"
        window.off()
        assert window.status == False, "Cannot close Window"    

    

    def test_create_devices(self):
        # Test that an instance of Aircondicioner and Window can be created from dictionaries
        devices_1 = {'name': 'AirCondicioner', 'status': False} 
        device_created = Builder.create_device_instance_from_dict(devices_1)
        devices2 = {'name': 'window', 'status': True} 
        device_created2 = Builder.create_device_instance_from_dict(devices2)

        assert isinstance(device_created, Aircondicioner), "Cannot create Aircondicioner from dictionary"
        assert isinstance(device_created2, Window), "Cannot create Window from dictionary"
        assert device_created.status == False, "Cannot set initial status of Aircondicioner"
        assert device_created2.status == True, "Cannot set initial status of Window"