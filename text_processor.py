class TextProcessor:
    @staticmethod
    def tokens(prompt):
        letter_count = sum(char.isalpha() for char in prompt)
        space_count = prompt.count(' ')
        tab_count = prompt.count('\t')
        return letter_count + space_count + tab_count
