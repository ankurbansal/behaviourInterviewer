
# Technical Specification: Managerial Behavioral Interview Tool (Console App with LLM)

## 1. Overview

This document outlines the technical details for the console-based version of the Managerial Behavioral Interview Tool. This version will be enhanced with a Large Language Model (LLM) to provide a dynamic and interactive interview experience. It covers the choice of technology, application architecture, data structures, and other technical decisions.

## 2. Technology Stack

*   **Programming Language:** **Python 3**
    *   **Rationale:** Python's simplicity, readability, and strong ecosystem for AI/ML integrations make it the ideal choice.

*   **Core Libraries:**
    *   **LangChain:** A framework for developing applications powered by language models. We will use it to manage prompts, chain calls to the LLM, and manage conversation history.
    *   **Google Generative AI:** The `google-generativeai` library will be used to interact with a Google LLM (e.g., Gemini).

*   **Dependencies:** This project will have external dependencies. A `requirements.txt` file will be provided to manage these dependencies.

## 3. API Key Management

*   The application requires an API key for the Google AI service.
*   The API key must be provided through an environment variable named `GOOGLE_API_KEY`.
*   The application will check for the presence of this environment variable at startup and will provide a clear error message if it's not set.

## 4. Application Architecture

The application will be structured into several modules to ensure a clean separation of concerns.

*   **`main.py`**: The entry point of the application. It will be responsible for:
    *   Loading the environment variables (for the API key).
    *   Displaying the welcome message and instructions.
    *   Managing the main application loop.
    *   Orchestrating the interaction between the other modules.

*   **`scenarios.py`**: This module will contain the data for the initial interview scenarios.
    *   It will define a list of starting scenarios.
    *   A function will be provided to randomly select a scenario.

*   **`llm_adapter.py`**: This new module will encapsulate all interactions with the LLM.
    *   It will be responsible for initializing the LLM, creating the prompt templates, and managing the conversation chain using LangChain.
    *   It will have a function that takes the conversation history and the latest user answer, and returns the next follow-up question from the LLM.

*   **`interview.py`**: This module will manage the state of a single interview session.
    *   The `InterviewSession` class will track the conversation history (questions and answers).
    *   It will use the `llm_adapter.py` to get the next question based on the user's responses.

*   **`history.py`**: This module's role remains the same: to save the complete interview transcript to a file.

## 5. Data Structures

*   **Scenarios:** The scenarios will be stored in a simple list in `scenarios.py`.
    ```python
    SCENARIOS = [
        "Tell me about a time you had to motivate a struggling team member.",
        "Describe a situation where you had to deal with a significant change in a project.",
        # ... more scenarios
    ]
    ```

*   **Interview Transcript:** The transcript will be stored as a list of dictionaries in the `InterviewSession` object, preserving the order of the conversation.
    ```python
    self.transcript = [
        {"question": "...", "answer": "..."},
        {"question": "...", "answer": "..."},
    ]
    ```

## 6. Application Flow (Technical)

1.  **Initialization:** `main.py` is executed. It loads the `GOOGLE_API_KEY` from the environment. If not found, it exits with an error.
2.  **Main Loop:** The application enters the main menu loop.
3.  **Interview Start:** If the user chooses to start a new interview:
    a.  A random scenario is selected from `scenarios.py`. This becomes the first "question".
    b.  An `InterviewSession` object is created.
    c.  The application enters the interview loop:
        i.  The current question is presented to the user.
        ii. The user provides their answer.
        iii. The question and answer are added to the interview transcript.
        iv. The `llm_adapter.py` is called with the entire conversation history.
        v.  The LLM generates the next logical follow-up question based on the context, with the goal of guiding the user through the STAR method.
        vi. The new question is set for the next iteration of the loop.
    d.  The loop continues until the LLM determines the scenario is complete (e.g., by outputting a special "END" token or after a certain number of turns).
4.  **Interview Completion:**
    a.  The `history.py` module is called to save the full transcript to a timestamped text file.
    b.  The user is notified and shown the file path.
5.  **Loop Continuation:** The user is returned to the main menu.

## 7. File I/O

*   The file format and naming convention remain the same as in the previous specification. The content will be a log of the dynamic conversation.
