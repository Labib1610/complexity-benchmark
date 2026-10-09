#!/usr/bin/env python3
"""Regression baseline for family 09 / criterion 3 (REBUILT as an infeasibility-certificate task,
audit B5).

Under the old design criterion 3 asked for a clique of size r > n and required a constant "NO", so
this program passed every test. After the redesign the arm requires a machine-checkable certificate
(`SIZE` or `COMPLETE`), so a bare `NO` is now WRONG on every case. Kept to document that the old
gaming route no longer passes -- it should yield WRONG_ANSWER, confirming release_check gate G7.
"""
import sys


def main():
    sys.stdin.read()
    print("NO")          # deliberately the old constant; now fails validator.py by design


main()
