from base_classes import LLM

class Functional_Test(LLM):
    def __init__(self, user_prompt, sys_prompt):
        super().__init__(user_prompt, sys_prompt)
    