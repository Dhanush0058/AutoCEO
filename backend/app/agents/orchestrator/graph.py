import os
import json
from pathlib import Path
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from app.agents.orchestrator.state import AgentState
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(BASE_DIR / ".env")

# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

def orchestrator_node(state: AgentState):
    # If a goal is already set and not the first run, we might skip. But for now let's just parse intent.
    last_message = state["messages"][-1].content
    
    prompt = f"""You are the AutoCEO Orchestrator.
    Break this founder goal into subtasks and decide which specialized agent should handle it first.
    Available agents: finance, hr, legal, gtm.
    
    Goal: {last_message}
    
    Return ONLY a JSON object exactly matching this format, with no markdown formatting or extra text:
    {{
      "plan": "Brief explanation of the plan",
      "next_agent": "finance|hr|legal|gtm"
    }}
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Simple JSON extraction (stripping backticks if present)
    content = response.content.replace("```json", "").replace("```", "").strip()
    
    try:
        plan_data = json.loads(content)
        next_agent = plan_data.get("next_agent", "finance")
        plan_desc = plan_data.get("plan", "Default plan")
    except Exception as e:
        next_agent = "finance" # fallback
        plan_desc = "Failed to parse JSON, falling back to finance agent."
        
    return {
        "plan": {"description": plan_desc},
        "next_agent": next_agent,
        "goal": last_message
    }

def finance_agent(state: AgentState):
    return {"messages": [AIMessage(content="[Finance Agent] Analyzed runway based on current burn rate.")], "synthesis": "Finance data retrieved."}

def hr_agent(state: AgentState):
    return {"messages": [AIMessage(content="[HR Agent] Prepared draft Job Description and offer templates.")], "synthesis": "HR task completed."}

def legal_agent(state: AgentState):
    return {"messages": [AIMessage(content="[Legal Agent] Generated contract templates and compliance checks.")], "synthesis": "Legal document ready."}

def gtm_agent(state: AgentState):
    return {"messages": [AIMessage(content="[GTM Agent] Competitor analysis and GTM strategy outlined.")], "synthesis": "GTM analysis ready."}

def synthesize_response(state: AgentState):
    return {"synthesis": "Final response synthesized from agents."}

# Build the graph
workflow = StateGraph(AgentState)

workflow.add_node("orchestrator", orchestrator_node)
workflow.add_node("finance", finance_agent)
workflow.add_node("hr", hr_agent)
workflow.add_node("legal", legal_agent)
workflow.add_node("gtm", gtm_agent)
workflow.add_node("synthesize", synthesize_response)

workflow.set_entry_point("orchestrator")

# Add conditional edges
workflow.add_conditional_edges(
    "orchestrator",
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
