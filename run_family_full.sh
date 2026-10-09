#!/usr/bin/env bash
# FULL per-family pipeline. Usage:  FAM=NN bash run_family_full.sh
# Runs: hardening (8 stages) -> worst-case probe -> frontier eval -> final report.
set -e
FAM="${FAM:?set FAM=NN}"
cd "$(dirname "$0")"
echo "########## FAMILY $FAM — FULL RUN ##########"
echo ">>> STAGE A: hardening pipeline"
FAM=$FAM bash run_agentic_family01.sh
echo ">>> STAGE B: worst-case probe"
FAM=$FAM python worstcase_probe.py
echo ">>> STAGE C: frontier eval (NPC+P on hardened variants)"
FAM=$FAM python run_frontier_variants.py
echo ">>> STAGE D: final report"
FAM=$FAM python family_report.py
echo "########## FAMILY $FAM — DONE ##########"
