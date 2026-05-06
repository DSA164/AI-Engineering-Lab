# AI Engineering Lab

Personal AI engineering learning lab.

This repository organizes a 2026 learning path toward practical AI engineering, with a strong focus on:

- local LLMs;
- workflow automation;
- RAG;
- agents;
- business watch systems;
- multimodal AI;
- robotics;
- deployable AI platforms.

## Updated project sequence

| Order | Project | Focus |
|---:|---|---|
| 01 | `2026_project_01--llm_playground` | LLM sampling, inference parameters, basic experiments |
| 02 | `2026_project_02--local_llm_server` | Local LLM API server, OpenAI-compatible patterns |
| 03 | `2026_project_03--workflow_automation_lab` | n8n, JS Code Nodes, ingestion, parsing, normalization, scoring, alerts |
| 04 | `2026_project_04--rag_system` | Basic Retrieval Augmented Generation |
| 05 | `2026_project_05--rag_enterprise` | Production-grade RAG patterns |
| 06 | `2026_project_06--ai_agents_lab` | Agents, tools, state, human-in-the-loop |
| 07 | `2026_project_07--business_watch_agent` | Watch systems combining workflows, memory, retrieval and agents |
| 08 | `2026_project_08--vision_ai_lab` | Computer vision foundations |
| 09 | `2026_project_09--multimodal_assistant` | Multimodal assistant experiments |
| 10 | `2026_project_10--robot_ai_system` | Robotics AI experiments |
| 11 | `2026_project_11--ai_platform` | Integrated local AI platform |

## Learning logic

```text
LLM foundations
  ↓
workflow automation
  ↓
RAG systems
  ↓
agents
  ↓
business watch
  ↓
vision / multimodal / robotics
  ↓
AI platform
```

## Why workflow automation was added before RAG

RAG and agents require solid data-pipeline thinking.

Before building retrieval systems, it is useful to learn how to:

- fetch data;
- parse sources;
- normalize records;
- deduplicate;
- score;
- store;
- alert;
- manage uncertainty.

This is the role of `2026_project_03--workflow_automation_lab`.

Its first use case is `BD Kids Hunter`.

## Documentation

- `Learning_roadmap.md`
- `Timing_table.md`
- `docs/project_taxonomy.md`
