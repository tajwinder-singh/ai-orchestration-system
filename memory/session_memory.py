session_memory = {}


def add_message(session_id, role, content):
    if session_id not in session_memory:
        session_memory[session_id] = []

    session_memory[session_id].append({
        "role": role,
        "content": content
    })


def get_messages(session_id):
    return session_memory.get(session_id, [])