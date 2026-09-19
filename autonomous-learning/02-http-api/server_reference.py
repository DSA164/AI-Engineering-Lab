"""Cours 02B — Référence serveur FastAPI / Pydantic.
Fichier pédagogique : aucun vrai LLM n'est encore chargé.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class GenerateRequest(BaseModel):
    # Champs obligatoires
    model: str
    prompt: str
    # Champs optionnels côté client, avec contraintes
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=500, ge=1)

class GenerateResponse(BaseModel):
    # Pas de défaut : le serveur doit annoncer les valeurs utilisées.
    response: str
    model: str
    temperature: float
    max_tokens: int

available_models = [
    "Qwen/Qwen3-30B",
    "Mistral/Mistral-7B",
]

app = FastAPI()

@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    # Pydantic a déjà validé la structure et les contraintes.
    # Ici commence la validation métier.
    if request.model not in available_models:
        raise HTTPException(
            status_code=404,
            detail=f"Model '{request.model}' not found",
        )

    # Simulation : aucun vrai LLM pour l'instant.
    return {
        "response": f"Reçu par {request.model} : {request.prompt}",
        "model": request.model,
        "temperature": request.temperature,
        "max_tokens": request.max_tokens,
    }

# Si ce fichier est nommé server.py :
#
# uvicorn server:app --host 0.0.0.0 --port 8000
#
# server   = module server.py
# app      = objet app = FastAPI()
# 0.0.0.0  = écoute sur toutes les interfaces IPv4
# 8000     = port
#
# Le client distant utilise la vraie IP du serveur,
# par exemple http://192.168.1.50:8000/generate
#
# STATUS À RETENIR :
# route inexistante       -> 404, generate() non appelée
# entrée Pydantic invalide-> 422, generate() non appelée
# modèle métier absent    -> 404, generate() appelée
# erreur Python non gérée -> 500
# succès                  -> 200
