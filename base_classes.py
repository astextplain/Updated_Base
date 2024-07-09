from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

class LLM:
    def __init__(self, user_prompt, sys_prompt):
        self.user_prompt = user_prompt
        self.sys_temp_prompt = sys_prompt
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)
        self.test_cases = self.groq()

    def groq(self):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": self.user_prompt,
                    },
                    {
                        "role": "system",
                        "content": self.sys_temp_prompt,
                    }
                ],
                model="llama3-8b-8192",
                temperature=0.2,
            )
            test_cases = chat_completion.choices[0].message.content.strip()
            return test_cases
        
        except Exception as e:
            print(f"Error occurred while interacting with Groq API: {str(e)}")
            return None

    def display_prompts(self):
        print(f"User Prompt: {self.user_prompt}")
        print(f"System Temp Prompt: {self.sys_temp_prompt}")


if __name__ == "__main__":
    
    llm_instance = LLM(user_prompt="Enter your input:", sys_prompt="System temperature:")

    
    llm_instance.display_prompts()


    test_cases = llm_instance.groq()
    if test_cases:
        print(f"Generated test cases: {test_cases}")

