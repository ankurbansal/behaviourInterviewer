# Managerial Behavioral Interview Tool

This tool is designed to help aspiring and current managers practice and refine their responses to behavioral interview questions. The tool presents users with realistic workplace scenarios and uses an AI-powered interviewer to ask a series of follow-up questions. This helps users develop a structured and comprehensive framework for articulating their leadership and management capabilities, such as the STAR (Situation, Task, Action, Result) method.

## Features

*   **Scenario Library:** A collection of realistic behavioral scenarios covering common managerial challenges.
*   **AI-Powered Interactive Q&A:** The tool leverages a Large Language Model (LLM) to generate dynamic and context-aware follow-up questions, guiding you through the STAR framework in a conversational manner.
*   **Interview History:** Each interview session is saved to a local text file for you to review and analyze your performance.

## Getting Started

### Prerequisites

*   Python 3.x
*   An API key for Google's Generative AI services.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ankurbansal/behaviourInterviewer.git
    cd behaviourInterviewer
    ```

2.  Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Create a `.env` file in the root of the project and add your API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY"
    ```

### Usage

Run the application from the command line:

```bash
python main.py
```
