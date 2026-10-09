#!/usr/bin/env python3
"""Regression baseline for family 16 / criterion 3 (REBUILT as an infeasibility-certificate task,
audit B5).

Under the old design criterion 3 guaranteed T < some job's machine-1 time and required a constant
"NO", so this program passed every test. After the redesign the arm requires a machine-checkable
certificate (`JOB i` or `LOAD c`), so a bare "NO" is now WRONG on every case. Kept to document that
the old gaming route no longer passes -- it should yield WRONG_ANSWER, confirming release_check G7.
"""
import sys


def main():
    sys.stdin.read()
    print("NO")          # deliberately the old constant; now fails validator.py by design


main()
