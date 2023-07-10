from src.models.smart_house_devices import *
from src.models.smart_home import *
from src.util.classes_creator import Builder

class TestRoom:
    def test_bathroom_with_devices(self):
        # Test that a Bathroom object can be created with Light and Window sensors
        light = Light()
        window = Window()
        room = Bathroom([light, window])
        assert isinstance(room.sensors[0], Light), "Cannot create Light sensor in Bathroom"
        assert isinstance(room.sensors[1], Window), "Cannot create Window sensor in Bathroom" 
        assert room.name == "Bathroom", "Cannot create Bathroom object"


    def test_build_room(self):
        # This test validate that my method create_room is working
        type_of_room = "Bathroom"
        room_created = Builder.create_room(type_of_room)    
        assert isinstance(room_created, Bathroom), "You are doing something wrong"