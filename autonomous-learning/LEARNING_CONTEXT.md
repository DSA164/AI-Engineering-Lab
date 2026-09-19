# 🧭 LEARNING_CONTEXT --- Parcours autonome AI Engineering

> **Rôle de ce fichier**\
> Ce document est le **passage de relais pédagogique entre les
> conversations**.\
> Il ne remplace pas les fiches de cours. Il indique où en est
> l'apprentissage, ce qui est acquis, ce qui reste fragile, les
> décisions d'architecture prises et la prochaine étape.
>
> **Instruction de reprise**\
> Dans une nouvelle conversation : **lire ce fichier avant de reprendre
> le parcours autonome**, puis consulter les fiches `cours.md`
> concernées si davantage de détail est nécessaire.

------------------------------------------------------------------------

# 🎯 Objectif général

Construire progressivement les connaissances permettant de concevoir et
exploiter de manière autonome une architecture de **second cerveau local
/ système agentique**, sans vibecoding.

Architecture cible à terme :

``` text
                         UTILISATEUR
                              │
                              ▼
                        ORCHESTRATEUR
                              │
                ┌─────────────┼─────────────┐
                │             │             │
              RAG          MÉMOIRE        OUTILS
                │             │             │
                └─────────────┼─────────────┘
                              │
                              ▼
                         MODEL ROUTER
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
          M4 Max          RTX 4090           Cloud
           MLX             vLLM/API        gros modèles
```

------------------------------------------------------------------------

# 🧑‍🏫 Méthode pédagogique à conserver

## Principes

-   **Ne pas vibecoder.**
-   Agir comme mentor pédagogique.
-   Expliquer le concept avant ou pendant sa mise en pratique.
-   Faire écrire le code à l'apprenant.
-   Donner des indices avant de donner une solution.
-   Corriger le code en expliquant **pourquoi**.
-   Ne donner une solution complète que lorsqu'elle est demandée ou
    lorsqu'elle sert de référence de fin de cours.
-   Relier les concepts au projet final de second cerveau local.
-   Préférer de petits exercices successifs.
-   Introduire les frameworks après compréhension des mécanismes
    sous-jacents.
-   Distinguer systématiquement :
    -   syntaxe ;
    -   modèle mental ;
    -   responsabilité architecturale.

## Ratio visé

``` text
≈ 70 % pratique
≈ 30 % théorie
```

------------------------------------------------------------------------

# 📚 Convention de capitalisation

À la fin de chaque bloc cohérent :

``` text
autonomous-learning/
└── XX-module/
    ├── cours*.md
    └── *_reference.py
```

## Fiche Markdown

Doit privilégier :

-   Markdown pur ;
-   structure aérée ;
-   schémas textuels ;
-   exemples liés au projet ;
-   erreurs réellement rencontrées ;
-   mémo final ;
-   transition vers l'étape suivante.

Code visuel :

``` text
🔵 CONCEPT
🟢 À RETENIR
🟠 ARCHITECTURE
🔴 PIÈGE / ERREUR
🟣 MODÈLE MENTAL
⚙️ CODE
🧪 TEST / DÉBOGAGE
```

## Fichier Python de référence

Le fichier `*_reference.py` :

-   n'est pas nécessairement destiné à la production ;
-   peut ne pas être exécuté automatiquement ;
-   sert surtout à **lire la syntaxe complète sur GitHub** ;
-   contient imports, définitions, implémentations, instanciations,
    exemples d'exécution et commentaires ;
-   relie explicitement chaque morceau de syntaxe au concept étudié.

------------------------------------------------------------------------

# 🧰 Environnement et stratégie matérielle

Point de départ du parcours :

``` text
MacBook Pro M4 Max 64 Go
    │
    ├── orchestration
    ├── mémoire
    ├── MLX / modèles locaux adaptés
    └── client / développement

PC
Ryzen 9 7950X3D
RTX 4090 24 Go
32 Go RAM
    │
    ├── workers GPU
    ├── inférence CUDA
    └── futur serveur vLLM/API

Cloud
    │
    └── recours ponctuel pour modèles trop gros
```

Principe architectural : rendre les backends interchangeables derrière
un contrat commun.

------------------------------------------------------------------------

# 📊 Diagnostic initial

Niveau observé au début du parcours :

  ------------------------------------------------------------------------
  Domaine                        Niveau approximatif Observation
  --------------------- ---------------------------- ---------------------
  Python général                                 2/3 bonnes bases
                                                     pratiques

  Structures de données                          2/3 compréhension
                                                     correcte

  POO / classes                        1/3 au départ remise à niveau
                                                     effectuée

  `async/await`                                0.5/3 encore à travailler

  Environnements Python                          2/3 Conda/Poetry déjà
                                                     vus, préférence pour
                                                     `uv`

  HTTP / API                         1.5/3 au départ notions désormais
                                                     consolidées

  Réseau                                         2/3 bonnes bases

  Linux                                          2/3 suffisant pour
                                                     avancer

  Git                                            2/3 workflow compris

  Docker                                         1/3 déjà utilisé, pas
                                                     encore maîtrisé

  SQL                                            2/3 bonne lecture des
                                                     requêtes
  ------------------------------------------------------------------------

------------------------------------------------------------------------

# ✅ Cours 01 --- POO appliquée à `ModelBackend`

## État

**Terminé et capitalisé.**

Fichiers :

``` text
autonomous-learning/01-poo-model-backend/
├── cours.md
└── exemple_complet.py
```

## Concepts acquis

-   classe ;
-   instance ;
-   `__init__` ;
-   `self` ;
-   attribut vs paramètre temporaire ;
-   méthodes ;
-   type hints ;
-   héritage ;
-   overriding ;
-   polymorphisme ;
-   `ABC` ;
-   `@abstractmethod` ;
-   `pass` vs `...` ;
-   `super()` ;
-   inspection simple avec `__dict__`.

## Architecture obtenue

``` text
                         ModelBackend
                         [abstrait]
                              │
                        generate()
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
      MLXBackend         VLLMBackend         CloudBackend
        M4 Max            RTX 4090              API
```

## Points ayant demandé consolidation

-   syntaxe des type hints ;
-   sens exact de `self` ;
-   appel du constructeur parent avec `super()` ;
-   distinction attribut durable / paramètre temporaire ;
-   différence entre classe abstraite et implémentation concrète.

------------------------------------------------------------------------

# ✅ Cours 02A --- HTTP, JSON et client API

## État

**Terminé et capitalisé.**

Fichiers :

``` text
autonomous-learning/02-http-api/
├── cours.md
└── client_reference.py
```

## Concepts acquis

-   protocole HTTP au niveau applicatif ;
-   URL ;
-   IP ;
-   port ;
-   route / endpoint ;
-   `POST` ;
-   headers ;
-   body ;
-   JSON ;
-   status codes ;
-   objet `requests.Response` ;
-   `response.status_code` ;
-   `response.json()` ;
-   sérialisation via `json=payload` ;
-   timeout ;
-   `raise_for_status()` ;
-   exceptions `requests`.

## Status travaillés

``` text
200 → succès
404 → ressource/route absente
500 → erreur interne serveur
```

Puis distinction :

``` text
aucune réponse HTTP → problème de connexion / transport
réponse 4xx/5xx     → serveur joint mais erreur HTTP
```

## Exceptions travaillées

``` text
RequestException
├── ConnectionError
├── Timeout
└── HTTPError
```

## Décision architecturale importante

Le `VLLMBackend` **ne transforme pas les erreurs réseau en chaînes**.

Contrat retenu :

``` text
generate(prompt)
├── succès → retourne str
└── échec  → exception qui remonte
```

Pourquoi :

``` text
VLLMBackend
     X Timeout / ConnectionError / HTTPError
     ▼
ModelRouter
├── retry
├── timeout adapté
├── fallback M4 Max
└── fallback Cloud
```

Le backend communique ; le routeur décide de la stratégie d'échec.

## Version conceptuelle actuelle

``` python
def generate(self, prompt: str) -> str:
    url = f"{self.base_url}/generate"

    payload = {
        "model": self.model,
        "prompt": prompt
    }

    response = requests.post(
        url=url,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]
```

## Points ayant demandé consolidation

-   HTTP ≠ mécanisme de vérification des paquets ;
-   route ≠ protocole ;
-   body JSON ≠ simple mot « JSON » ;
-   `Response` ≠ réponse du LLM directement ;
-   `status_code` est un attribut, pas une méthode ;
-   `raise_for_status()` n'est pas un booléen ;
-   `return exception` ≠ `raise exception`.

------------------------------------------------------------------------

# ✅ Cours 02B --- Serveur FastAPI / Pydantic

## État

**Terminé et capitalisé avant passage au laboratoire.**

Fichiers :

``` text
autonomous-learning/02-http-api/
├── cours_02B_server.md
└── server_reference.py
```

## Concepts acquis

-   FastAPI ;
-   Uvicorn ;
-   ASGI au niveau conceptuel ;
-   décorateur `@app.post(...)` ;
-   `BaseModel` ;
-   `GenerateRequest` ;
-   valeurs par défaut ;
-   `Field` ;
-   contraintes `ge` / `le` ;
-   validation Pydantic ;
-   `GenerateResponse` ;
-   `response_model` ;
-   validation d'entrée vs validation de sortie ;
-   validation structurelle vs validation métier ;
-   `HTTPException` ;
-   `raise` vs `return` ;
-   guard clause ;
-   adresse d'écoute `0.0.0.0`.

## Contrat d'entrée actuel

``` python
class GenerateRequest(BaseModel):
    model: str
    prompt: str
    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0
    )
    max_tokens: int = Field(
        default=500,
        ge=1
    )
```

## Contrat de sortie actuel

``` python
class GenerateResponse(BaseModel):
    response: str
    model: str
    temperature: float
    max_tokens: int
```

Les valeurs de sortie n'ont volontairement pas de défaut : le serveur
doit annoncer explicitement les valeurs réellement utilisées.

## Validation métier actuelle

``` python
available_models = [
    "Qwen/Qwen3-30B",
    "Mistral/Mistral-7B",
]
```

Puis guard clause :

``` python
if request.model not in available_models:
    raise HTTPException(
        status_code=404,
        detail=f"Model '{request.model}' not found"
    )
```

## Status consolidés

``` text
route inexistante
    → 404
    → generate() non appelée

entrée Pydantic invalide
    → 422
    → generate() non appelée

modèle métier inexistant
    → 404 volontaire
    → generate() appelée

exception Python non gérée dans generate()
    → 500

succès
    → 200
```

## Distinction importante

``` text
VALIDATION STRUCTURELLE
Pydantic
│
├── types
├── champs obligatoires
└── contraintes

VALIDATION MÉTIER
application / service
│
├── modèle disponible ?
├── modèle chargé ?
├── GPU disponible ?
└── autorisation ?
```

## FastAPI vs Uvicorn

``` text
CLIENT
  │ HTTP
  ▼
Uvicorn       ← serveur ASGI, écoute réseau / port
  │
  ▼
FastAPI       ← application, routes, validation, logique HTTP
```

Commande comprise :

``` bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

Décomposition :

``` text
server   → module server.py
app      → objet app = FastAPI()
0.0.0.0  → toutes les interfaces IPv4 d'écoute
8000     → port
```

Le client distant utilise la vraie IP du serveur, **pas `0.0.0.0`**.

## Points ayant demandé consolidation

-   modèle d'entrée vs modèle de sortie ;
-   Pydantic vs logique métier ;
-   `Field` déclare les contraintes, Pydantic les applique ;
-   4xx vs 5xx ;
-   `raise` vs `return` ;
-   rôle respectif de FastAPI et Uvicorn.

------------------------------------------------------------------------

# 🧠 Flux global désormais compris

``` text
Mac / VLLMBackend
       │
       │ dict Python
       ▼
requests
       │
       ▼
JSON + HTTP
       │
══════ RÉSEAU ══════
       │
       ▼
Uvicorn
       │
       ▼
FastAPI
       │
       ▼
GenerateRequest / Pydantic
       │
       ├── invalide → 422
       │
       ▼
validation métier
       │
       ├── modèle absent → 404
       │
       ▼
generate()
       │
       ├── erreur interne → 500
       │
       ▼
GenerateResponse
       │
       ▼
FastAPI
       │
       ▼
JSON + 200
       │
══════ RÉSEAU ══════
       │
       ▼
requests.Response
       │
       ▼
raise_for_status()
       │
       ▼
response.json()
       │
       ▼
data["response"]
```

------------------------------------------------------------------------

# 🚦 État pédagogique actuel

## Considéré acquis pour avancer

``` text
✅ bases POO nécessaires
✅ abstraction ModelBackend
✅ client HTTP synchrone
✅ JSON
✅ status HTTP fondamentaux
✅ exceptions requests
✅ contrat API
✅ validation Pydantic
✅ FastAPI conceptuel
✅ Uvicorn conceptuel
```

## À ne pas considérer encore acquis

``` text
⏳ environnement uv de projet en pratique
⏳ exécution réelle FastAPI/Uvicorn
⏳ curl
⏳ localhost / interfaces en pratique
⏳ firewall / réseau Mac ↔ PC
⏳ async / await
⏳ concurrence
⏳ vrai serveur LLM
⏳ API OpenAI-compatible
⏳ streaming
⏳ retry / backoff
⏳ ModelRouter réel
```

------------------------------------------------------------------------

# 🚀 PROCHAINE ÉTAPE EXACTE

## Lab 01 --- API locale

Créer un laboratoire séparé :

``` text
AI-Engineering-Lab/
└── labs/
    └── 02-http-api/
```

### Étape 1

``` bash
uv init
uv add fastapi uvicorn requests
```

Puis **lire et comprendre `pyproject.toml`**.

### Étape 2

Écrire soi-même un premier :

``` text
server.py
```

à partir des concepts appris, sans copier immédiatement
`server_reference.py`.

### Étape 3

Lancer :

``` text
localhost → localhost
```

et observer réellement :

-   Uvicorn ;
-   route `/generate` ;
-   `200` ;
-   `404` ;
-   `422`.

### Étape 4

Créer le client réel et tester :

``` text
client Python → serveur FastAPI
```

### Étape 5

Passer ensuite à :

``` text
Mac M4 Max
     │
     │ réseau local
     ▼
PC 7950X3D + RTX 4090
```

### Étape 6

Seulement après validation de l'API réseau :

``` text
brancher un vrai backend LLM
```

------------------------------------------------------------------------

# 🔭 Suite prévue du parcours

``` text
Lab API réelle
    ↓
async / await
    ↓
inférence locale
    ↓
ModelRouter
    ↓
RAG
    ↓
RAG avancé + évaluation
    ↓
agents
    ↓
orchestration multi-agent
    ↓
mémoire
    ↓
GraphRAG
    ↓
production / observabilité
```

------------------------------------------------------------------------

# 📝 Règle de mise à jour de ce fichier

À chaque fin de bloc significatif :

1.  mettre à jour **État pédagogique actuel** ;
2.  déplacer les notions maîtrisées vers **acquis** ;
3.  noter les erreurs ou confusions qui ont nécessité plusieurs
    itérations ;
4.  enregistrer les décisions architecturales prises ;
5.  définir **une prochaine étape exacte**, pas seulement un objectif
    vague ;
6.  conserver ce fichier comme point d'entrée de la conversation
    suivante.

> **Ne pas utiliser ce fichier comme substitut aux exercices.**\
> Il sert à préserver la continuité pédagogique, pas à donner les
> solutions à l'avance.
