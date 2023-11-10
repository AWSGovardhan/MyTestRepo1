from fastapi import FastAPI, HTTPException

# Create a FastAPI app
app = FastAPI()

# LEGO Set data
lego_sets = []

# Define a LEGO Set model
class LegoSet:
    def __init__(self, id, name, pieces):
        self.id = id
        self.name = name
        self.pieces = pieces

# Create a new LEGO Set using a design pattern
def create_lego_set(name, pieces):
    new_lego_set = LegoSet(id=len(lego_sets) + 1, name=name, pieces=pieces)
    lego_sets.append(new_lego_set)
    return new_lego_set

# Get all LEGO Sets
@app.get("/legosets", response_model=list[LegoSet])
def read_lego_sets():
    return lego_sets

# Create a new LEGO Set
@app.post("/legosets", response_model=LegoSet)
def create_lego_set_endpoint(name: str, pieces: int):
    lego_set = create_lego_set(name, pieces)
    return lego_set

# Get a single LEGO Set by ID
@app.get("/legosets/{lego_id}", response_model=LegoSet)
def read_lego_set(lego_id: int):
    for lego_set in lego_sets:
        if lego_set.id == lego_id:
            return lego_set
    raise HTTPException(status_code=404, detail="LEGO Set not found")

# Update a LEGO Set
@app.put("/legosets/{lego_id}", response_model=LegoSet)
def update_lego_set(lego_id: int, name: str, pieces: int):
    for lego_set in lego_sets:
        if lego_set.id == lego_id:
            lego_set.name = name
            lego_set.pieces = pieces
            return lego_set
    raise HTTPException(status_code=404, detail="LEGO Set not found")

# Delete a LEGO Set
@app.delete("/legosets/{lego_id}", response_model=LegoSet)
def delete_lego_set(lego_id: int):
    for lego_set in lego_sets:
        if lego_set.id == lego_id:
            lego_sets.remove(lego_set)
            return lego_set
    raise HTTPException(status_code=404, detail="LEGO Set not found")
