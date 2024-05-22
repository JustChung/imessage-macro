import hashlib

class Detector:
    def __init__(self, file_path):
        self.path = file_path
        self.last_hash = self._calculate_file_hash()

    def _calculate_file_hash(self):
        with open(self.path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        return file_hash

    def is_change(self):
        current_hash = self._calculate_file_hash()
        change = current_hash != self.last_hash
        if change:
            self.last_hash = current_hash
        return change