# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import ast
import unittest
import uuid
from pathlib import Path

CONNECTOR = Path(__file__).resolve().parents[1] / "detectionondemand_connector.py"


def _load_report_id_validator():
    source = CONNECTOR.read_text()
    tree = ast.parse(source)
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "_canonical_report_id")
    namespace = {"uuid": uuid}
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(CONNECTOR), "exec"), namespace)
    return namespace["_canonical_report_id"]


class ReportIdValidationTests(unittest.TestCase):
    def test_accepts_canonical_uuid(self):
        value = str(uuid.UUID(int=1))
        self.assertEqual(_load_report_id_validator()(value), value)

    def test_rejects_path_and_noncanonical_uuid_values(self):
        validator = _load_report_id_validator()
        canonical = str(uuid.UUID(int=1))
        for value in (".", "..", "x/../../health", canonical.replace("-", ""), f"{{{canonical}}}"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validator(value)


if __name__ == "__main__":
    unittest.main()
