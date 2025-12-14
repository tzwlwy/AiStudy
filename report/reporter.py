import time


class Reporter:
    def __init__(self):
        self.records = []

    def record_attempt(self, case_name, attempt, latency, result):
        self.records.append({
            "case": case_name,
            "attempt": attempt,
            "latency": latency,
            "ok": result.ok,
            "errors": [e.code for e in result.errors],
        })

    def summary(self):
        total = len(self.records)
        success = sum(1 for r in self.records if r["ok"])
        return {
            "total_attempts": total,
            "success": success,
            "success_rate": success / total if total else 0
        }
