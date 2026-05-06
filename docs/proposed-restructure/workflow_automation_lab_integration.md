# Proposed integration — Workflow Automation Lab

## Recommendation

Add a new project after `local_llm_server` and before `rag_system`:

```text
2026_project_03--workflow_automation_lab
```

## New recommended order

```text
01 llm_playground
02 local_llm_server
03 workflow_automation_lab
04 rag_system
05 rag_enterprise
06 ai_agents_lab
07 business_watch_agent or financial_agent
08 ai_platform
09 vision_ai_lab
10 multimodal_assistant
11 robot_ai_system
```

## Reason

The previous roadmap moves quickly from local LLM foundations to RAG and agents. For enterprise AI workflows, a missing practical layer should be learned first:

- n8n
- HTTP/API ingestion
- JavaScript Code Nodes
- parsing
- normalization
- deduplication
- scoring
- storage
- alerting
- workflow robustness

## First use case

`BD Kids Hunter`: a pedagogical workflow that searches for children’s comic book lots in Belgium from 2ememain and Vinted.
