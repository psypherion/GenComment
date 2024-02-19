import os

def tokens(prompt):
    letter_count = sum(char.isalpha() for char in prompt)
    space_count = prompt.count(' ')
    tab_count = prompt.count('\t')
    return letter_count + space_count + tab_count

class CodeModifier:
    @staticmethod
    def count_tokens(prompt):
        return tokens(prompt) + 150

    @staticmethod
    def write_to_file(file_name, content):
        with open(file_name, "w") as f:
            f.write(content)

class ProgramHandler:
    def __init__(self, folder_name, file_ext=".c"):
        self.folder_name = folder_name
        self.file_ext = file_ext
        self.program_paths = []

    def extract_numeric_prefix(self, program_name):
        try:
            return int(program_name.split('_')[0])
        except ValueError:
            return 0

    def get_program_paths(self):
        programs_list = os.listdir(self.folder_name)
        paths = sorted(programs_list, key=self.extract_numeric_prefix)
        self.program_paths = [os.path.join(self.folder_name, program) for program in paths]

    def content(self, file_path):
        with open(file_path, "r") as f:
            content = f.read()
        return content
