def basic_prompt(topic):
    return f"Explain {topic} in simple terms."


def detailed_prompt(topic):
    return f"""
Explain {topic} in detail.

Include:
1. Definition
2. Key concepts
3. Example
4. Advantages
5. Conclusion
"""


def structured_prompt(topic):
    return f"""
Explain {topic} using the following structure:

Definition:
Give a clear definition.

Key Points:
List the important points.

Example:
Give one practical example.

Advantages:
Explain the main advantages.

Conclusion:
Give a short conclusion.
"""


def compare_prompts(topic):
    return {
        "Basic Prompt": basic_prompt(topic),
        "Detailed Prompt": detailed_prompt(topic),
        "Structured Prompt": structured_prompt(topic)
    }