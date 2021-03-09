from Core.utilities.results.result import Result

class ErrorResult(Result):
    def __init__(self, message='ERROR'):
        super().__init__(False, message)
        