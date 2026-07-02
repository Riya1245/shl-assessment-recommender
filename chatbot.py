from app.retriever import recommend


def generate_response(messages):

    user_message = messages[-1].content.lower()

    comparison = compare_assessments(user_message)

    if comparison:
        return comparison

    # Off topic questions
    if any(word in user_message for word in [
        "weather",
        "movie",
        "cricket",
        "football",
        "legal",
        "lawyer",
        "recipe"
    ]):
        return {
            "reply": "I can only help with SHL assessment recommendations.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Prompt injection protection
    if any(word in user_message for word in [
        "ignore previous",
        "system prompt",
        "developer prompt"
    ]):
        return {
            "reply": "Sorry, I can only answer questions related to SHL assessments.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Clarifying question
    if len(user_message.split()) < 4:
        return {
            "reply": "Could you tell me the job role, experience level, and whether you need technical, cognitive, or personality assessments?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Retrieve recommendations
    recommendations = recommend(user_message)

    return {
        "reply": "Based on your requirements, here are the most relevant SHL assessments.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }


def compare_assessments(query):

    query = query.lower()

    if "opq" in query and "gsa" in query:
        return {
            "reply": "OPQ32r measures personality traits, whereas GSA measures general cognitive ability.",
            "recommendations": [],
            "end_of_conversation": False
        }

    return None

