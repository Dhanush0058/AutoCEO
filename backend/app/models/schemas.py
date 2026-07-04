from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class QueryRequest(BaseModel):
    query: str

class AgentResponse(BaseModel):
    agent_name: str
    status: str
    data: Dict[str, Any]
    message: str

class OrchestratorResponse(BaseModel):
    original_query: str
    plan: str
    synthesis: str
    agent_responses: List[AgentResponse]
    requires_approval: bool
