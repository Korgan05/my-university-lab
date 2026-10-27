import hashlib
import json
import os
from typing import Dict

class StudentAuth:
        def __init__(self, db_file="students.json"):
                    self.db_file = db_file
                    self.students = self._load_data()

        def _load_data(self):
                    if os.path.exists(self.db_file):
                                    try:
                                                        with open(self.db_file, "r", encoding="utf-8") as f:
                                                                                return json.load(f)
                                                                        except:
                                                        return {}
                                return {}

    def _save_data(self):
                with open(self.db_file, "w", encoding="utf-8") as f:
                                json.dump(self.students, f, indent=4)

    def _hash_password(self, password):
                return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def register(self, username, password):
                if username in self.students:
                                return False
                            self.students[username] = self._hash_password(password)
        self._save_data()
        return True

    def authenticate(self, username, password):
                if username not in self.students:
                                return False
                            return self.students[username] == self._hash_password(password)

if __name__ == "__main__":
        auth = StudentAuth()
    auth.register("korgan", "password123")
    print(auth.authenticate("korgan", "password123"))
