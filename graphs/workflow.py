from langgraph.graph import StateGraph
from graphs.state import GraphState

from graphs.nodes import (
    retrieve_node,
    router_node,
    generate_node,
    escalation_node
)


# LangGraph workflow controlling retrieval,
# routing, escalation, and generation flow.
workflow = StateGraph(GraphState)  

workflow.add_node("retrieve", retrieve_node)
workflow.add_node("router", router_node)
workflow.add_node("generate", generate_node)
workflow.add_node("escalate", escalation_node)

workflow.set_entry_point("retrieve") 

workflow.add_edge("retrieve", "router")  


def route_decision(state):
    return state["decision"]


# Dynamically route execution based on
# the decision produced by the router node.
workflow.add_conditional_edges(  
    "router", 
    route_decision,
    {
        "ALLOW": "generate",    
        "ESCALATE": "escalate"
    }
)

workflow.set_finish_point("generate")  
workflow.set_finish_point("escalate")

# Compile graph definition into executable workflow.
app_graph = workflow.compile()  