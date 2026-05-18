from flask import Flask, request, jsonify
from graphs.workflow import app_graph
import uuid

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    question = data.get("question")
    session_id = data.get("session_id")

    # Generate a new session automatically
    # for first-time conversations.
    if not session_id:
        session_id = str(uuid.uuid4())

    # Initial workflow state passed into LangGraph execution.
    result = app_graph.invoke({
        "session_id": session_id,
        "question": question,
        "history": "",
        "context": "",
        "confidence": 0.0,
        "decision": "",
        "response": ""
    })


    return jsonify({
        "session_id": session_id,
        "decision": result["decision"],
        "confidence": float(result["confidence"]),
        "response": result["response"]
    })


if __name__ == "__main__":
    app.run(debug=True)