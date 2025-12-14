
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# The prompt template is the heart of the AI interviewer.
# It sets the context, the persona, the goal, and the constraints for the LLM.
PROMPT_TEMPLATE = """
You are an expert behavioral interviewer for a management position.
Your goal is to guide the candidate through the STAR method (Situation, Task, Action, Result) for a given scenario without explicitly mentioning the STAR method.
You must ask one question at a time.
Based on the user's previous answers, ask a relevant follow-up question to probe deeper into their experience.
Once you are confident that you have a complete story covering all aspects of the STAR method, you must respond with the exact string "END_INTERVIEW". Do not say anything else.

Current conversation history:
{history}

User's latest answer:
{answer}

Your next question:"""

def get_next_question(history, answer):
    """
    Gets the next interview question from the LLM based on the conversation history.

    Args:
        history (str): The history of the conversation so far.
        answer (str): The user's latest answer.

    Returns:
        str: The next question from the LLM, or "END_INTERVIEW".
    """
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

        prompt = PromptTemplate(
            template=PROMPT_TEMPLATE,
            input_variables=["history", "answer"]
        )

        chain = LLMChain(llm=llm, prompt=prompt)

        response = chain.invoke({
            "history": history,
            "answer": answer
        })

        return response['text'].strip()

    except Exception as e:
        # This is a fallback in case the LLM fails for any reason
        print(f"Error interacting with LLM: {e}")
        return "END_INTERVIEW"

if __name__ == '__main__':
    # Example usage for testing
    test_history = "Initial Question: Tell me about a time you had to motivate a struggling team member."
    test_answer = "I had a team member, John, who was new to the team and was having a hard time keeping up with the pace of the project. He seemed disengaged."

    next_q = get_next_question(test_history, test_answer)
    print(f"Next Question: {next_q}")
