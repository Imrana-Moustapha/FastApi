from fastapi import FastAPI, HTTPException, status
from model.users import Users
from typing import List

app = FastAPI(
    title="My First Todo API", 
    version="1.0.0",
    description="Une API simple pour gérer une liste d'utilisateurs/todos."
)

# Simulation de base de données
users_list: List[Users] = []

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    """Page d'accueil de l'API."""
    return {"Hello": "World"}

@app.get("/users", response_model=List[Users], tags=["Users"])
async def get_users():
    """Récupérer la liste de tous les utilisateurs."""
    return users_list

@app.get("/users/{user_id}", response_model=Users, tags=["Users"])
async def get_user_by_id(user_id: int):
    """Récupérer un utilisateur spécifique via son ID (index)."""
    try:
        return users_list[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )

@app.post("/users", response_model=Users, status_code=status.HTTP_201_CREATED, tags=["Users"])
async def create_user(user: Users):
    """Créer un nouvel utilisateur."""
    users_list.append(user)
    return user

@app.put("/users/{user_id}", response_model=Users, tags=["Users"])
async def update_user(user_id: int, updated_user: Users):
    """Remplacer complètement un utilisateur existant."""
    try:
        users_list[user_id] = updated_user
        return updated_user
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    
@app.delete("/users/{user_id}", response_model=Users, tags=["Users"])
async def delete_user(user_id: int):
    """Supprimer un utilisateur de la liste."""
    try:
        return users_list.pop(user_id)
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )