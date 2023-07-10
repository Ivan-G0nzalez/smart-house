from src.util.menu import Menu
import click

@click.command(help="Welcome to our menu")
def run():
  Menu.menu_smart_devices()

if __name__=="__main__":
  run()

