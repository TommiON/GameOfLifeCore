from Domain.Population import Population
from Domain.World import World
from Engine.Setupper import validate_setup_input
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
    
        response = {
            "generation": generation_one.generation,
            "census": generation_one.census,
            "cells": generation_one.get_cell_values()
        }
        
        return jsonify(response)
    
    except ValueError as error:
        return jsonify({ "VIRHE": str(error)})