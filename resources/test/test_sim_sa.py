import unittest
import subprocess

pyton_bin_path = "../../venv/Scripts/python.exe"


def remove_leading_whitespace(text):
    return "\n".join(line.lstrip() for line in text.splitlines())


class TestSimSA(unittest.TestCase):
    """
    测试用例不用给老师
    """

    def setUp(self):
        self.maxDiff = None  # 允许显示完整的 diff

    def test_sim_dm_output(self):
        test_cases = [
            ("pingpong.trace 16 2 4".split(" "),
             """pingpong.trace
                Processing your program trace, progress so far = 0 %
                set and tag of 0x0 is 0 0
                address 0x0 CACHE MISS. Loading from memory.
                set and tag of 0x10 is 0 2
                address 0x10 CACHE MISS. Loading from memory.
                set and tag of 0x0 is 0 0
                address 0x0 CACHE HIT. Good Job.
                set and tag of 0x10 is 0 2
                address 0x10 CACHE HIT. Good Job.
                set and tag of 0x0 is 0 0
                address 0x0 CACHE HIT. Good Job.
                set and tag of 0x10 is 0 2
                address 0x10 CACHE HIT. Good Job.
                set and tag of 0x0 is 0 0
                address 0x0 CACHE HIT. Good Job.
                set and tag of 0x10 is 0 2
                address 0x10 CACHE HIT. Good Job.
                total cache misses 2
                miss_rate 0.25
                hit_rate 0.75
                Finished processing your program trace, progress = 100.0 %
             """
             ),
            ("test_q.trace 64 2 4".split(" "),
             """test_q.trace
                Processing your program trace, progress so far = 0 %
                set and tag of 0x0 is 0 0
                address 0x0 CACHE MISS. Loading from memory.
                set and tag of 0x4 is 1 0
                address 0x4 CACHE MISS. Loading from memory.
                set and tag of 0x24 is 1 1
                address 0x24 CACHE MISS. Loading from memory.
                set and tag of 0x10 is 4 0
                address 0x10 CACHE MISS. Loading from memory.
                set and tag of 0x4 is 1 0
                address 0x4 CACHE HIT. Good Job.
                set and tag of 0x44 is 1 2
                address 0x44 CACHE MISS. Loading from memory.
                set and tag of 0x24 is 1 1
                address 0x24 CACHE MISS. Loading from memory.
                set and tag of 0x1c is 7 0
                address 0x1c CACHE MISS. Loading from memory.
                set and tag of 0x0 is 0 0
                address 0x0 CACHE HIT. Good Job.
                set and tag of 0x24 is 1 1
                address 0x24 CACHE HIT. Good Job.
                set and tag of 0x30 is 4 1
                address 0x30 CACHE MISS. Loading from memory.
                set and tag of 0x10 is 4 0
                address 0x10 CACHE HIT. Good Job.
                total cache misses 8
                miss_rate 0.6666666666666666
                hit_rate 0.33333333333333337
                Finished processing your program trace, progress = 100.0 %
             """),
            ("sa.trace 64 2 8".split(" "),
             """sa.trace
                Processing your program trace, progress so far = 0 %
                set and tag of 0x4 is 0 0
                address 0x4 CACHE MISS. Loading from memory.
                set and tag of 0x48 is 1 2
                address 0x48 CACHE MISS. Loading from memory.
                set and tag of 0x8 is 1 0
                address 0x8 CACHE MISS. Loading from memory.
                set and tag of 0xc is 1 0
                address 0xc CACHE HIT. Good Job.
                set and tag of 0x10 is 2 0
                address 0x10 CACHE MISS. Loading from memory.
                set and tag of 0x50 is 2 2
                address 0x50 CACHE MISS. Loading from memory.
                set and tag of 0x14 is 2 0
                address 0x14 CACHE HIT. Good Job.
                set and tag of 0x54 is 2 2
                address 0x54 CACHE HIT. Good Job.
                set and tag of 0x84 is 0 4
                address 0x84 CACHE MISS. Loading from memory.
                set and tag of 0x88 is 1 4
                address 0x88 CACHE MISS. Loading from memory.
                set and tag of 0x4 is 0 0
                address 0x4 CACHE HIT. Good Job.
                set and tag of 0x10 is 2 0
                address 0x10 CACHE HIT. Good Job.
                total cache misses 7
                miss_rate 0.5833333333333334
                hit_rate 0.41666666666666663
                Finished processing your program trace, progress = 100.0 %
             """)
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=" ".join(input_value)):
                # Run the sim_dm.py script using subprocess and capture the output
                cmd = [pyton_bin_path, "../code/sim_sa.py", ] + input_value
                print("run cmd " + " ".join(cmd))
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    cwd="../traces"
                )
                self.assertEqual(result.stderr, "")
                self.assertEqual(result.stdout, remove_leading_whitespace(expected_output))


if __name__ == "__main__":
    unittest.main()
