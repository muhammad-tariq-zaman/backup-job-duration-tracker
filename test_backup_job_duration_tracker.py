import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import track

def row(j, d, dur, exp):
    return {"job": j, "date": d, "duration_minutes": str(dur), "expected_minutes": str(exp)}

class TestJobDuration(unittest.TestCase):
    def test_overrun(self):
        self.assertEqual(track([row("DB", "2026-11-05", 90, 60)])[0][5], "OVERRUN")
    def test_ok(self):
        self.assertEqual(track([row("DB", "2026-11-05", 45, 60)])[0][5], "OK")
    def test_exactly_expected_ok(self):
        self.assertEqual(track([row("DB", "2026-11-05", 60, 60)])[0][5], "OK")
    def test_overrun_minutes(self):
        self.assertEqual(track([row("DB", "2026-11-05", 90, 60)])[0][4], 30)
    def test_longest_first(self):
        r = track([row("A", "2026-11-05", 30, 60), row("B", "2026-11-05", 120, 60)])
        self.assertEqual(r[0][0], "B")
