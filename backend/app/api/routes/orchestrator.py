from fastapi import APIRouter
from app.models.schemas import QueryRequest, OrchestratorResponse
from app.agents.orchestrator.graph import orchestrator_graph
from langchain_core.messages import HumanMessage

router = APIRouter()

@router.post("/query", response_model=OrchestratorResponse)
async def handle_query(request: QueryRequest):
    # Run the graph
    initial_state = {"messages": [HumanMessage(content=request.query)], "next_agent": "", "plan": "", "requires_approval": False, "synthesis": ""}
    
    result_state = orchestrator_graph.invoke(initial_state)
    
    # Extract data from state
    plan = result_state.get("plan", "")
    synthesis = result_state.get("synthesis", "")
    agent_msgs = [m.content for m in result_state.get("messages", []) if m.type == "ai"]
    
    # Create responses format
    agent_responses = []
    for msg in agent_msgs:
        agent_responses.append({
            "agent_name": "Specialist Agent",
            "status": "success",
            "data": {},
            "message": msg
        })

    return OrchestratorResponse(
        original_query=request.query,
        plan=plan,
        synthesis=synthesis,
        agent_responses=agent_responses,
        requires_approval=result_state.get("requires_approval", False)
    )
