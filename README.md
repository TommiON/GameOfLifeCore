Backend/core for [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Implements the game logic and offers two modes of interaction:

## 1. Local

`python3 game_of_life_core.py <setup_file_name>`

Rudimentary text-based user interface, initial state given in a JSON file. Displays generation after generation with half-a-second intervals until extinction or manual termination.

Example of a configuration file:

```
    "worldHeight": 20,
    "initialCells": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "worldWidth": 20,
    "toroidalInX": true,
    "toroidalInY": true
```

Width and height dimensions and first generation of cells are required. If `toroidalInX` is `true`, the right/left edges are stiched together, making that dimension infinite. `toroidalInY` is similar in up/down dimension. Both are optional and default to `true`.

### 2. REST interface for a separate frontend

`python3 game_of_life_core.py`

Endpoints:

`POST /setup` Sets up the world dimensions and first generation. Data in request body, format similar to local setup JSON.

`GET /next_generation` Returns the next generation.

`GET /generation/<generation_number>` Jumps straight to and returns an arbitrary generation, using cached generations and computation as needed.

`GET /healthcheck` General health check.

