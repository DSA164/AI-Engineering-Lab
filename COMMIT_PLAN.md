# Commit plan — Mentored documentation

Direct GitHub write access was refused by the connector with HTTP 403, so these files are provided as a ready-to-copy package.

Recommended commit strategy:

## Option A — one clean documentation commit

```bash
git add 2026_project_*/README.md 2026_project_*/MENTORING.md
git commit -m "docs: add mentored README and MENTORING files for AI Engineering Lab projects"
```

Commit description:

```text
Adds pedagogical README.md and MENTORING.md files for projects 01 to 11.
Each project now includes learning goals, guided exercises, a minimal milestone,
a final deliverable, validation criteria, and anti-vibecoding mentoring rules.
```

## Option B — project-by-project commits

```bash
git add 2026_project_01--llm_playground/README.md 2026_project_01--llm_playground/MENTORING.md
git commit -m "docs(project-01): add mentored LLM playground structure"

git add 2026_project_02--local_llm_server/README.md 2026_project_02--local_llm_server/MENTORING.md
git commit -m "docs(project-02): add mentored local LLM server structure"

git add 2026_project_03--workflow_automation_lab/README.md 2026_project_03--workflow_automation_lab/MENTORING.md
git commit -m "docs(project-03): add mentored workflow automation structure"

git add 2026_project_04--rag_system/README.md 2026_project_04--rag_system/MENTORING.md
git commit -m "docs(project-04): add mentored basic RAG structure"

git add 2026_project_05--rag_enterprise/README.md 2026_project_05--rag_enterprise/MENTORING.md
git commit -m "docs(project-05): add mentored enterprise RAG structure"

git add 2026_project_06--ai_agents_lab/README.md 2026_project_06--ai_agents_lab/MENTORING.md
git commit -m "docs(project-06): add mentored AI agents lab structure"

git add 2026_project_07--business_watch_agent/README.md 2026_project_07--business_watch_agent/MENTORING.md
git commit -m "docs(project-07): add mentored business watch agent structure"

git add 2026_project_08--vision_ai_lab/README.md 2026_project_08--vision_ai_lab/MENTORING.md
git commit -m "docs(project-08): add mentored vision AI lab structure"

git add 2026_project_09--multimodal_assistant/README.md 2026_project_09--multimodal_assistant/MENTORING.md
git commit -m "docs(project-09): add mentored multimodal assistant structure"

git add 2026_project_10--robot_ai_system/README.md 2026_project_10--robot_ai_system/MENTORING.md
git commit -m "docs(project-10): add mentored robot AI system structure"

git add 2026_project_11--ai_platform/README.md 2026_project_11--ai_platform/MENTORING.md
git commit -m "docs(project-11): add mentored AI platform structure"
```
