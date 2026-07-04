from langchain_core.messages import HumanMessage
from langgraph.types import interrupt
from app.agents.state import AgentState


def approval_gate_node(state: AgentState) -> dict:
    """
    Approval gate - pauses execution for high-stakes actions.
    This is the critical "human-in-the-loop" control point.
    """
    
    if not state.get("requires_approval"):
        return state
    
    pending = state.get("pending_approval")
    if not pending:
        return state
    
    # Create approval request message
    approval_request = {
        "type": "approval_required",
        "agent": pending.get("agent"),
        "action": pending.get("action"),
        "details": pending.get("details"),
        "message": f"The {pending.get('agent')} agent is requesting approval for: {pending.get('action')}"
    }
    
    # CRITICAL: Interrupt execution here until founder approves
    # This pause will be handled by the frontend via WebSocket
    decision = interrupt(approval_request)
    
    if decision == "approved":
        return {
            "messages": [HumanMessage(content=f"Founder approved: {pending.get('action')}")],
            "next_agent": "execute",
            "requires_approval": False
        }
    else:
        return {
            "messages": [HumanMessage(content=f"Founder rejected: {pending.get('action')}")],
            "next_agent": "rejected",
            "requires_approval": False
        }


def should_request_approval(state: AgentState) -> bool:
    """Determine if we should request approval before proceeding."""
    return state.get("requires_approval", False)


def route_to_next_agent(state: AgentState) -> str:
    """Route to the appropriate next agent based on current plan."""
    next_agent = state.get("next_agent", "END")
    
    if next_agent == "finance":
        return "finance_agent"
    elif next_agent == "hr":
        return "hr_agent"
    elif next_agent == "legal":
        return "legal_agent"
    elif next_agent == "gtm":
        return "gtm_agent"
    elif next_agent == "synthesize":
        return "synthesize"
    elif next_agent == "execute":
        return "execute_approved_actions"
    else:
        return "END"
