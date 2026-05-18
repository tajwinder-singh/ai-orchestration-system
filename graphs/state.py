# Shared workflow state passed between LangGraph nodes.
# Each node can read or update values during execution.
class GraphState(TypedDict):
    session_id: str
    question: str
    history: str
    context: str
    confidence: float
    decision: str
    response: str