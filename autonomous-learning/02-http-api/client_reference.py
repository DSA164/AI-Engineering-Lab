"""
Cours 02A — Référence complète du client HTTP
Fichier pédagogique destiné surtout à lire la syntaxe complète sur GitHub.
Le serveur /generate sera construit dans la partie 02B.
"""

import requests
from abc import ABC, abstractmethod


class ModelBackend(ABC):
    """Contrat commun aux backends."""

    def __init__(self, name: str, device: str):
        self.name = name
        self.device = device

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Retourne la génération ou laisse remonter une exception."""
        ...


class VLLMBackend(ModelBackend):
    """Client pédagogique du futur serveur RTX 4090/vLLM."""

    def __init__(
        self,
        name: str,
        device: str,
        base_url: str,
        model: str,
    ):
        super().__init__(name, device)
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str) -> str:
        # 1. Construction de l'endpoint.
        url = f"{self.base_url}/generate"

        # 2. État de l'objet + donnée de l'appel.
        payload = {
            "model": self.model,
            "prompt": prompt,
        }

        # 3. POST HTTP.
        # json=payload sérialise le dict Python en JSON.
        response = requests.post(
            url=url,
            json=payload,
            timeout=30,
        )

        # 4. Les réponses 4xx/5xx deviennent des HTTPError.
        # Nous ne capturons pas l'exception ici : elle doit pouvoir
        # remonter vers le futur ModelRouter.
        response.raise_for_status()

        # 5. JSON reçu -> objet Python.
        data = response.json()

        # 6. Contrat de succès : generate() retourne un str.
        return data["response"]


# ============================================================
# INSTANCIATION
# ============================================================

qwen = VLLMBackend(
    name="Qwen",
    device="RTX4090",
    base_url="http://192.168.1.50:8000",
    model="Qwen/Qwen3-30B",
)


# ============================================================
# UTILISATION — référence uniquement
# ============================================================

# Le serveur n'est pas encore construit, donc on ne lance pas
# automatiquement cet appel :
#
# answer = qwen.generate("Explique le RAG")
# print(answer)


# ============================================================
# CE QUI PART SUR LE RÉSEAU
# ============================================================

# Pour qwen.generate("Bonjour"), le payload vaut :
#
# {
#     "model": "Qwen/Qwen3-30B",
#     "prompt": "Bonjour"
# }
#
# Requête conceptuelle :
#
# POST /generate
# Content-Type: application/json
#
# {
#     "model": "Qwen/Qwen3-30B",
#     "prompt": "Bonjour"
# }


# ============================================================
# OÙ TRAITER LES ERREURS ?
# ============================================================

# Nous avons choisi de laisser les exceptions remonter :
#
# VLLMBackend
#      X Timeout / ConnectionError / HTTPError
#      ▼
# futur ModelRouter
#      ├── retry
#      ├── fallback M4 Max
#      └── fallback Cloud
#
# Ainsi :
# - retour normal de generate() -> str
# - échec -> exception


def pedagogical_call_example() -> None:
    """Exemple de traitement au niveau appelant."""

    try:
        answer = qwen.generate("Explique le RAG")
        print(answer)

    except requests.exceptions.ConnectionError as e:
        print("Serveur inaccessible :", e)

    except requests.exceptions.Timeout as e:
        print("Timeout :", e)

    except requests.exceptions.HTTPError as e:
        print("Erreur HTTP :", e)

    except requests.exceptions.RequestException as e:
        print("Autre erreur de requête :", e)


# La fonction n'est volontairement pas appelée automatiquement.
