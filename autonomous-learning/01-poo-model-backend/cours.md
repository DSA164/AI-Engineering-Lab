# 🧠 Cours 01 — POO pour AI Engineering
## Construire l’interface `ModelBackend`

> 🎯 **OBJECTIF** — Comprendre juste assez de POO pour qu’un orchestrateur puisse utiliser un modèle sur **M4 Max**, **RTX 4090** ou **Cloud**.

---

# 🗺️ Vue d’ensemble

```text
                         ORCHESTRATEUR
                              │
                              │ generate(prompt)
                              ▼
                        ModelBackend
                       contrat commun
                              ▲
              ┌───────────────┼───────────────┐
              │               │               │
         MLXBackend      VLLMBackend      CloudBackend
              │               │               │
           M4 Max          RTX 4090         API Cloud
```

> 🔵 **CONCEPT CENTRAL**  
> L’orchestrateur ne doit pas connaître MLX, CUDA, vLLM ou l’API cloud. Il appelle simplement `backend.generate(prompt)`.

---

# 1 — Classe & instance

Une **classe** est un modèle permettant de créer des objets.

```python
class ModelBackend:
    ...
```

Une **instance** est un objet concret :

```python
qwen = ModelBackend("Qwen", "RTX4090")
```

```text
             CLASSE
          ModelBackend
               │
               ▼
            INSTANCE
              qwen
        ┌───────────────┐
        │ name = Qwen   │
        │ device = 4090 │
        └───────────────┘
```

> 🟢 **À RETENIR** — `ModelBackend` = modèle ; `qwen` = objet concret.

---

# 2 — `__init__`

```python
class ModelBackend:
    def __init__(self, name: str, device: str):
        self.name = name
        self.device = device
```

Avec :

```python
qwen = ModelBackend("Qwen", "RTX4090")
```

```text
self   → qwen
name   → "Qwen"
device → "RTX4090"

qwen
 ├── name ─────► "Qwen"
 └── device ───► "RTX4090"
```

> 🟢 **À RETENIR** — `__init__()` initialise l’état de l’instance.

---

# 3 — `self`

`self` représente **l’instance actuellement manipulée**.

```text
qwen.generate(...)
     └── self ──► qwen
                  ├── name = Qwen
                  └── device = RTX4090
```

> 🔴 **ERREUR RENCONTRÉE**
>
> ❌ `name.self = name`  
> ✅ `self.name = name`

> 🟣 **MODÈLE MENTAL** — `self.name = name` signifie : « l’attribut `name` de cet objet reçoit la valeur `name`. »

---

# 4 — Attribut ou paramètre temporaire ?

```text
ÉTAT DU BACKEND               DONNÉES D’UN APPEL
────────────────             ──────────────────
self.name                     prompt
self.device                   temperature
self.base_url                 max_tokens
self.model                    ...
```

Le prompt appartient naturellement à l’appel :

```python
def generate(self, prompt: str) -> str:
    ...
```

> 🟢 **RÈGLE PRATIQUE** — Demande : **« cette donnée décrit-elle l’objet ou seulement cette opération ? »**

---

# 5 — Méthode

```python
def generate(self, prompt: str) -> str:
    return f"[{self.name} sur {self.device}] Réponse à : {prompt}"
```

```python
qwen.generate("Explique le RAG")
```

```text
[Qwen sur RTX4090] Réponse à : Explique le RAG
```

---

# 6 — Type hints

```python
def generate(self, prompt: str) -> str:
```

```text
prompt : str        -> str
  │      │             │
  │      │             └── type de retour annoncé
  │      └──────────────── type attendu
  └─────────────────────── paramètre
```

> 🔴 **ERREUR RENCONTRÉE** — ❌ `STR` → ✅ `str`

> 🟢 **À RETENIR** — Les type hints documentent le contrat et aident les outils ; ils ne valident pas strictement les types par défaut.

---

# 7 — Héritage

```python
class LocalBackend(ModelBackend):
    ...
```

```text
              ModelBackend
                   ▲
                   │ hérite de
                   │
              LocalBackend
```

> 🔵 **CONCEPT** — Factoriser le commun dans le parent ; spécialiser ce qui change dans l’enfant.

---

# 8 — Overriding

```python
class LocalBackend(ModelBackend):
    def generate(self, prompt: str) -> str:
        return f"[LOCAL - {self.name} sur {self.device}] Réponse à : {prompt}"
```

```text
ModelBackend
    └── generate()
          ▲
          │ redéfini
LocalBackend
    └── generate() → comportement LOCAL
```

> 🟢 **À RETENIR** — L’enfant peut fournir sa propre version d’une méthode.

---

# 9 — Polymorphisme

```python
def ask_model(model: ModelBackend, prompt: str) -> str:
    return model.generate(prompt)
```

```text
                   ask_model()
                       │
                       │ generate()
                       ▼
                  ModelBackend
                       ▲
            ┌──────────┴──────────┐
            │                     │
       VLLMBackend           CloudBackend
            │                     │
            ▼                     ▼
      code vLLM              code Cloud
```

> 🟢 **FORMULE** — **Même interface, implémentations différentes.**

> 🟠 **ARCHITECTURE** — L’orchestrateur change de backend sans réécrire sa logique.

---

# 10 — Classe abstraite

`ModelBackend` représente surtout un **contrat**.

```python
from abc import ABC, abstractmethod

class ModelBackend(ABC):
    def __init__(self, name: str, device: str):
        self.name = name
        self.device = device

    @abstractmethod
    def generate(self, prompt: str) -> str:
        ...
```

```text
                  ModelBackend
                 CLASSE ABSTRAITE
                       │
               impose generate()
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
         MLX          vLLM         Cloud
     implémente    implémente    implémente
      generate      generate      generate
```

> 🔵 **CONCEPT** — La classe abstraite définit le **contrat commun**, pas le backend concret.

---

# 11 — `@abstractmethod`

```python
@abstractmethod
def generate(self, prompt: str) -> str:
    ...
```

```text
ModelBackend
     │ exige generate()
     ▼
BrokenBackend
     │
     └── generate() absent
             │
             ▼
       reste abstrait
```

---

# 12 — `pass` ou `...` ?

**`pass`** : instruction qui ne fait rien.

```python
def generate(...):
    pass
```

**`...`** : objet Python `Ellipsis`, souvent utilisé pour montrer une implémentation volontairement absente.

```python
def generate(...) -> str:
    ...
```

> 🟢 **DANS NOTRE CODE** — `...` rend visible que l’implémentation appartient aux classes concrètes.

---

# 13 — Parent : seulement le commun

```text
                         ModelBackend
                         ┌──────────┐
                         │ name     │
                         │ device   │
                         └────┬─────┘
                              │
            ┌─────────────────┼──────────────────┐
            │                 │                  │
            ▼                 ▼                  ▼
      MLXBackend         VLLMBackend        CloudBackend
      ──────────         ───────────        ────────────
      model_path         base_url           base_url
                         model              model
                                            api_key
```

> 🟠 **ARCHITECTURE** — `api_key` ne concerne pas MLX ; `model_path` ne concerne pas nécessairement le cloud. On ne les impose donc pas au parent.

> ⚠️ **QUESTION OUVERTE** — `device` convient à `M4 Max` et `RTX4090`, mais un backend cloud peut masquer le matériel réel. Nous le gardons sans surconcevoir.

---

# 14 — `super()`

```python
class VLLMBackend(ModelBackend):
    def __init__(self, name: str, device: str, base_url: str, model: str):
        super().__init__(name, device)
        self.base_url = base_url
        self.model = model
```

```text
VLLMBackend.__init__()
        │
        ├────────► super().__init__(name, device)
        │                    │
        │                    ▼
        │           ModelBackend.__init__()
        │                    │
        │             ┌──────┴──────┐
        │             ▼             ▼
        │         self.name    self.device
        │
        ├────────► self.base_url
        └────────► self.model
```

> 🟢 **À RETENIR** — `super()` ne crée pas un deuxième objet. Parent et enfant initialisent **la même instance**.

---

# 15 — 🔴 Erreur importante avec `super()`

Nous avions essayé :

```python
super().__init__(base_url, model)
```

Mais le parent attend :

```python
__init__(self, name: str, device: str)
```

Cela aurait donné :

```text
self.name   = base_url    ❌
self.device = model       ❌
```

> 🔴 **PIÈGE** — Un programme peut être **syntaxiquement valide** mais **logiquement faux**.

> 🟢 **RÉFLEXE** — Avant `super().__init__(...)`, vérifier la signature du constructeur parent.

---

# 16 — Notre `VLLMBackend`

## ⚙️ CODE DE RÉFÉRENCE

```python
class VLLMBackend(ModelBackend):
    def __init__(self, name: str, device: str, base_url: str, model: str):
        super().__init__(name, device)
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str) -> str:
        return f"[vLLM - {self.name}] {prompt}"
```

```python
qwen = VLLMBackend(
    "Qwen3-30B",
    "RTX4090",
    "http://192.168.1.50:8000",
    "Qwen/Qwen3-30B"
)
```

```text
qwen
├── name ───────► "Qwen3-30B"
├── device ─────► "RTX4090"
├── base_url ───► "http://192.168.1.50:8000"
└── model ──────► "Qwen/Qwen3-30B"
```

---

# 17 — 🧪 Inspecter l’objet

```python
print(qwen.__dict__)
```

```python
{
    'name': 'Qwen3-30B',
    'device': 'RTX4090',
    'base_url': 'http://192.168.1.50:8000',
    'model': 'Qwen/Qwen3-30B'
}
```

> 🧪 **DÉBOGAGE** — Comparer **ce que je pensais construire** ↔ **ce que Python a réellement construit**.

---

# 📌 MÉMO — POO en une page

| Notion | Forme | Idée |
|---|---|---|
| 🔵 **Classe** | `class ModelBackend:` | Modèle d’objet |
| 🔵 **Instance** | `qwen = VLLMBackend(...)` | Objet concret |
| 🔵 **self** | `self.name` | Instance courante |
| 🔵 **Initialisation** | `__init__()` | Initialise l’état |
| 🔵 **Héritage** | `VLLMBackend(ModelBackend)` | Spécialise le parent |
| 🔵 **Override** | `def generate(...)` | Redéfinit un comportement |
| 🔵 **Polymorphisme** | `model.generate(prompt)` | Même interface, comportements différents |
| 🔵 **Abstraction** | `ModelBackend(ABC)` | Définit un contrat |
| 🔵 **Méthode abstraite** | `@abstractmethod` | Impose une méthode |
| 🔵 **Parent** | `super().__init__(...)` | Réutilise l’initialisation héritée |
| 🧪 **Inspection** | `obj.__dict__` | Observe les attributs |

---

# 🧠 MODÈLE MENTAL FINAL

```text
        QU’EST-CE QUI EST COMMUN ?
                  │
                  ▼
             ModelBackend
                  │
          contrat generate()
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
       MLX       vLLM      Cloud
        │         │         │
        └──── détails spécifiques
```

### L’orchestrateur voit :

```python
backend.generate(prompt)
```

### Il ne devrait pas avoir à connaître :

```text
MLX ? CUDA ? vLLM ? HTTP ? clé API ? GPU distant ?
```

---

# 🚀 PROCHAINE ÉTAPE — HTTP

```text
Mac M4 Max                              PC RTX 4090
┌─────────────┐                         ┌─────────────┐
│ VLLMBackend │                         │ serveur LLM │
└──────┬──────┘                         └──────▲──────┘
       │          HTTP + JSON                  │
       └──────────────────────────────────────►│
       │          réponse JSON                 │
       ◄───────────────────────────────────────┘
```

À étudier :

```text
IP → port → HTTP → route → POST → headers → JSON → status code
```

---

# 🎨 Légende visuelle

- 🔵 **CONCEPT** — nouvelle notion
- 🟢 **À RETENIR** — essentiel
- 🟠 **ARCHITECTURE** — lien avec le système final
- 🔴 **PIÈGE / ERREUR** — erreur rencontrée
- 🟣 **MODÈLE MENTAL** — représentation conceptuelle
- ⚙️ **CODE** — implémentation
- 🧪 **TEST / DÉBOGAGE** — vérification

> Cette fiche utilise du **Markdown pur + Unicode/emoji**, sans dépendre de CSS ou de `<span style=...>`, afin d’être plus robuste dans les lecteurs Markdown comme MacDown3000.


---

# 🧩 EXEMPLE FINAL COMMENTÉ — Tout le cours réuni

> 🎯 **BUT** — Réunir classe abstraite, héritage, `self`, `super()`, overriding et polymorphisme dans un programme cohérent.

```python
# Outils Python pour créer une classe abstraite.
from abc import ABC, abstractmethod


# ============================================================
# 1. LE CONTRAT COMMUN
# ============================================================

class ModelBackend(ABC):

    def __init__(self, name: str, device: str):
        # Attributs communs à tous les backends.
        # "self" désigne l'instance en cours de construction.
        self.name = name
        self.device = device

    @abstractmethod
    def generate(self, prompt: str) -> str:
        # Toute classe concrète devra implémenter generate().
        ...


# ============================================================
# 2. BACKEND vLLM
# ============================================================

class VLLMBackend(ModelBackend):

    def __init__(
        self,
        name: str,
        device: str,
        base_url: str,
        model: str
    ):
        # Le parent initialise les attributs communs.
        super().__init__(name, device)

        # Attributs propres au backend vLLM.
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str) -> str:
        # Implémentation concrète de la méthode abstraite.
        # Elle est encore factice : le prochain cours
        # remplacera ceci par un véritable appel HTTP.
        return f"[vLLM - {self.name} sur {self.device}] {prompt}"


# ============================================================
# 3. BACKEND CLOUD
# ============================================================

class CloudBackend(ModelBackend):

    def __init__(
        self,
        name: str,
        device: str,
        base_url: str,
        model: str,
        api_key: str
    ):
        super().__init__(name, device)

        self.base_url = base_url
        self.model = model
        self.api_key = api_key

    def generate(self, prompt: str) -> str:
        # Même interface generate(), autre implémentation.
        return f"[CLOUD - {self.name}] {prompt}"


# ============================================================
# 4. POLYMORPHISME
# ============================================================

def ask_model(model: ModelBackend, prompt: str) -> str:
    # Cette fonction ne connaît que le contrat ModelBackend.
    # Elle n'a pas besoin de tester VLLMBackend ou CloudBackend.
    return model.generate(prompt)


# ============================================================
# 5. CRÉATION DES INSTANCES
# ============================================================

qwen = VLLMBackend(
    name="Qwen3-30B",
    device="RTX4090",
    base_url="http://192.168.1.50:8000",
    model="Qwen/Qwen3-30B"
)

cloud_model = CloudBackend(
    name="CloudModel",
    device="Cloud",
    base_url="https://api.exemple.com",
    model="large-model",
    api_key="CLE_FICTIVE"
)


# ============================================================
# 6. UTILISATION
# ============================================================

response_local = ask_model(qwen, "Explique le RAG")
response_cloud = ask_model(cloud_model, "Explique le KV cache")

print(response_local)
print(response_cloud)


# ============================================================
# 7. INSPECTION
# ============================================================

print(qwen.__dict__)
print(cloud_model.__dict__)
```

## 🖥️ Sortie principale attendue

```text
[vLLM - Qwen3-30B sur RTX4090] Explique le RAG
[CLOUD - CloudModel] Explique le KV cache
```

## 🔍 Trajet d'un appel

```text
ask_model(qwen, "Explique le RAG")
              │
              ▼
        model = qwen
              │
              ▼
     model.generate(prompt)
              │
              ▼
   VLLMBackend.generate()
```

Avec le cloud :

```text
ask_model(cloud_model, ...)
              │
              ▼
     model = cloud_model
              │
              ▼
     model.generate(prompt)
              │
              ▼
   CloudBackend.generate()
```

> 🟢 **POLYMORPHISME** — Le code appelant reste `model.generate(prompt)`, mais Python exécute l'implémentation correspondant à l'objet réel.

---

# 🔗 Où retrouver chaque concept dans le code

| Concept | Exemple |
|---|---|
| 🔵 Classe | `class VLLMBackend:` |
| 🔵 Instance | `qwen = VLLMBackend(...)` |
| 🔵 Constructeur | `def __init__(...)` |
| 🔵 `self` | `self.name` |
| 🔵 Attribut | `self.base_url` |
| 🔵 Paramètre temporaire | `prompt` |
| 🔵 Type hint | `prompt: str` |
| 🔵 Retour typé | `-> str` |
| 🔵 Héritage | `VLLMBackend(ModelBackend)` |
| 🔵 Override | `VLLMBackend.generate()` |
| 🔵 Abstraction | `ModelBackend(ABC)` |
| 🔵 Méthode abstraite | `@abstractmethod` |
| 🔵 Parent | `super().__init__(name, device)` |
| 🔵 Polymorphisme | `ask_model(model: ModelBackend, ...)` |
| 🧪 Inspection | `qwen.__dict__` |

---

# 🟠 Pourquoi ce code prépare le prochain cours

Aujourd'hui, `generate()` simule encore la réponse :

```python
return f"[vLLM - {self.name} sur {self.device}] {prompt}"
```

Au prochain chapitre, **l'architecture reste la même**, mais l'intérieur de `generate()` deviendra :

```text
generate(prompt)
      │
      ▼
préparer le JSON
      │
      ▼
HTTP POST
      │
      ▼
192.168.1.50:8000
      │
      ▼
serveur vLLM / RTX 4090
      │
      ▼
réponse HTTP + JSON
      │
      ▼
return réponse
```

> 🟢 **À RETENIR** — La POO n'était pas un exercice isolé. Nous venons de construire le squelette dans lequel nous allons maintenant brancher le réseau puis le véritable LLM.
