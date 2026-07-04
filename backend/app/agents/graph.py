from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.orchestrator_node import orchestrator_node
from app.agents.agent_nodes import (
    finance_agent_node, hr_agent_node, legal_agent_node, gtm_agent_node, synthesize_node
)
from app.agents.approval_gate import approval_gate_node, route_to_next_agent


def build_orchestrator_graph():
    """Build the complete agentic workflow graph."""
    
    # Create the graph
    workflow = StateGraph(AgentState)
    
    # Add all nodes
    workflow.add_node("orchestrator", orchestrator_node)
    workflow.add_node("approval_gate", approval_gate_node)
    workflow.add_node("finance_agent", finance_agent_node)
    workflow.add_node("hr_agent", hr_agent_node)
    workflow.add_node("legal_agent", legal_agent_node)
    workflow.add_node("gtm_agent", gtm_agent_node)
    workflow.add_node("synthesize", synthesize_node)
    
    # Set entry point
    workflow.set_entry_point("orchestrator")
    
    # Connect orchestrator to approval gate
    workflow.add_edge("orchestrator", "approval_gate")
    
    # Conditional routing from approval gate
    workflow.add_conditional_edges(
        "approval_gate",
        route_to_next_agent,
        {
            "finance_agent": "finance_agent",
            "hr_agent": "hr_agent",
            "legal_agent": "legal_agent",
            "gtm_agent": "gtm_agent",
            "synthesize": "synthesize",
            "execute": "synthesize",
            "rejected": END,
            "END": END
        }
    )
    
    # Route all agents through approval gate before continuing
    for agent in ["finance_agent", "hr_agent", "legal_agent", "gtm_agent"]:
        workflow.add_edge(agent, "approval_gate")
    
    # Synthesize leads to end
    workflow.add_edge("synthesize", END)
    
    # Compile the graph
    orchestrator_graph = workflow.compile()
    
    return orchestrator_graph


# Create singleton instance
orchestrator_graph = build_orchestrator_graph()
