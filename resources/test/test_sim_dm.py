import unittest
import subprocess

pyton_bin_path = "../../venv/Scripts/python.exe"


def remove_leading_whitespace(text):
    return "\n".join(line.lstrip() for line in text.splitlines())


class TestSimDM(unittest.TestCase):
    """
    测试用例不用给老师
    """

    def setUp(self):
        self.maxDiff = None  # 允许显示完整的 diff

    def test_sim_dm_output(self):
        test_cases = [
            (
                "first.trace 16 1 4".split(" "),
                """first.trace
                Processing your program trace, progress so far = 0 %
                set and tag of 0x0 is 0 0
                address 0x0 CACHE MISS. Loading from memory.
                set and tag of 0x4 is 1 0
                address 0x4 CACHE MISS. Loading from memory.
                set and tag of 0x8 is 2 0
                address 0x8 CACHE MISS. Loading from memory.
                set and tag of 0xc is 3 0
                address 0xc CACHE MISS. Loading from memory.
                set and tag of 0x10 is 0 1
                address 0x10 CACHE MISS. Loading from memory.
                set and tag of 0xc is 3 0
                address 0xc CACHE HIT. Good Job.
                set and tag of 0x10 is 0 1
                address 0x10 CACHE HIT. Good Job.
                set and tag of 0x3c is 3 3
                address 0x3c CACHE MISS. Loading from memory.
                total cache misses 6
                miss_rate 0.75
                hit_rate 0.25
                Finished processing your program trace, progress = 100.0 %
                """),
            ("first.trace 16 1 8".split(" "),
             """first.trace
            Processing your program trace, progress so far = 0 %
            set and tag of 0x0 is 0 0
            address 0x0 CACHE MISS. Loading from memory.
            set and tag of 0x4 is 0 0
            address 0x4 CACHE HIT. Good Job.
            set and tag of 0x8 is 1 0
            address 0x8 CACHE MISS. Loading from memory.
            set and tag of 0xc is 1 0
            address 0xc CACHE HIT. Good Job.
            set and tag of 0x10 is 0 1
            address 0x10 CACHE MISS. Loading from memory.
            set and tag of 0xc is 1 0
            address 0xc CACHE HIT. Good Job.
            set and tag of 0x10 is 0 1
            address 0x10 CACHE HIT. Good Job.
            set and tag of 0x3c is 1 3
            address 0x3c CACHE MISS. Loading from memory.
            total cache misses 4
            miss_rate 0.5
            hit_rate 0.5
            Finished processing your program trace, progress = 100.0 %
             """),
            ("pingpong.trace 16 1 4".split(" "),
             """pingpong.trace
            Processing your program trace, progress so far = 0 %
            set and tag of 0x0 is 0 0
            address 0x0 CACHE MISS. Loading from memory.
            set and tag of 0x10 is 0 1
            address 0x10 CACHE MISS. Loading from memory.
            set and tag of 0x0 is 0 0
            address 0x0 CACHE MISS. Loading from memory.
            set and tag of 0x10 is 0 1
            address 0x10 CACHE MISS. Loading from memory.
            set and tag of 0x0 is 0 0
            address 0x0 CACHE MISS. Loading from memory.
            set and tag of 0x10 is 0 1
            address 0x10 CACHE MISS. Loading from memory.
            set and tag of 0x0 is 0 0
            address 0x0 CACHE MISS. Loading from memory.
            set and tag of 0x10 is 0 1
            address 0x10 CACHE MISS. Loading from memory.
            total cache misses 8
            miss_rate 1.0
            hit_rate 0.0
            Finished processing your program trace, progress = 100.0 %
             """),
            ("dm_a.trace 64 1 4".split(" "),
             """dm_a.trace
                Processing your program trace, progress so far = 0 %
                set and tag of 0x0 is 0 0
                address 0x0 CACHE MISS. Loading from memory.
                set and tag of 0x4 is 1 0
                address 0x4 CACHE MISS. Loading from memory.
                set and tag of 0x8 is 2 0
                address 0x8 CACHE MISS. Loading from memory.
                set and tag of 0xc is 3 0
                address 0xc CACHE MISS. Loading from memory.
                set and tag of 0x10 is 4 0
                address 0x10 CACHE MISS. Loading from memory.
                set and tag of 0x14 is 5 0
                address 0x14 CACHE MISS. Loading from memory.
                set and tag of 0x18 is 6 0
                address 0x18 CACHE MISS. Loading from memory.
                set and tag of 0x1c is 7 0
                address 0x1c CACHE MISS. Loading from memory.
                set and tag of 0x20 is 8 0
                address 0x20 CACHE MISS. Loading from memory.
                set and tag of 0x24 is 9 0
                address 0x24 CACHE MISS. Loading from memory.
                set and tag of 0x28 is 10 0
                address 0x28 CACHE MISS. Loading from memory.
                set and tag of 0x2c is 11 0
                address 0x2c CACHE MISS. Loading from memory.
                set and tag of 0x30 is 12 0
                address 0x30 CACHE MISS. Loading from memory.
                set and tag of 0x34 is 13 0
                address 0x34 CACHE MISS. Loading from memory.
                set and tag of 0x38 is 14 0
                address 0x38 CACHE MISS. Loading from memory.
                set and tag of 0x3c is 15 0
                address 0x3c CACHE MISS. Loading from memory.
                set and tag of 0x4 is 1 0
                address 0x4 CACHE HIT. Good Job.
                set and tag of 0x48 is 2 1
                address 0x48 CACHE MISS. Loading from memory.
                set and tag of 0x8 is 2 0
                address 0x8 CACHE MISS. Loading from memory.
                set and tag of 0xc is 3 0
                address 0xc CACHE HIT. Good Job.
                set and tag of 0x10 is 4 0
                address 0x10 CACHE HIT. Good Job.
                set and tag of 0x50 is 4 1
                address 0x50 CACHE MISS. Loading from memory.
                set and tag of 0x14 is 5 0
                address 0x14 CACHE HIT. Good Job.
                set and tag of 0x54 is 5 1
                address 0x54 CACHE MISS. Loading from memory.
                set and tag of 0x84 is 1 2
                address 0x84 CACHE MISS. Loading from memory.
                set and tag of 0x88 is 2 2
                address 0x88 CACHE MISS. Loading from memory.
                set and tag of 0x4 is 1 0
                address 0x4 CACHE MISS. Loading from memory.
                set and tag of 0x10 is 4 0
                address 0x10 CACHE MISS. Loading from memory.
                total cache misses 24
                miss_rate 0.8571428571428571
                hit_rate 0.1428571428571429
                Finished processing your program trace, progress = 100.0 %
                """
             ),
            ("dm_b.trace 64 1 8".split(" "),
             """dm_b.trace
                Processing your program trace, progress so far = 0 %
                set and tag of 0x4 is 0 0
                address 0x4 CACHE MISS. Loading from memory.
                set and tag of 0x48 is 1 1
                address 0x48 CACHE MISS. Loading from memory.
                set and tag of 0x8 is 1 0
                address 0x8 CACHE MISS. Loading from memory.
                set and tag of 0xc is 1 0
                address 0xc CACHE HIT. Good Job.
                set and tag of 0x10 is 2 0
                address 0x10 CACHE MISS. Loading from memory.
                set and tag of 0x50 is 2 1
                address 0x50 CACHE MISS. Loading from memory.
                set and tag of 0x14 is 2 0
                address 0x14 CACHE MISS. Loading from memory.
                set and tag of 0x54 is 2 1
                address 0x54 CACHE MISS. Loading from memory.
                set and tag of 0x84 is 0 2
                address 0x84 CACHE MISS. Loading from memory.
                set and tag of 0x88 is 1 2
                address 0x88 CACHE MISS. Loading from memory.
                set and tag of 0x4 is 0 0
                address 0x4 CACHE MISS. Loading from memory.
                set and tag of 0x10 is 2 0
                address 0x10 CACHE MISS. Loading from memory.
                total cache misses 11
                miss_rate 0.9166666666666666
                hit_rate 0.08333333333333337
                Finished processing your program trace, progress = 100.0 %
            """)
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=" ".join(input_value)):
                # Run the sim_dm.py script using subprocess and capture the output
                result = subprocess.run(
                    [pyton_bin_path, "../code/sim_dm.py", ] + input_value,
                    capture_output=True,
                    text=True,
                    cwd="../traces"
                )
                self.assertEqual(result.stderr, "")
                self.assertEqual(result.stdout, remove_leading_whitespace(expected_output))


if __name__ == "__main__":
    unittest.main()
