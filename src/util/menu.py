from src.util.classes_creator import Builder
from src.models.smart_home import SmartHouse
from src.util.config_util import GlobalConfig
# from src.util.logger import logger
from src.constants import *
import logging
import inspect

import click
import time

# Configuración del formato del mensaje de registro
log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
formatter = logging.Formatter(log_format)

# Configuración del handler de archivo con el formato personalizado
file_handler = logging.FileHandler(GlobalConfig.get_log_filename())
file_handler.setFormatter(formatter)



class Menu:
    logger = logging.getLogger("Menu")
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    @staticmethod
    def menu_smart_devices() -> None: 
        
        
        """
        Displays the main menu of the smart house system and handles user input to create rooms with sensors,
        navigate through the rooms, or sign off.

        Displays a submenu to create a room, where the user can select a room type and add sensors to it.
        Once a room is created, it is added to the list of rooms in the smart house.
        
        Displays a submenu to navigate through the rooms in the smart house.
        """
        
        smart_house = SmartHouse([])

        while True:
            Menu.logger.info("Menu was display")
            click.echo("""
            Hi Welcome to our system!... =)
            *_______________________*
            |                       |   
            |    1 - Create room    |
            |    2 - Navigate       |
            |    3 - Sign off       |
            |_______________________|
            *                       *
            """)
            answer = click.prompt("Enter a number ", type=click.Choice(["1", "2", "3"]))
            Menu.logger.info(f"The option {answer} was selected")

            if answer == "3":
                click.echo("Thanks for your preference!!!...")
                Menu.logger.info(f"Menu finished")
                break

            elif answer == "1":
                Menu.logger.info("Second menu was iniated")
                click.clear()
                while True:
                    answer_2 = Menu._show_room_menu(room_options )
                    if answer_2 == "5":
                        Menu.logger.info("Returning to the previous menu")
                        break
                                    
                    else: 
                        room_name = room_options[answer_2]
                        new_room = Builder.create_room(room_name)
                        sensors = Menu.menu_sensor(type_of_sensor)
                        new_room.add_sensor(sensors)
                        smart_house.add_room(new_room)

                        sensors_in_room = [f"{sensor.name}: {', '.join([device.name for device in sensor.devices])}" for sensor in sensors]
                        click.echo(f"{new_room.name} was created with {len(sensors_in_room)} sensors: {', '.join(sensors_in_room)}")                        
                        
            elif answer == "2":
                Menu._navigate(smart_house.rooms)

    
    def _show_object(objects):
        """
        Prints a numbered list of objects to the console.
        Args:
        objects (list): A list of objects to be displayed.
        """
        Menu.logger.info(f"Showing object: {objects}")
        for index, obj in enumerate(objects, 1):
            click.echo(f"{index} - {obj}")

    def _create_devices(list_devices):
        """
        Asks the user to create one or more devices from a list of available devices. The method uses the 
        `DeviceCreator` class to create device instances based on the user's selection. The method returns 
        a list of the devices created.
        
        Parameters:
        list_devices (list): A list of devices that can be created.
        """
        if not list_devices:
            return

        temp_list_devices = list(list_devices)
        temp_list_devices.append("go back")
        object_devices = []
        
        while len(temp_list_devices) > 0:
            click.clear()
            click.echo("Which device would you like to create? ")
            Menu._show_object(temp_list_devices)
            answer_place = click.prompt(
            "Chose one of the option above ",
            type=click.IntRange(min=1, max=len(temp_list_devices)),
            show_default=False,
            )

            if answer_place == len(temp_list_devices):
                return object_devices

            selected_device = temp_list_devices.pop(answer_place - 1)
            click.echo(f"{selected_device} was created.")
            time.sleep(3)
            object_devices.append(Builder.create_device_from_str(selected_device))
        
        return object_devices

    @staticmethod
    def menu_sensor(list_sensors):
        """
        Displays a menu to create and configure sensors.

        Args:
            list_sensors: A list of sensor types available for creation.

        Returns:
            A list of created sensors.
        """
        if not list_sensors:
            return

        temp_list_sensor = list(list_sensors)
        temp_list_sensor.append("go back")
        sensor_created = []

        sensor_creation_functions = {
            "Movement": lambda: Builder.create_sensor_2("Movement", "on", Menu._create_devices(movement_devices)),
            "Temperature": lambda: Builder.create_sensor_2("Temperature", "on", Menu._create_devices(temperature_devices), click.prompt("What's the temperature of the room", type=click.IntRange(min=0, max=40), show_default='20 (valid range: 0-40)', prompt_suffix='\nPlease enter a temperature between 0 and 40: '))
        }

        while len(temp_list_sensor) > 0:
            click.clear()
            click.echo("Which sensor would you like to create: ")
            Menu._show_object(temp_list_sensor)
            answer_place = click.prompt("Choose one of the options above", type=click.IntRange(min=1, max=len(temp_list_sensor)), show_default=False)

            selected_sensor = temp_list_sensor[answer_place - 1]
            temp_list_sensor.remove(selected_sensor)

            if selected_sensor == "go back":
                return sensor_created

            elif selected_sensor.capitalize() in sensor_creation_functions:
                Menu.logger.info(f"{selected_sensor} devices selected")
                sensor = sensor_creation_functions[selected_sensor.capitalize()]()
                click.echo(f"{selected_sensor} sensor was created")
                sensor_created.append(sensor)

    def _show_room_menu(room_options):
        """
        Displays a menu to select a room from a dictionary of room options.
        Parameters:
        - room_options: A dictionary mapping the available room options (room number) to their names (room description).
        Returns:
        - A string representing the selected room number.
        The function displays a menu with the available rooms and prompts the user to select one by entering the corresponding number.
        """
        click.echo("Which room would you like to create?")
        for key, value in room_options.items():
            click.echo(f"{key} - {value}")

        return click.prompt(
            "Chose one of the options above",
            type=click.Choice(room_options.keys()),
            show_choices=False
        )

    def _navigate(room_created):
        """
        Displays a list of rooms and prompts the user to choose a room and sensor to activate.
        If there are no rooms or sensors, appropriate messages are displayed.

        Args:
        - room_created: a list of Room objects
        """
        if not room_created:
            click.echo("No rooms created yet")
        else:
            for index,room in enumerate(room_created, 1):
                click.echo(f"{index} - {room.name}")

            answer_2 = click.prompt("Which room would you like to go: ", 
                                    type=click.IntRange(min=1, max=len(room_created)),
                                    show_default=f'1 (valid range: 1-{len(room_created)})')


            sensors_list = room_created[answer_2 - 1].sensors

            if not sensors_list:
                click.echo("No sensors in this room")
            else:
                for index, sensor in enumerate(sensors_list, 1):
                    click.echo(f"{index} - {sensor.name}")

                answer_3 = click.prompt("Which sensor would you like to activate?",
                            type=click.IntRange(min=1, max=len(sensors_list)))
                
                sensors_list[answer_3 - 1].detect_event()
                click.echo(f"In the {room_created[answer_2 - 1].name} the sensor {sensors_list[answer_3 - 1].name} has caused changes on {sensors_list[answer_3 - 1]}.")
                Menu.logger.info(f"In the {room_created[answer_2 - 1].name} the sensor {sensors_list[answer_3 - 1].name} has caused changes on {sensors_list[answer_3 - 1].devices}.")

