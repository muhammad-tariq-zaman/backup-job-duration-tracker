"""Track backup job durations against expected minutes.

Usage: python3 main.py jobs.csv
CSV columns: job,date (ISO),duration_minutes,expected_minutes.
OVERRUN when a job took longer than expected, otherwise OK.
Longest job first, with the overrun in minutes shown.
"""
import argparse, csv, sys

def track(rows):
    out = []
    for row in rows:
        duration = int(row["duration_minutes"])
        expected = int(row["expected_minutes"])
        overrun = duration - expected
        verdict = "OVERRUN" if overrun > 0 else "OK"
        out.append((row["job"].strip(), row["date"].strip(), duration, expected, overrun, verdict))
    return sorted(out, key=lambda r: -r[2])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for job, date_, duration, expected, overrun, verdict in track(list(csv.DictReader(f))):
            print(f"{job} ({date_}): {verdict} ({duration} min, expected {expected} min, {overrun:+d} min)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
