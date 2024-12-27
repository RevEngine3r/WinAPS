import pathlib as pl
import json


# {"ac":[],"bt":[]}


def load_config():
    return json.loads(pl.Path('config.json').read_text())


nircmdc = r'.\bin\nircmdc'

on_battery_actions = [
    f'{nircmdc} setdisplay 1920 1080 24 60',
    f'{nircmdc} setbrightness 1',
]

on_ac_actions = [
    f'{nircmdc} setdisplay 1920 1080 24 144',
    f'{nircmdc} setbrightness 90',
]


def get_commands_battery():
    return on_battery_actions


def get_commands_ac():
    return on_ac_actions
