from pydantic import BaseModel
from typing import Optional

class Users(BaseModel) :
    nom : str
    prenom : str 
    age : int
    email : str
    telephone : str
        