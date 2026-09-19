# 🖥️ Cours 02B — Serveur FastAPI, Pydantic et contrats API

> 🎯 **OBJECTIF** — Recevoir le JSON du client, le valider, appliquer la logique métier et produire une réponse HTTP conforme à un contrat.

## 🗺️ Vue d'ensemble

```text
CLIENT → Uvicorn → FastAPI → Pydantic → generate()
                                      ↓
CLIENT ← JSON/HTTP ← FastAPI ← GenerateResponse
```

> 🔵 **CONCEPT CENTRAL** — Plusieurs couches interviennent avant et après notre fonction Python.

## 1 — FastAPI vs Uvicorn

**FastAPI** est le framework applicatif : routes, fonctions, validation Pydantic, réponses HTTP.

**Uvicorn** est le serveur ASGI : il fait tourner l'application et écoute réellement le réseau.

```text
CLIENT
  │ HTTP
  ▼
Uvicorn       ← réseau / port
  │ ASGI
  ▼
FastAPI       ← application / routes
```

## 2 — Route

```python
@app.post("/generate")
def generate(...):
    ...
```

Le décorateur associe `POST /generate` à la fonction située dessous.

## 3 — Contrat d'entrée

```python
class GenerateRequest(BaseModel):
    model: str
    prompt: str
```

```text
JSON → Pydantic → GenerateRequest
                    ├── request.model
                    └── request.prompt
```

> 🟢 La fonction reçoit un objet Python validé, pas un JSON brut.

## 4 — Défauts et contraintes

```python
class GenerateRequest(BaseModel):
    model: str
    prompt: str
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=500, ge=1)
```

`ge` = ≥ ; `le` = ≤.

> 🔵 `Field` déclare les contraintes ; **Pydantic effectue la validation**.

## 5 — Où intervient `generate()` ?

```text
POST /generate
      │
      ▼
FastAPI — route existe ?
  │ non → 404 (generate NON)
  ▼ oui
Pydantic — données valides ?
  │ non → 422 (generate NON)
  ▼ oui
generate()
  ├── succès → 200
  └── erreur interne non gérée → 500
```

## 6 — Contrat de sortie

```python
class GenerateResponse(BaseModel):
    response: str
```

```python
@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    ...
```

> 🔴 **ERREUR RENCONTRÉE** — `GenerateRequest` est l'entrée de la fonction ; `GenerateResponse` décrit sa sortie.

Nous avons ensuite enrichi la sortie :

```python
class GenerateResponse(BaseModel):
    response: str
    model: str
    temperature: float
    max_tokens: int
```

Pas de défaut ici : le serveur doit annoncer explicitement ce qu'il a utilisé.

## 7 — Validation structurelle vs métier

Pydantic sait vérifier :

```text
model est str ?
prompt est str ?
0 <= temperature <= 2 ?
max_tokens >= 1 ?
```

Mais la disponibilité réelle du modèle dépend de l'application.

```text
Pydantic
   │ validation structurelle
   ▼
service / generate()
   │ validation métier
   ▼
inférence
```

## 8 — Validation métier

```python
available_models = [
    "Qwen/Qwen3-30B",
    "Mistral/Mistral-7B",
]
```

```python
if request.model not in available_models:
    raise HTTPException(
        status_code=404,
        detail=f"Model '{request.model}' not found",
    )
```

> 🟣 `return` termine normalement la fonction ; `raise` l'interrompt en levant une exception.

## 9 — Guard clause

Préférer :

```python
if erreur:
    raise ...

return ...
```

à une imbrication `if/else` inutile lorsque `raise` arrête déjà le chemin.

## 10 — Réponse factice complète

```python
return {
    "response": f"Reçu par {request.model} : {request.prompt}",
    "model": request.model,
    "temperature": request.temperature,
    "max_tokens": request.max_tokens,
}
```

FastAPI sérialise ensuite la réponse standard en JSON et produit le statut de succès.

## 11 — Uvicorn

Si le fichier est `server.py` :

```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

```text
uvicorn  → serveur ASGI
server   → module server.py
app      → objet app = FastAPI()
0.0.0.0  → toutes les interfaces IPv4 d'écoute
8000     → port
```

> 🔴 `0.0.0.0` est une adresse **d'écoute**, pas l'adresse utilisée par le client.

## 🧠 Flux complet

```text
Mac / VLLMBackend
       │ dict
       ▼
requests → JSON → HTTP
       │
════ réseau ════
       ▼
    Uvicorn
       ▼
    FastAPI
       ▼
GenerateRequest / Pydantic
       ├── invalide → 422
       ▼
validation métier
       ├── modèle absent → 404
       ▼
    generate()
       ├── erreur interne → 500
       ▼
GenerateResponse
       ▼
FastAPI → JSON + 200
       │
════ réseau ════
       ▼
requests.Response → response.json()
```

## 📌 Mémo

| Notion | Rôle |
|---|---|
| `FastAPI()` | application web |
| Uvicorn | serveur ASGI / réseau |
| `@app.post()` | route POST |
| `BaseModel` | modèle Pydantic |
| `GenerateRequest` | contrat d'entrée |
| `Field` | défauts et contraintes |
| `GenerateResponse` | contrat de sortie |
| `response_model=` | schéma de sortie |
| `HTTPException` | erreur HTTP volontaire |
| `raise` | lève une exception |
| guard clause | élimine tôt un cas invalide |
| `422` | entrée invalide |
| `404` | route/ressource absente |
| `500` | erreur interne |
| `200` | succès |

## 🧩 Code complet

Voir [`server_reference.py`](./server_reference.py).

## 🚀 Étape suivante

Créer un vrai laboratoire `labs/02-http-api/` avec `uv`, FastAPI, Uvicorn et `requests`, puis tester d'abord `localhost → localhost`, avant `Mac → PC RTX 4090`.
