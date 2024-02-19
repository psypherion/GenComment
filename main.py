import json
import os
import tkinter as tk
from dotenv import load_dotenv
from program_handler import ProgramHandler, CodeModifier
from openai_handler import OpenAIClient, CompletionSerializer
from text_processor import TextProcessor
from ui import FolderSelectorUI

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
API_KEY = os.getenv("OPENAI_API_KEY")

def main(folder_name):
    # Your existing main logic here
    output_directory = "Modified_Programs"
    if output_directory not in os.listdir():
        os.mkdir(output_directory)
    # Initialize OpenAIClient, ProgramHandler, CodeModifier, and TextProcessor
    openai_client = OpenAIClient(api_key=API_KEY)
    program_handler = ProgramHandler(folder_name)
    program_handler.get_program_paths()
    code_modifier = CodeModifier()
    text_processor = TextProcessor()

    # Iterate through programs and process each one
    for program_path in program_handler.program_paths:
        prompt_comments = program_handler.content(program_path)
        max_tokens = code_modifier.count_tokens(prompt_comments)
        prompt_code = """
        Here are the comments for the C program. Please add the comments to the code 
        accordingly without changing the code or the logic of the code itself.:

        Modified Code:
        """
        combined_prompt = prompt_comments + prompt_code
        
        # Use the prompt comment to generate modified code
        response = openai_client.get_completion("gpt-3.5-turbo-instruct", combined_prompt, max_tokens)

        # Serialize the Completion object
        serializer = CompletionSerializer(response)
        serialized_data = json.dumps(serializer.to_dict(), indent=2)

        # Deserialize the JSON-formatted string
        response = json.loads(serialized_data)

        # Access the "text" part
        response_text = response['choices'][0]['text'] if response['choices'] else ''

        # Write the modified code to a new file
        output_file_name = f"{output_directory}/{os.path.basename(program_path)}"
        code_modifier.write_to_file(output_file_name, response_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderSelectorUI(root)
    root.mainloop()
    selected_folder = app.get_selected_folder()
    
    if selected_folder:
        main(selected_folder)
