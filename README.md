Backend/core for [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Implements the game logic and offers two modes of interaction:

###### 1. Local

Rudimentary text-based user interface, initial state given in a JSON file.

`python3 game_of_life_core.py <setup_file_name>`

Displays generation after generation with half-a-second intervals until extinction or manual termination.

###### 2. REST interface for a separate frontend.

`python3 game_of_life_core.py`

Endpoints:

`POST /setup` Sets up the world dimensions and first generation. Data in request body, format similar to local setup JSON. 
`GET /next_generation` Returns the next generation.
`GET /generation/<generation_number>` Jumps straight to and returns an arbitrary generation, using cached generations and computation as needed.
`GET /healthcheck` General health check.

