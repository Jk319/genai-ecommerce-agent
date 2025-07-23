# app/utils.py
def format_response(question, result):
    if isinstance(result, str):
        return result
    if not result:
        return "No results found."
    if len(result[0]) == 1:
        return f"Answer: {result[0][0]}"
    return f"Results: {result}"
