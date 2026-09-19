# 🌐 Cours 02A — HTTP, JSON et client API

> 🎯 **OBJECTIF** — Comprendre le côté client avant de construire le serveur : URL, méthode HTTP, route, headers, body JSON, réponse, status codes, exceptions et intégration dans `VLLMBackend`.

## 🗺️ Vue d'ensemble

```text
Mac M4 Max                              PC RTX 4090
CLIENT                                  SERVEUR
   │ POST /generate + JSON                 │
   ├──────────────────────────────────────►│
   │ 200 + JSON                            │
   ◄───────────────────────────────────────┤
```

> 🔵 **CONCEPT CENTRAL** — `requests` construit et envoie la requête HTTP que nous avons d'abord apprise à décomposer.

## 1 — Anatomie d'une URL

```text
http://192.168.1.50:8000/generate
│          │           │       │
protocole  machine     port    route
```

> 🔴 **ERREUR RENCONTRÉE** — `HTTP` n'est pas la route. La route est `/generate`.

## 2 — Requête HTTP

```text
POST /generate
Content-Type: application/json

{
    "prompt": "Explique le RAG"
}
```

```text
REQUÊTE
├── méthode : POST
├── route : /generate
├── header : Content-Type: application/json
└── body : données JSON
```

## 3 — Réponse HTTP

```text
HTTP/1.1 200 OK
Content-Type: application/json

{"response": "Le RAG permet..."}
```

- `200` : succès
- `404` : route/ressource absente
- `500` : erreur côté serveur
- serveur inaccessible : **aucune réponse HTTP**

> 🟢 Recevoir un `404` signifie que la communication HTTP a fonctionné : le serveur a répondu.

## 4 — JSON ≠ dictionnaire Python

```text
dict Python → sérialisation → JSON → HTTP → réseau
réseau → JSON → désérialisation → dict Python
```

## 5 — POST avec `requests`

```python
import requests

url = "http://192.168.1.50:8000/generate"
payload = {"prompt": "Explique le RAG"}

response = requests.post(url, json=payload)
```

`json=payload` demande à `requests` de sérialiser le dictionnaire en JSON et de préparer le type de contenu JSON approprié.

## 6 — L'objet `Response`

```text
response
├── status_code
├── headers
├── text
└── json()
```

```python
data = response.json()
print(data["response"])
```

> 🔴 **ERREUR RENCONTRÉE** — `response.json()` donne le contenu JSON désérialisé ; `data["response"]` sélectionne la génération.

## 7 — Timeout

```python
response = requests.post(url, json=payload, timeout=30)
```

> 🟠 Un worker lent ou bloqué ne doit pas immobiliser tout l'orchestrateur. Nous verrons plus tard retry, backoff, streaming et timeouts plus fins.

## 8 — `raise_for_status()`

```python
response.raise_for_status()
```

```text
2xx → continuer
4xx/5xx → HTTPError
```

> 🔴 **ERREUR RENCONTRÉE** — pas de `if response.raise_for_status()`. On appelle la méthode ; elle lève une exception si nécessaire.

## 9 — Exceptions

```text
RequestException
├── ConnectionError
├── Timeout
└── HTTPError
```

Les exceptions spécialisées doivent être traitées avant le cas général.

## 10 — Décision d'architecture

Nous avons comparé :

```text
A. erreur → str
B. erreur → None
C. erreur → exception qui remonte
```

Choix : **C**.

```text
VLLMBackend
     X Timeout / ConnectionError / HTTPError
     ▼
ModelRouter
├── retry ?
├── timeout adapté ?
├── fallback M4 Max ?
└── fallback Cloud ?
```

> 🟠 **Séparation des responsabilités** — Le backend sait communiquer ; le routeur décidera quoi faire si le backend échoue.

## 11 — `VLLMBackend.generate()`

```python
def generate(self, prompt: str) -> str:
    url = f"{self.base_url}/generate"

    payload = {
        "model": self.model,
        "prompt": prompt
    }

    response = requests.post(url=url, json=payload, timeout=30)
    response.raise_for_status()

    data = response.json()
    return data["response"]
```

Contrat :

```text
succès → retourne str
échec  → lève une exception
```

## 12 — POO → JSON → HTTP

Avec `self.model = "Qwen/Qwen3-30B"` et `prompt = "Bonjour"` :

```python
{
    "model": "Qwen/Qwen3-30B",
    "prompt": "Bonjour"
}
```

```text
self.model ─┐
            ├→ dict Python → JSON → HTTP POST
prompt ─────┘
```

## 📌 Mémo

| Notion | Exemple |
|---|---|
| URL | `http://192.168.1.50:8000/generate` |
| Méthode | `POST` |
| Route | `/generate` |
| Header | `Content-Type: application/json` |
| Succès | `200 OK` |
| Route absente | `404` |
| Erreur serveur | `500` |
| POST Python | `requests.post(...)` |
| JSON sortant | `json=payload` |
| JSON entrant | `response.json()` |
| Validation | `response.raise_for_status()` |
| Timeout | `timeout=30` |
| Erreur générale | `RequestException` |

## 🧩 Référence complète

Voir [`client_reference.py`](./client_reference.py).

## 🚀 Prochaine partie

Nous nous arrêtons volontairement avant FastAPI :

```text
POST /generate → FastAPI → Pydantic → generate() → réponse JSON
```

Ce sera **02B — serveur API**.
