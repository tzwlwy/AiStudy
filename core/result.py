class RunResult:
    def __init__(self, success, data=None, error=None, stage=None):
        self.success = success
        self.data = data
        self.error = error
        self.stage = stage

    def __repr__(self):
        return (
            f"RunResult(success={self.success}, "
            f"data={self.data}, error={self.error}, stage={self.stage})"
        )
