
import datetime

def save_history(transcript, scenario):
    """
    Saves the interview transcript to a timestamped text file.

    Args:
        transcript (list): A list of dictionaries, where each dictionary
                           has a "question" and "answer" key.
        scenario (str): The initial scenario that started the interview.

    Returns:
        str: The path to the saved file.
    """
    now = datetime.datetime.now()
    filename = f"interview_history_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write(f"# Interview Session: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## Scenario: {scenario}\n\n")

        for item in transcript:
            f.write(f"**Question:** {item['question']}\n")
            f.write(f"**Answer:** {item['answer']}\n\n")

    return filename
