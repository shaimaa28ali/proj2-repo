# AI Task Planner Agent

## Overview

AI Task Planner Agent is a web application built with **LangChain**, **LangGraph**, **OpenAI GPT-4o-mini**, and **Flask**. It helps users organize tasks by generating summaries, subtasks, classifications, priorities, and a smart execution plan.

## Features

* Summarize user tasks using LangChain
* Build sequential chains for:

  * Task summarization
  * Word counting
  * Task classification
* AI Agents for:

  * Text summarization
  * Word counting
  * Task prioritization
* LangGraph workflow for multi-step task planning
* Flask web interface displaying:

  * Original task
  * Generated subtasks
  * Task classification
  * Priority levels
  * Smart plan

## Technologies

* Python
* LangChain
* LangGraph
* OpenAI GPT-4o-mini
* Flask
* HTML/CSS

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/AI-Task-Planner.git
cd AI-Task-Planner
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

4. Run the application:

```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000**.

## Project Workflow

User Input → Summarization → Subtask Generation → Classification → Prioritization → Smart Plan → Flask Interface

## Project Structure

```text
AI-Task-Planner/
├── app.py
├── chains/
├── agents/
├── graph/
├── templates/
├── static/
├── requirements.txt
└── README.md
```

## License

This project was developed for educational purposes.
