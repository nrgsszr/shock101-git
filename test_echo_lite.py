"""Unit tests for Echo-lite."""

import unittest
from echo_lite import reply


class TestEchoLite(unittest.TestCase):

    def test_normal_message(self):
        self.assertEqual(
            reply("Hello"),
            "Echo-lite received: Hello"
        )

    def test_empty_message(self):
        self.assertEqual(
            reply(""),
            "Please enter a message."
        )

    def test_whitespace(self):
        self.assertEqual(
            reply("  Hi  "),
            "Echo-lite received: Hi"
        )

    def test_persian_message(self):
        self.assertEqual(
            reply("خوبی؟"),
            "Echo-lite received: خوبی؟"
        )

    def test_salam_greeting(self):
        self.assertEqual(
            reply("سلام"),
            "سلام! خوش آمدید."
        )

if __name__ == "__main__":
    unittest.main()
