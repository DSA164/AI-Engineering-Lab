# 🧠 Learning Knowledge Model

Cette couche rend le parcours autonome robuste entre les conversations.

## Structure

```text
ontology/
├── learning_ontology.yaml
└── curriculum.yaml
state/
├── learner_state.yaml
└── current_session.yaml
schemas/
└── models.py
```

Les YAML structurés deviennent progressivement la **source de vérité**. `LEARNING_CONTEXT.md` reste une vue humaine.

## Reprise d'une nouvelle conversation

1. Lire `state/current_session.yaml`.
2. Lire les concepts pertinents dans `state/learner_state.yaml`.
3. Résoudre les prérequis via `ontology/learning_ontology.yaml`.
4. Vérifier le module dans `ontology/curriculum.yaml`.
5. Consulter les fiches Markdown pour le détail.
6. Respecter `teaching_policy`, `do_not_skip` et `do_not_introduce_yet`.

## Choix technique

On commence par YAML + Pydantic : simple, lisible, versionnable avec Git. Neo4j/GraphRAG viendra lorsque le besoin de traversal et de retrieval graphe sera réel.
