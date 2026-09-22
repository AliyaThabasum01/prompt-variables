# 🧩 Prompt Variables

A lightweight Python CLI tool for creating reusable prompt templates with dynamic variables.

## Features

- Detect `{variables}` automatically
- Fill variables interactively
- Reuse the same prompt template
- Prevent duplicate variable prompts
- No external dependencies

## Run

```bash
python main.py
```

## Example

```text
Enter prompt template:
> Create a {type} website for {product} using a {style} design.

Fill the variables:

type: portfolio
product: AI assistant
style: futuristic

✨ Final Prompt
========================================

Create a portfolio website for AI assistant using a futuristic design.
```

## Built With

- Python
- Regular Expressions
