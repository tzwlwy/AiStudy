# main.py
from cases.prompt_cases import PROMPT_CASES
from llm.client import DeepSeekLLMClient,OpenAILLMClient
from runner.prompt_runner import PromptRunner
from report.reporter import Reporter
from evaluator.schema_validator import SchemaValidator
from prompts.prompt_builder import PromptBuilder


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

    reporter = Reporter()
    runner = PromptRunner(
        llm_client=llm,
        validator=validator,
        prompt_builder=prompt_builder,
        reporter=reporter
    )
    for case in PROMPT_CASES:
        result = runner.run(
            user_input=case["input"],
            schema=case["schema"]
        )
        print(f"[{case['task']}] result:", result)


if __name__ == "__main__":
    main()



