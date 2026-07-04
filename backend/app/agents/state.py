from typing import Annotated, TypedDict, Optional
import operator
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    """State for the multi-agent orchestrator."""
    messages: Annotated[list[BaseMessage], operator.add]
    goal: str
    plan: dict
    next_agent: str
    agent_responses: list
    pending_approval: Optional[dict]
    requires_approval: bool
    current_step: int
    total_steps: int
