from memory.session_memory import (
    add_message,
    get_messages
)
from rag.retriever import retriever
from chains.rag_chain import rag_chain
from utils.confidence import compute_confidence

# High-risk signals that should trigger escalation.
ESCALATION_KEYWORDS = [
    "legal",
    "lawsuit",
    "gdpr",
    "chargeback",
    "refund dispute"
]


# Retrieves relevant KB chunks and computes
# retrieval confidence before generation.
def retrieve_node(state):
    question = state["question"]

    docs_and_scores = retriever.vectorstore.similarity_search_with_score(  
        question,
        k=3
    )

    docs = [doc for doc, score in docs_and_scores]  # Capturing docs only

    # Combine retrieved chunks into a single context block
    # that will be injected into the LLM prompt.
    context = "\n\n".join([
        doc.page_content for doc in docs  
    ])

    scores = [score for doc, score in docs_and_scores]  

    confidence = compute_confidence(scores)  


    state["context"] = context
    state["confidence"] = confidence

    return state



# Applies deterministic escalation rules before
# generation to avoid unsafe autonomous responses.
def router_node(state):
    question = state["question"].lower()

    if state["confidence"] < 0.4:
        state["decision"] = "ESCALATE"
        return state

    for keyword in ESCALATION_KEYWORDS:
        if keyword in question:
            state["decision"] = "ESCALATE"
            return state

    state["decision"] = "ALLOW"

    return state



# Generates grounded responses using retrieved context
# and conversation history.
def generate_node(state):
    session_id = state["session_id"]

    history_messages = get_messages(session_id)

    # Convert stored chat history into prompt-friendly text.
    history_text = "\n".join([
        f"{msg['role']}: {msg['content']}"
        for msg in history_messages
    ])

    response = rag_chain.invoke({
        "history": history_text,
        "context": state["context"],
        "question": state["question"]
    })

    add_message(
        session_id,
        "user",
        state["question"]
    )

    add_message(
        session_id,
        "assistant",
        response
    )

    state["history"] = history_text
    state["response"] = response

    return state



# Escalated queries intentionally bypass generation
# and require human review instead.
def escalation_node(state):
    session_id = state["session_id"]

    response = (
        "This query requires human escalation."
    )

    add_message(
        session_id,
        "user",
        state["question"]
    )

    add_message(
        session_id,
        "assistant",
        response
    )

    state["response"] = response

    return state