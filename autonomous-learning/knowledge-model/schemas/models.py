"""Premiers data models Pydantic du parcours pédagogique."""
from typing import Literal
from pydantic import BaseModel, Field

MasteryStatus = Literal["not_started", "learning", "learned", "learned_conceptually", "mastered"]

class ConceptState(BaseModel):
    status: MasteryStatus
    evidence: list[str] = Field(default_factory=list)
    misconceptions: list[str] = Field(default_factory=list)

class Misconception(BaseModel):
    concept: str
    observed: str
    corrected: bool = False

class TeachingPolicy(BaseModel):
    no_vibecoding: bool = True
    student_writes_first: bool = True
    hints_before_solution: bool = True
    capitalize_at_end_of_block: bool = True

class NextAction(BaseModel):
    type: str
    instructions: list[str]

class CurrentSession(BaseModel):
    version: str
    current_module: str
    current_step: str
    objective: str
    previous_completed: list[str]
    next_action: NextAction
    do_not_skip: list[str] = Field(default_factory=list)
    do_not_introduce_yet: list[str] = Field(default_factory=list)
    teaching_policy: TeachingPolicy
