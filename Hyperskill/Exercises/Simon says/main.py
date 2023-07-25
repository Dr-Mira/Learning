def what_to_do(instructions):
    text = "Simon says"
    if instructions.startswith(text) or instructions.endswith(text):
        return "I " + instructions.replace(text, "").strip()
    else:
        return "I won't do it!"