import json

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