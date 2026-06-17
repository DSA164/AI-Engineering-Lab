# Instructions pour appliquer la structure mentorée dans `DSA164/AI-Engineering-Lab`

## Objectif

Transformer le dépôt `AI-Engineering-Lab` en laboratoire pédagogique mentoré, projet par projet, sans faire de vibecoding.

Le but n'est pas de générer du code applicatif automatiquement, mais d'ajouter une structure d'apprentissage claire autour de chaque projet : objectifs, concepts à comprendre, exercices progressifs, critères de réussite, erreurs fréquentes et journal d'apprentissage.

## Fichiers fournis

Le paquet `ai_engineering_lab_mentored_docs.zip` contient :

- `COMMIT_PLAN.md` ;
- `README.md` pour les projets 01 à 11 ;
- `MENTORING.md` pour les projets 01 à 11.

Les dossiers ciblés sont :

```text
2026_project_01--llm_playground/
2026_project_02--local_llm_server/
2026_project_03--workflow_automation_lab/
2026_project_04--rag_system/
2026_project_05--rag_enterprise/
2026_project_06--ai_agents_lab/
2026_project_07--business_watch_agent/
2026_project_08--vision_ai_lab/
2026_project_09--multimodal_assistant/
2026_project_10--robot_ai_system/
2026_project_11--ai_platform/
```

## Application locale simple

Depuis ton Mac :

```bash
cd ~/chemin/vers/AI-Engineering-Lab
unzip ~/Downloads/ai_engineering_lab_mentored_docs.zip
git status
```

Puis commit global :

```bash
git add COMMIT_PLAN.md 2026_project_*/README.md 2026_project_*/MENTORING.md
git commit -m "docs: add mentored project structure"
git push
```

## Application avec branche dédiée

Recommandé si tu veux garder un historique propre :

```bash
cd ~/chemin/vers/AI-Engineering-Lab
git checkout master
git pull
git checkout -b docs/mentored-project-structure
unzip ~/Downloads/ai_engineering_lab_mentored_docs.zip
git status
git add COMMIT_PLAN.md 2026_project_*/README.md 2026_project_*/MENTORING.md
git commit -m "docs: add mentored project structure"
git push -u origin docs/mentored-project-structure
```

Ensuite, créer une Pull Request vers `master`.

## Application avec Codex local

Lancer Codex dans le dossier du dépôt :

```bash
cd ~/chemin/vers/AI-Engineering-Lab
codex
```

Prompt conseillé pour Codex :

```text
Tu es dans le dépôt AI-Engineering-Lab.

Objectif : appliquer une structure pédagogique mentorée projet par projet.

Contraintes :
- Ne modifie aucun code applicatif.
- Ne supprime aucun fichier existant.
- Travaille uniquement sur les fichiers README.md, MENTORING.md et COMMIT_PLAN.md fournis dans le ZIP.
- Vérifie que chaque projet 2026_project_01 à 2026_project_11 possède un README.md et un MENTORING.md.
- Si un README.md existait déjà, préserve les informations utiles et enrichis-le au lieu de l'écraser sans analyse.
- Fais des commits séparés et explicites si possible.
- À la fin, affiche git status et git log --oneline -n 12.
```

## Messages de commit recommandés

Option simple :

```bash
git commit -m "docs: add mentored project structure"
```

Option projet par projet :

```bash
git commit -m "docs(project-01): add mentored LLM playground structure"
git commit -m "docs(project-02): add mentored local LLM server structure"
git commit -m "docs(project-03): add mentored workflow automation structure"
git commit -m "docs(project-04): add mentored basic RAG structure"
git commit -m "docs(project-05): add mentored enterprise RAG structure"
git commit -m "docs(project-06): add mentored AI agents structure"
git commit -m "docs(project-07): add mentored business watch agent structure"
git commit -m "docs(project-08): add mentored vision AI lab structure"
git commit -m "docs(project-09): add mentored multimodal assistant structure"
git commit -m "docs(project-10): add mentored robotics AI system structure"
git commit -m "docs(project-11): add mentored AI platform structure"
```

## Organisation pédagogique visée

Chaque projet doit idéalement contenir :

```text
README.md        # décrit le projet, son rôle et le livrable
MENTORING.md     # guide l'apprentissage, les exercices et les critères de réussite
learning_log.md  # journal personnel, à créer progressivement si utile
notes/           # notes conceptuelles
exercises/       # exercices guidés
src/             # code applicatif, si pertinent
experiments/     # essais et comparaisons
docs/            # documentation plus longue
```

## Logique globale du parcours

```text
01 LLM playground
02 Local LLM server
03 Workflow automation lab
04 Basic RAG system
05 Enterprise RAG
06 AI agents lab
07 Business watch agent
08 Vision AI lab
09 Multimodal assistant
10 Robot AI system
11 AI platform
```

## Intention pédagogique

Le parcours doit t'aider à apprendre dans cet ordre :

1. comprendre le comportement des LLM ;
2. servir un modèle localement ;
3. construire des pipelines de données ;
4. ajouter du RAG ;
5. rendre le RAG robuste ;
6. construire des agents contrôlés ;
7. appliquer ces briques à la veille ;
8. ajouter vision et multimodal ;
9. connecter l'IA à la robotique ;
10. intégrer le tout dans une plateforme locale.

## Points d'attention

- Ne pas commencer par les agents avant d'avoir compris les workflows et le RAG.
- Ne pas transformer `workflow_automation_lab` en projet RAG trop tôt.
- Ne pas confondre prototype et système robuste.
- Ajouter des critères de réussite observables dans chaque projet.
- Garder une trace des erreurs et des hypothèses dans `learning_log.md`.

## Vérifications finales

Après application :

```bash
git status
find . -maxdepth 2 -name README.md | sort
find . -maxdepth 2 -name MENTORING.md | sort
git diff --stat HEAD~1..HEAD
```

