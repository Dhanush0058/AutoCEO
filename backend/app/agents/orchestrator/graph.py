from langgraph.graph import StateGraph, END
from app.agents.orchestrator.state import AgentState
from langchain_core.messages import HumanMessage, AIMessage

def parse_intent(state: AgentState):
    # Stub intent parser
    last_message = state["messages"][-1].content.lower()
    next_agent = "finance" if "runway" in last_message or "burn" in last_message else "hr" if "hire" in last_message or "jd" in last_message else "legal" if "contract" in last_message else "gtm"
    return {"next_agent": next_agent, "plan": f"Routing to {next_agent} agent"}

def finance_agent(state: AgentState):
    return {"messages": [AIMessage(content="[Finance Agent] Current runway is 8.8 months.")], "synthesis": "Finance data retrieved."}

def hr_agent(state: AgentState):
    return {"messages": [AIMessage(content="[HR Agent] Drafted Job Description.")], "synthesis": "HR task completed."}

def legal_agent(state: AgentState):
    return {"messages": [AIMessage(content="[Legal Agent] Generated contract template.")], "synthesis": "Legal document ready."}

def gtm_agent(state: AgentState):
    return {"messages": [AIMessage(content="[GTM Agent] Competitor analysis complete.")], "synthesis": "GTM analysis ready."}

def synthesize_response(state: AgentState):
    return {"synthesis": "Final response synthesized from agents."}

# Build the graph
workflow = StateGraph(AgentState)

workflow.add_node("parse_intent", parse_intent)
workflow.add_node("finance", finance_agent)
workflow.add_node("hr", hr_agent)
workflow.add_node("legal", legal_agent)
workflow.add_node("gtm", gtm_agent)
workflow.add_node("synthesize", synthesize_response)

workflow.set_entry_point("parse_intent")

# Add conditional edges
workflow.add_conditional_edges(
    "parse_intent",
    lambda state: state["next_agent"],
    {
        "finance": "finance",
        "hr": "hr",
        "legal": "legal",
        "gtm": "gtm"
    }
)

# Route all to synthesis
for agent in ["finance", "hr", "legal", "gtm"]:
    workflow.add_edge(agent, "synthesize")

workflow.add_edge("synthesize", END)

orchestrator_graph = workflow.compile()
