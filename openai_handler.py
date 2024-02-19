from openai import OpenAI
import json
from text_processor import TextProcessor

class OpenAIClient:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def get_completion(self, model, prompt, max_tokens):
        response = self.client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response

class CompletionSerializer:
    def __init__(self, completion):
        self.completion = completion

    def to_dict(self):
        return {
            'id': self.completion.id,
            'choices': [
                {
                    'finish_reason': choice.finish_reason,
                    'index': choice.index,
                    'logprobs': choice.logprobs,
                    'text': choice.text,
                }
                for choice in self.completion.choices
            ],
            'created': self.completion.created,
            'model': self.completion.model,
            'object': self.completion.object,
            'system_fingerprint': self.completion.system_fingerprint,
            'usage': {
                'completion_tokens': self.completion.usage.completion_tokens,
                'prompt_tokens': self.completion.usage.prompt_tokens,
                'total_tokens': self.completion.usage.total_tokens,
            }
        }

class CodeModifier:
    @staticmethod
    def count_tokens(prompt):
        return TextProcessor.tokens(prompt) + 150

    @staticmethod
    def write_to_file(file_name, content):
        with open(file_name, "w") as f:
            f.write(content)
