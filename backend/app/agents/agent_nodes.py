from langchain_core.messages import AIMessage
from app.agents.state import AgentState
from app.config import settings


def finance_agent_node(state: AgentState) -> dict:
    """Finance agent - analyzes runway, burn, and cash flow."""
    
    response_data = {
        "agent_name": "Finance",
        "status": "success",
        "data": {
            "current_runway": 8.8,
            "current_burn": 45000,
            "total_cash": 400000,
            "monthly_revenue": 25000
        },
        "message": "Current runway is 8.8 months at current burn rate.",
        "action_required": False
    }
    
    return {
        "messages": [AIMessage(content=f"Finance Agent: {response_data['message']}")],
        "agent_responses": [response_data],
        "next_agent": "hr"
    }


def hr_agent_node(state: AgentState) -> dict:
    """HR agent - evaluates hiring decisions and headcount."""
    
    response_data = {
        "agent_name": "HR",
        "status": "success",
        "data": {
            "current_headcount": 5,
            "open_positions": 2,
            "hiring_cost_monthly": 26000,
            "impact_on_runway": -5.2
        },
        "message": "Hiring 2 engineers would reduce runway to 5.2 months.",
        "action_required": True,
        "requires_approval": True
    }
    
    return {
        "messages": [AIMessage(content=f"HR Agent: {response_data['message']}")],
        "agent_responses": [response_data],
        "next_agent": "legal",
        "requires_approval": True,
        "pending_approval": {
            "agent": "hr",
            "action": "hire_engineers",
            "details": response_data
        }
    }


def legal_agent_node(state: AgentState) -> dict:
    """Legal agent - handles contracts and compliance."""
    
    response_data = {
        "agent_name": "Legal",
        "status": "success",
        "data": {
            "compliance_status": "good",
            "pending_agreements": 1,
            "doc_type": "offer_letter"
        },
        "message": "1 offer letter ready for signature.",
        "action_required": False
    }
    
    return {
        "messages": [AIMessage(content=f"Legal Agent: {response_data['message']}")],
        "agent_responses": [response_data],
        "next_agent": "gtm"
    }


def gtm_agent_node(state: AgentState) -> dict:
    """GTM agent - market and competitor analysis."""
    
    response_data = {
        "agent_name": "GTM",
        "status": "success",
        "data": {
            "competitors": ["CorpA", "CorpB", "CorpC"],
            "market_opportunity": "expanding",
            "recommendation": "accelerate hiring to capture market"
        },
        "message": "Market timing is favorable for expansion.",
        "action_required": False
    }
    
    return {
        "messages": [AIMessage(content=f"GTM Agent: {response_data['message']}")],
        "agent_responses": [response_data],
        "next_agent": "synthesize"
    }


def synthesize_node(state: AgentState) -> dict:
    """Synthesize all agent responses into a final recommendation."""
    
    synthesis = "Based on agent analysis: Current runway is tight (8.8 months). Market timing favors expansion. Hiring would reduce runway to 5.2 months but market opportunity justifies the risk. Recommend proceeding with hiring pending your approval."
    
    return {
        "messages": [AIMessage(content=f"Synthesis: {synthesis}")],
        "synthesis": synthesis,
        "requires_approval": True
    }
