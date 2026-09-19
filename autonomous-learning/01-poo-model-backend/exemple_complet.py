"""
Cours 01 — POO appliquée à ModelBackend
=======================================

FICHIER DE RÉFÉRENCE PÉDAGOGIQUE

Ce fichier rassemble la syntaxe complète vue pendant le cours :
- classe et instance ;
- __init__ et self ;
- attributs ;
- type hints ;
- héritage ;
- overriding ;
- classe abstraite ;
- @abstractmethod ;
- super() ;
- polymorphisme ;
- inspection avec __dict__.

Il est volontairement plus commenté qu'un fichier de production.
Le backend vLLM est encore simulé : le prochain cours remplacera
la réponse factice par un véritable échange HTTP + JSON.
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. CLASSE ABSTRAITE : LE CONTRAT COMMUN
# ============================================================

class ModelBackend(ABC):
    """Contrat minimal commun à nos différents backends de modèles."""

    def __init__(self, name: str, device: str):
        # "self" représente l'instance actuellement construite.
        #
        # name et device sont reçus comme paramètres temporaires,
        # puis conservés comme attributs de cette instance.
        self.name = name
        self.device = device

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Générer une réponse à partir d'un prompt.

        Cette méthode est abstraite :
        ModelBackend impose son existence mais ne décide pas
        comment un backend concret doit générer la réponse.
        """
        ...


# ============================================================
# 2. BACKEND vLLM
# ============================================================

class VLLMBackend(ModelBackend):
    """Backend pédagogique représentant le futur serveur RTX 4090/vLLM."""

    def __init__(
        self,
        name: str,
        device: str,
        base_url: str,
        model: str,
    ):
        # ModelBackend sait déjà initialiser name et device.
        #
        # super() appelle donc le constructeur parent au lieu
        # de recopier :
        #
        # self.name = name
        # self.device = device
        #
        # Parent et enfant travaillent sur LA MÊME instance.
        super().__init__(name, device)

        # Ces attributs sont spécifiques au backend vLLM.
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str) -> str:
        """Implémentation concrète de generate() pour vLLM."""

        # Il s'agit d'un OVERRIDE :
        # VLLMBackend fournit l'implémentation exigée par
        # ModelBackend.
        #
        # Pour l'instant, aucune requête HTTP n'est effectuée.
        # Le prochain cours remplacera ce return par un appel
        # au serveur situé à self.base_url.
        return f"[vLLM - {self.name} sur {self.device}] {prompt}"


# ============================================================
# 3. BACKEND CLOUD
# ============================================================

class CloudBackend(ModelBackend):
    """Autre implémentation concrète du même contrat."""

    def __init__(
        self,
        name: str,
        device: str,
        base_url: str,
        model: str,
        api_key: str,
    ):
        # Initialisation des attributs communs.
        super().__init__(name, device)

        # Attributs propres au backend cloud.
        self.base_url = base_url
        self.model = model
        self.api_key = api_key

    def generate(self, prompt: str) -> str:
        """Implémentation de generate() propre au cloud."""

        # Même signature que VLLMBackend.generate(),
        # mais comportement différent.
        return f"[CLOUD - {self.name}] {prompt}"


# ============================================================
# 4. POLYMORPHISME
# ============================================================

def ask_model(model: ModelBackend, prompt: str) -> str:
    """Interroger n'importe quel backend respectant ModelBackend."""

    # Cette fonction dépend du CONTRAT, pas de l'implémentation.
    #
    # Elle ne contient donc pas :
    #
    # if isinstance(model, VLLMBackend):
    #     ...
    # elif isinstance(model, CloudBackend):
    #     ...
    #
    # Elle sait seulement qu'un ModelBackend concret possède
    # une méthode generate(prompt).
    return model.generate(prompt)


# ============================================================
# 5. CRÉATION DES INSTANCES
# ============================================================

qwen = VLLMBackend(
    name="Qwen3-30B",
    device="RTX4090",
    base_url="http://192.168.1.50:8000",
    model="Qwen/Qwen3-30B",
)

cloud_model = CloudBackend(
    name="CloudModel",
    device="Cloud",
    base_url="https://api.exemple.com",
    model="large-model",

    # Toujours fictive dans un fichier Git.
    # Ne jamais committer une vraie clé API.
    api_key="CLE_FICTIVE",
)


# ============================================================
# 6. UTILISATION
# ============================================================

response_local = ask_model(
    qwen,
    "Explique le RAG",
)

response_cloud = ask_model(
    cloud_model,
    "Explique le KV cache",
)

print(response_local)
print(response_cloud)


# ============================================================
# 7. INSPECTION DES INSTANCES
# ============================================================

# __dict__ permet ici de visualiser simplement les attributs
# stockés sur chaque instance.
print(qwen.__dict__)
print(cloud_model.__dict__)


# ============================================================
# 8. SORTIE PRINCIPALE ATTENDUE
# ============================================================

# [vLLM - Qwen3-30B sur RTX4090] Explique le RAG
# [CLOUD - CloudModel] Explique le KV cache


# ============================================================
# 9. MODÈLE MENTAL DU POLYMORPHISME
# ============================================================

# ask_model(qwen, "Explique le RAG")
#              │
#              ▼
#        model = qwen
#              │
#              ▼
#     model.generate(prompt)
#              │
#              ▼
#   VLLMBackend.generate()
#
#
# ask_model(cloud_model, "...")
#              │
#              ▼
#     model = cloud_model
#              │
#              ▼
#     model.generate(prompt)
#              │
#              ▼
#   CloudBackend.generate()


# ============================================================
# 10. CORRESPONDANCE SYNTAXE → CONCEPT
# ============================================================

# class ModelBackend(ABC)
#     → classe abstraite / contrat
#
# @abstractmethod
#     → méthode obligatoire pour les classes concrètes
#
# class VLLMBackend(ModelBackend)
#     → héritage
#
# self.name
#     → attribut de l'instance courante
#
# super().__init__(name, device)
#     → réutilisation de l'initialisation du parent
#
# VLLMBackend.generate(...)
#     → overriding
#
# model: ModelBackend
#     → ask_model dépend du contrat commun
#
# model.generate(prompt)
#     → polymorphisme
#
# qwen.__dict__
#     → inspection simple de l'instance


# ============================================================
# 11. PROCHAINE ÉTAPE
# ============================================================

# Aujourd'hui :
#
# VLLMBackend.generate()
#          │
#          └── return d'une chaîne factice
#
#
# Prochain cours :
#
# VLLMBackend.generate(prompt)
#          │
#          ▼
# construire le body JSON
#          │
#          ▼
# HTTP POST
#          │
#          ▼
# http://192.168.1.50:8000
#          │
#          ▼
# serveur vLLM / RTX 4090
#          │
#          ▼
# réponse HTTP + JSON
#          │
#          ▼
# return réponse
