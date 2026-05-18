from langchain_core.prompts import ChatPromptTemplate

support_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a support assistant.

Answer ONLY using retrieved company policy.

If unsure, say escalation required.

Return professional responses.
"""
    ),
    (
        "user",
        """
Conversation History:
{history}

Context:
{context}

Question:
{question}
"""
    )
])