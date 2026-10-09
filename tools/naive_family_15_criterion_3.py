#!/usr/bin/env python3
"""Regression baseline for family 15 / criterion 3 (REBUILT as an infeasibility-certificate task,
audit B5).

Under the old design criterion 3 used mutually disjoint alphabets and required a constant "NONE", so
this program passed every test. After the redesign the arm requires an instance-specific BLOCK
certificate, so a bare "NONE" is now WRONG on every case. Kept to document that the old gaming route
no longer passes -- it should yield WRONG_ANSWER, confirming release_check gate G7.
"""
import sys


def main():
    sys.stdin.read()
    print("NONE")        # deliberately the old constant; now fails validator.py by design


main()
