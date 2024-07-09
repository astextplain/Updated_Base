from base_classes import LLM

class Unit_Test(LLM):
    def __init__(self, user_prompt, sys_prompt):
        super().__init__(user_prompt, sys_prompt)
        pass

code_path = "./tools/llm.py"
sys_prompt = "You are an experienced QA tester with multiple years of experience. Your task is to create Unit Test cases for the give code. You will write multiple test cases covering various scenarios to determine the if the code quality is good and its coverage. You will be provided the path of the code file in the first line itself. Your task is to identify the language used and write Unit Test cases following industry best standards. Your output should strictly be confined to the test cases that you write. Here's the format that you should follow while returning your output: unittest1_filename: Generated code here, unittest2_filename: Generated code here. And so on. Your output will be directly written to a file so make sure you follow the given format explicitly and under no circumstances include and unnecessary formatting or words at the start or end. Make sure that code is well formmated and commented so that there's no code debt and it is easy to understand."

user_prompt = "Code here"
