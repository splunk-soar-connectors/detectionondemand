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
        value = "9f7dd79d-1e94-473d-bef9-bd405a04336a"
        self.assertEqual(_load_report_id_validator()(value), value)

    def test_rejects_path_and_noncanonical_uuid_values(self):
        validator = _load_report_id_validator()
        for value in (".", "..", "x/../../health", "9f7dd79d1e94473dbef9bd405a04336a", "{9f7dd79d-1e94-473d-bef9-bd405a04336a}"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validator(value)


if __name__ == "__main__":
    unittest.main()
