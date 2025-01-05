# Forest-of-Thought (FoT) Framework

## Overview
The Forest-of-Thought (FoT) framework enhances reasoning in LLMs by building multiple reasoning trees with dynamic self-correction and sparse activation strategies. This agent implements consensus-guided decision-making with majority voting and expert evaluation, validating reasoning using benchmarks such as GSM8K, Game of 24, and MATH.

The development of this GitHub Repository was inspired by the "Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning
" Paper. To read the entire paper, visit https://arxiv.org/pdf/2412.09078 

## Directory Structure
- `core/`: Contains core logic for reasoning trees, decision-making, and benchmarks.
- `agents/`: Contains the AI agent implementation.
- `tasks/`: Manages tasks related to the agent.
- `benchmarks/`: Runs benchmarks for validation.
- `tests/`: Contains test cases for the agent.
- `docs/`: Documentation for the framework.

## Usage
To use the FoT framework, instantiate the `FoAgent` class and utilize its methods for decision-making and reasoning validation.

## Requirements
See `requirements.txt` for dependencies.
