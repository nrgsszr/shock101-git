"""A small rule-based assistant for the Git mini-project."""


def reply(text: str) -> str:
    """Return a simple response to the user's message."""
    message = text.strip()

    if not message:
        return "Please enter a message."

    if message == "سلام":
        return "سلام! خوش آمدید. چطور می‌توانم کمکتان کنم؟"

    return f"Echo-lite received: {message}"


if __name__ == "__main__":
    user_input = input("You: ")
    print(reply(user_input))
