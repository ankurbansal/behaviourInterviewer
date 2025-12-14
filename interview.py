
from llm_adapter import get_next_question
from history import save_history

class InterviewSession:
    """
    Manages a single interview session.
    """
    def __init__(self, scenario):
        self.scenario = scenario
        self.transcript = []
        self.history_for_llm = ""

    def _get_formatted_history(self):
        """
        Formats the transcript into a string for the LLM prompt.
        """
        formatted_history = ""
        for item in self.transcript:
            formatted_history += f"Interviewer: {item['question']}\n"
            formatted_history += f"User: {item['answer']}\n"
        return formatted_history

    def start(self):
        """
        Starts and manages the interview loop.
        """
        print("\nStarting new interview...")
        print("Type 'quit' at any time to end the interview.")
        print("-" * 20)

        next_question = self.scenario
        
        while next_question.strip().upper() != "END_INTERVIEW":
            answer = input(f"\n{next_question}\n> ")

            if answer.strip().lower() == 'quit':
                print("\nInterview ended.")
                break

            self.transcript.append({"question": next_question, "answer": answer})
            
            # Update the history for the LLM
            self.history_for_llm = self._get_formatted_history()

            print("\nThinking...")
            next_question = get_next_question(self.history_for_llm, answer)

        # Save the history
        if self.transcript:
            saved_file = save_history(self.transcript, self.scenario)
            print(f"\nInterview finished. Transcript saved to: {saved_file}")
        else:
            print("\nInterview finished. Nothing to save.")

