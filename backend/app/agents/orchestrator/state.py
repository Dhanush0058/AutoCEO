from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    goal: str
    plan: dict
    next_agent: str
    pending_approval: dict | None
    synthesis: str
