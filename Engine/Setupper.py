from Domain.World import World
import json
from sys import exit

def setup_world(data_from_REST_request = None, config_file_name = None):
    if config_file_name:
        setup_data = read_setup_from_file(filename = config_file_name)
    elif data_from_REST_request:
        setup_data = data_from_REST_request
    else:
        raise ValueError("Konfiguraatiodataa ei ole!")
        exit(1)

    validate_setup_input(setup_data)

    World.set_width(setup_data["worldWidth"])
    World.set_height(setup_data["worldHeight"])

    World.set_generation_one(setup_data["initialCells"])

    try:
        toroidal_in_X = setup_data["toroidalInX"]
        if toroidal_in_X in {True, False}:
            World.set_toroidal_in_X_dimension(toroidal_in_X)
        else:
            World.set_toroidal_in_X_dimension(True)
    except:
        World.set_toroidal_in_X_dimension(True)
    
    try:
        toroidal_in_Y = setup_data["toroidalInY"]
        if toroidal_in_Y in {True, False}:
            World.set_toroidal_in_Y_dimension(toroidal_in_Y)
        else:
            World.set_toroidal_in_Y_dimension(True)
    except:
        World.set_toroidal_in_Y_dimension(True)

def read_setup_from_file(filename):
    setup_data = None
    with open(filename, 'r', encoding="utf-8") as file:
        setup_data = json.loads(file.read())

    validate_setup_input(setup_data)

    return setup_data

def validate_setup_input(setup_json_data):
    height = setup_json_data["worldHeight"]
    width = setup_json_data["worldWidth"]
    cells = setup_json_data["initialCells"]

    if not height:
        raise ValueError("Korkeustieto puuttuu")
    elif not width:
        raise ValueError("Leveystieto puuttuu")
    elif not cells:
        raise ValueError("Solut puuttuvat")
    elif len(cells) > (width * height):
        raise ValueError("Syötteessä liikaa soluja")
    elif len(cells) < (width * height):
        raise ValueError("Syötteessä liian vähän soluja")
    else:
        for value in cells:
            if value not in [0, 1, "0", "1", True, False]:
                raise ValueError("Syötteen soluissa saa olla vain totuusarvoja")