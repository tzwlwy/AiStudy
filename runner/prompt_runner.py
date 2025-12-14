import time

class PromptRunner:
    def __init__(self, llm_client, validator, prompt_builder, reporter=None):
        self.llm = llm_client
        self.validator = validator
        self.prompt_builder = prompt_builder
        self.reporter = reporter

    def run(self, user_input, schema, case_name="default", max_retry=2):
        prompt = self.prompt_builder.build(user_input)

        for attempt in range(1, max_retry + 1):
            start = time.time()
            raw = self.llm.generate(prompt)
            latency = time.time() - start

            result = self.validator.validate(raw, schema)

            if self.reporter:
                self.reporter.record_attempt(
                    case_name=case_name,
                    attempt=attempt,
                    latency=latency,
                    result=result
                )

            if result.ok:
                return result.data

            prompt = self.prompt_builder.build_retry(
                user_input,
                result.errors
            )

        raise RuntimeError("LLM output invalid after retries")
