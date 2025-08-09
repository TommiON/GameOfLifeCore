import json

def read_setup_from_json():
    setup_data = None
    with open('setup.json', 'r', encoding="utf-8") as file:
        setup_data = json.loads(file.read())

    validate_input(setup_data)

    return setup_data

def validate_input(setup_json_data):
    height = setup_json_data["worldHeight"]
    width = setup_json_data["worldWidth"]
    cells = setup_json_data["initialCells"]

    if len(cells) > (width * height):
        raise ValueError("Syötteessä liikaa arvoja")
    elif len(cells) < (width * height):
        raise ValueError("Syötteessä liian vähän arvoja")
    else:
        for value in cells:
            if value not in [0, 1, "0", "1", True, False]:
                raise ValueError("Syötteessä saa olla vain totuusarvoja")