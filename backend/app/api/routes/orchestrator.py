from fastapi import APIRouter
from app.models.schemas import QueryRequest, OrchestratorResponse
from app.agents.orchestrator.graph import orchestrator_graph
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()


@router.post("/query", response_model=OrchestratorResponse)
async def handle_query(request: QueryRequest):
    """
    Main API endpoint for the agentic orchestrator.
    Handles founder goals and routes to specialized agents.
    """
    if not os.environ.get("GOOGLE_API_KEY"):
        return OrchestratorResponse(
            original_query=request.query,
            plan="Demo Plan: Analyze financials → Review hiring → Check legal → GTM timing",
            synthesis="Demo response. Add GEMINI_API_KEY to enable AI orchestration.",
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
            requires_approval=True
        )

    try:
        initial_state = {
            "messages": [HumanMessage(content=request.query)],
            "goal": request.query,
            "plan": {},
            "next_agent": "",
            "agent_responses": [],
            "pending_approval": None,
            "requires_approval": False,
            "current_step": 0,
            "total_steps": 0
        }

        result_state = orchestrator_graph.invoke(initial_state)

        plan_dict = result_state.get("plan", {})
        plan = plan_dict.get("description", "") if isinstance(plan_dict, dict) else str(plan_dict)

        # Extract AI messages to display as agent responses in the frontend
        messages = result_state.get("messages", [])
        agent_responses = []
        for m in messages:
            # We want to ignore the HumanMessage, only extract AIMessages (the agent's output)
            if hasattr(m, 'content') and not isinstance(m, HumanMessage):
                agent_responses.append({
                    "agent_name": result_state.get("next_agent", "Specialized Agent").capitalize(),
                    "message": m.content,
                    "status": "success",
                    "data": {}
                })

        return OrchestratorResponse(
            original_query=request.query,
            plan=plan,
            synthesis=result_state.get("synthesis", "Analysis complete."),
            agent_responses=agent_responses,
            requires_approval=result_state.get("requires_approval", False)
        )
        
    except Exception as e:
        return OrchestratorResponse(
            original_query=request.query,
            plan="Error in orchestrator",
            synthesis=f"Error: {str(e)}",
            agent_responses=[],
            requires_approval=False
        )
