import fastapi
from pydantic import BaseModel
import pandas as pd

# Set up router
router = fastapi.APIRouter()

# load data
efternamn = pd.read_csv("data/efternamn.csv")
förnamn_kvinnor = pd.read_csv("data/förnamn_kvinnor.csv")
förnamn_män = pd.read_csv("data/förnamn_män.csv")
tilltalsnamn_kvinnor = pd.read_csv("data/tilltalsnamn_kvinnor.csv")
tilltalsnamn_män = pd.read_csv("data/tilltalsnamn_män.csv")


class Names(BaseModel):
    Män: int
    Kvinnor: int


class QueryResult(BaseModel):
    Query_name: str
    Förnamn: Names
    Tilltalsnamn: Names
    Efternamn: int


@router.get("/search_name/")
def search_name(name: str) -> QueryResult:
    """
    Search for a name in the database and return the number of people with that name.

    Input:
        name (str): The name to search for.

    Output:
        result_json (JSON): A JSON structure with the number of people with that name.
    """

    # Clean input. Make sure first letter is capitalized and remove whitespace.
    name = name.upper().strip()

    num_efternamn = efternamn.query(f"Efternamn=='{name}'")["Antal bärare"]
    num_förnamn_kvinnor = förnamn_kvinnor.query(f"Förnamn=='{name}'")["Antal bärare"]
    num_förnamn_män = förnamn_män.query(f"Förnamn=='{name}'")["Antal bärare"]
    num_tilltalsnamn_män = tilltalsnamn_män.query(f"Tilltalsnamn=='{name}'")[
        "Antal bärare"
    ]
    num_tilltalsnamn_kvinnor = tilltalsnamn_kvinnor.query(f"Tilltalsnamn=='{name}'")[
        "Antal bärare"
    ]

    num_tilltalsnamn_kvinnor = (
        int(num_tilltalsnamn_kvinnor.values[0])
        if len(num_tilltalsnamn_kvinnor) > 0
        else 0
    )
    num_tilltalsnamn_män = (
        int(num_tilltalsnamn_män.values[0]) if len(num_tilltalsnamn_män) > 0 else 0
    )
    num_förnamn_män = int(num_förnamn_män.values[0]) if len(num_förnamn_män) > 0 else 0
    num_förnamn_kvinnor = (
        int(num_förnamn_kvinnor.values[0]) if len(num_förnamn_kvinnor) > 0 else 0
    )
    num_efternamn = int(num_efternamn.values[0]) if len(num_efternamn) > 0 else 0
    # Create JSON structure
    result_json = {
        "Query_name": name[0] + name[1:].lower(),
        "Förnamn": {"Män": num_förnamn_män, "Kvinnor": num_förnamn_kvinnor},
        "Tilltalsnamn": {
            "Män": num_tilltalsnamn_män,
            "Kvinnor": num_tilltalsnamn_kvinnor,
        },
        "Efternamn": num_efternamn,
    }

    return QueryResult(**result_json)
