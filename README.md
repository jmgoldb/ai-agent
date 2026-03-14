# AI Code Agent

A learning project built while studying AI agent development. This agent uses an LLM to autonomously read, write, and execute Python files to complete programming tasks.

## Features

- File system navigation and reading
- File writing
- Python script execution via subprocess
- LLM-driven decision making

## Security Notice

This project is a learning exercise only. It allows an LLM to execute arbitrary Python code on your machine with minimal sandboxing. **Do not** distribute or expose this to untrusted input. It is not suitable for production use.

## Usage

```bash
uv run main.py <working_directory> "<prompt>"