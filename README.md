# GenComment

GenComment is a Python program that utilizes OpenAI's GPT-3.5-turbo model to automatically generate comments for programs.

## Features

- Automatically generates comments for C programs.
- Easy-to-use UI for selecting the target folder.
- Utilizes OpenAI's GPT-3.5-turbo for natural language processing.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- OpenAI GPT-3 API key (set as an environment variable or directly in the code)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ky13-troj/GenComment.git
2. Move into the directory
   
   ```bash
   cd GenComment
3. Install requirements.txt
   
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the main script :

   ```bash
   python main.py
3. A GUI will prompt you to select the target folder containing your programs.

4. The program will process each program, generate comments, and save the modified code in the "Modified_Programs" folder.


## Acknowledgement

Special thanks to OpenAI for providing the powerful GPT-3.5 model that makes this automatic code commenting tool possible.

- [OpenAI](https://openai.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Creating OpenAI API Key

To use the OpenAI API, you need to create an API key. Follow these steps:

1. Visit [OpenAI Platform](https://platform.openai.com/).
2. Sign in or create an account if you don't have one.
3. Once logged in, navigate to the API section.
4. Create a new API key by following the provided instructions.
5. Copy the generated API key.
6. Replace `"your_api_key_here"` with your actual OpenAI API key.
8. Create an .env file :
   ```bash
   OPENAI_API_KEY = 'your api key'
9. or paste this in the main file :
    ```bash
    OPENAI_API_KEY = 'your api key'

**Note:** Treat your API key as a sensitive credential and keep it secure. You can set it as an environment variable or directly use it in your code.
