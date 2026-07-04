from fastapi import APIRouter
from app.models.schemas import QueryRequest, OrchestratorResponse
from app.agents.orchestrator.graph import orchestrator_graph
from langchain_core.messages import HumanMessage
from app.config import settings

router = APIRouter()


@router.post("/query", response_model=OrchestratorResponse)
async def handle_query(request: QueryRequest):
    if not settings.OPENAI_API_KEY:
        return OrchestratorResponse(
            original_query=request.query,
            plan="Routing to finance and hr agents.",
            synthesis="Demo response. Add OPENAI_API_KEY to enable AI orchestration.",
            agent_responses=[
                {
                    "agent_name": "Finance",
                    "status": "success",
                    "data": {"current_runway": 8.8, "current_burn": 45000},
                    "message": "Calculated current financial metrics."
                },
                {
                    "agent_name": "HR",
                    "status": "success",
                    "data": {"additional_monthly_cost": 26000},
                    "message": "Calculated additional cost for 2 engineers."
                }
            ],
            requires_approval=False
        )

    initial_state = {"messages": [HumanMessage(content=request.query)], "next_agent": "", "plan": "", "requires_approval": False, "synthesis": ""}

    result_state = orchestrator_graph.invoke(initial_state)

    plan = result_state.get("plan", "")
    synthesis = result_state.get("synthesis", "")
    agent_msgs = [m.content for m in result_state.get("messages", []) if getattr(m, "type", "") == "ai"]

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
