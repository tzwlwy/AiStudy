# main.py
from cases.prompt_cases import PROMPT_CASES
from llm.client import DeepSeekLLMClient,OpenAILLMClient
from runner.prompt_runner import PromptRunner
from core.result import RunResult
from evaluator.schema_validator import SchemaValidator
from prompts.prompt_builder import PromptBuilder
from schemas.user import UserSchema


def main():
    # llm = OpenAILLMClient(
    #     api_key="YOUR_API_KEY",
    #     model="gpt-4o-mini"
    # )

    llm = DeepSeekLLMClient(
            api_key="sk-a999cb8c34f54262aee03239cba7c826",
            model="deepseek-chat"
        )
    validator = SchemaValidator()
    prompt_builder = PromptBuilder()

    # reporter = RunResult()
    runner = PromptRunner(
        llm_client=llm,
        validator=validator,
        prompt_builder=prompt_builder,
        # reporter=reporter
    )
    result = runner.run("生成一个用户", UserSchema)
    print(result)


if __name__ == "__main__":
    main()



