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

        CachedGenerations.store_latest(population = generation_one)
        #CachedGenerations.store_generation(population = generation_one)
        
        return jsonify({
            "generation": generation_one.generation,
            "census": generation_one.census,
            "cells": generation_one.get_cell_values()
        })
    
    except ValueError as error:
        return jsonify({ "VIRHE": str(error)})
    
@app.route("/next_generation", methods = ["GET"])
def next_generation():
    try:
        next_generation = Population(previous_generation = CachedGenerations.latest)
    
        CachedGenerations.store_latest(next_generation)

        return jsonify({
            "generation": next_generation.generation,
            "census": next_generation.census,
            "cells": next_generation.get_cell_values()
        })
    
    except AttributeError as error:
        return jsonify({ "VIRHE": "sisäinen virhe"})