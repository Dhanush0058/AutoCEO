from langchain_core.messages import HumanMessage, AIMessage
from app.agents.state import AgentState
from app.config import settings
import json


def parse_plan(text: str) -> dict:
    """Extract JSON plan from LLM response."""
    try:
        # Try to extract JSON from the response
        start = text.find("{")
        end = text.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(text[start:end])
    except:
        pass
    
    return {
        "steps": [
            {"agent": "finance", "task": "Analyze financial metrics"},
            {"agent": "hr", "task": "Review hiring needs"},
        ],
        "approval_required": True
    }


def orchestrator_node(state: AgentState) -> dict:
    """Main orchestrator that plans the workflow."""
    
    # Always use a basic plan (fast, reliable)
    plan = {
        "steps": [
            {"agent": "finance", "task": "Analyze financial metrics"},
            {"agent": "hr", "task": "Evaluate hiring impact"},
            {"agent": "legal", "task": "Review compliance"},
            {"agent": "gtm", "task": "Assess market timing"}
        ],
        "approval_required": True,
        "reasoning": f"Processing: {state.get('goal', 'No goal provided')}"
    }
    
    # Optional: Try Gemini for AI planning (but don't block if it fails)
    if settings.GEMINI_API_KEY:
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError
            
            def call_llm():
                llm = ChatGoogleGenerativeAI(
                    model="gemini-1.5-flash",
                    api_key=settings.GEMINI_API_KEY,
                    temperature=0.7
                )
                
                prompt = f"""You are the AutoCEO Orchestrator. Break this founder goal into a plan.

Founder Goal: {state.get('goal', 'General analysis')}

Available agents: finance, hr, legal, gtm

Return JSON with steps array and approval_required flag."""
                
                return llm.invoke([HumanMessage(content=prompt)])
            
            # Try with 3 second timeout
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(call_llm)
                response = future.result(timeout=3)
                plan = parse_plan(response.content)
                
                return {
                    "plan": plan,
                    "messages": [response],
                    "next_agent": plan.get("steps", [{}])[0].get("agent", "finance"),
                    "requires_approval": plan.get("approval_required", False),
                    "current_step": 1,
                    "total_steps": len(plan.get("steps", []))
                }
        except (FutureTimeoutError, Exception) as e:
            print(f"Gemini API error (using fallback): {str(e)[:100]}")
            # Fall through to basic plan
    
    # Fallback: return basic plan (always works)
    return {
        "plan": plan,
        "messages": [AIMessage(content=f"Plan: {json.dumps(plan)}")],
        "next_agent": "finance",
        "requires_approval": plan.get("approval_required", False),
        "current_step": 1,
        "total_steps": len(plan.get("steps", []))
    }
