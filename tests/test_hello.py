import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hello import greet


class TestHello(unittest.TestCase):
    def test_default_greeting(self) -> None:
        self.assertEqual(greet(), "Hello, GitHub Actions!")

    def test_custom_name(self) -> None:
        self.assertEqual(greet("Komal"), "Hello, Komal!")


if __name__ == "__main__":
    unittest.main()
