import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> object:
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                pass

        self.file = open(self.filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.file:
            self.file.close()

        if os.path.exists(self.filename):
            os.remove(self.filename)
