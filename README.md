# backup-job-duration-tracker

Track backup job durations against expected minutes: OVERRUN when a job ran long, with the overrun shown — longest job first, so a backup window that no longer fits is caught early.

## How to run

```sh
python3 main.py jobs.csv
```

## Example output

```
DB-nightly (2026-11-05): OVERRUN (90 min, expected 60 min, +30 min)
Files-weekly (2026-11-05): OK (45 min, expected 60 min, -15 min)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
