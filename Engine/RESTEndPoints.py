from Domain.Population import Population
from Domain.World import World
from Engine.Setupper import validate_setup_input
from Engine.CachedGenerations import CachedGenerations
from flask import Flask, jsonify, request

app = Flask(__name__)

def listen_for_requests():
    app.run(debug = True)

@app.route("/healthcheck", methods = ["GET"])
def get_status():
    return jsonify({"Terveys": "Hyvä!"})

@app.route("/setup", methods = ["POST"])
def setup():
    try:
        validate_setup_input(request.json)

        World.set_width(request.json["worldWidth"])
        World.set_height(request.json["worldHeight"])
        
        generation_one = Population(initial_cell_values = request.json["initialCells"])

        CachedGenerations.store_seed(population = generation_one)
        
        return jsonify({
            "generation": generation_one.generation,
            "census": generation_one.census,
            "cells": generation_one.get_cell_values()
        })
    
    except ValueError as error:
        return jsonify({ "VIRHE": str(error)})
    
@app.route("/next_generation", methods = ["GET"])
def next_generation():
    if CachedGenerations.seed_generation is None:
        return jsonify({"VIRHE": "Maailmaa ei ole vielä alustettu"})

    try:
        next_generation = Population(previous_generation = CachedGenerations.latest_generation)
        CachedGenerations.store_latest(next_generation)

        return jsonify({
            "generation": next_generation.generation,
            "census": next_generation.census,
            "cells": next_generation.get_cell_values()
        })
    
    except AttributeError as error:
        return jsonify({ "VIRHE": "sisäinen virhe"})
    
@app.route("/generation/<generation_number>", methods = ["GET"])
def generation(generation_number):
    if CachedGenerations.seed_generation is None:
        return jsonify({"VIRHE": "Maailmaa ei ole vielä alustettu"})

    if CachedGenerations.retrieve_generation(generation_number) is not None:
        nth_generation = CachedGenerations.retrieve_generation(generation_number)
    elif CachedGenerations.get_nearest_lesser_generation(generation_number) is not None:
        nth_generation = CachedGenerations.get_nearest_lesser_generation(generation_number)
        
        while(nth_generation.generation < int(generation_number)):
            previous_generation = nth_generation
            nth_generation = Population(previous_generation = previous_generation)
    else:
        nth_generation = CachedGenerations.seed_generation

        for index in range(1, int(generation_number)):
            previous_generation = nth_generation
            nth_generation = Population(previous_generation = previous_generation)

    return jsonify({
        "generation": nth_generation.generation,
        "census": nth_generation.census,
        "cells": nth_generation.get_cell_values()
    })
