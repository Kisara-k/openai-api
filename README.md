## OpenAI API Integration

This script provides a Python interface to interact with OpenAI's GPT-4 models, specifically designed for generating and processing text content in a structured manner.

Currently it takes extracted text from a lecture slide as input and generates two key outputs:
1. Detailed overview / cheat sheet of the lecture, for quick review or study.
2. A high-level transcript that provides an overview of the lecture (intended to be used in TTS).

## Features

*   Connects to OpenAI's API using environment variables for secure API key management
*   Supports multi-turn conversations with the GPT-4 model
*   Saves generated content to markdown files in an `outputs` directory
*   Includes timing metrics for API calls
*   Configurable parameters for model behavior (temperature, max\_tokens, etc.)

## Prerequisites

*   Python 3.x
*   OpenAI Python package (`openai`)
*   python-dotenv package
*   IPython (for display functionality)
*   A valid OpenAI API key

## Setup

Install the required packages:

Create a `.env` file in the project root with your OpenAI API key:

## Usage

1.  Configure your prompts and settings in `config.py`
2.  Run the script:

Ensure you have a `config.py` file with the following variables defined:

*   `system_prompt`: The system message to set the assistant's behavior
*   `user_prompt`: The initial user prompt
*   `user_prompt_2`: A follow-up prompt for the second API call
*   `clean()`: A function to process the API response content

## Output

The script generates two markdown files in the `outputs` directory:

1.  `DM 00 Introduction.md` - Contains the response to the first prompt
2.  `DM 00 Lec.md` - Contains the response to the follow-up prompt

## Configuration

The script uses the following default parameters for the OpenAI API:

*   Model: `gpt-4.1-mini`
*   Max Tokens: 10000 (for detailed, unrestraicted output)
*   Temperature: 0.3 (lower for more focused, deterministic output)
*   Top P: 0.3

These parameter values were chosen based on the analysis in [this Reddit post](https://www.reddit.com/r/ChatGPT/comments/126sr15/gpt_api_analyzing_which_temperature_and_top_p/), which explores optimal configurations for different use cases.

## Notes

*   Ensure you have sufficient API credits before running the script
*   The script includes timing metrics to monitor API call duration
*   Error handling for API rate limits or connection issues is not included in the basic implementation

```plaintext
OPENAI_KEY=your_api_key_here
```

```plaintext
pip install openai python-dotenv ipython
```
