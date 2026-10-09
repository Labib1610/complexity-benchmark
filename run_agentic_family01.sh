#!/usr/bin/env bash
# Full agentic hardening pipeline for ONE family (default 01), on the REBUILT dataset.
# Checkpointed: if it stops, just re-run this script and it resumes where it left off.
# Usage:  bash run_agentic_family01.sh            # family 01
#         FAM=all bash run_agentic_family01.sh    # all families (only after 01 is reviewed)
set -e
cd "$(dirname "$0")"
FAM="${FAM:-01}"
LOG="agentic/logs/pipeline_family_${FAM}.log"
mkdir -p agentic/logs
export PYTHONUNBUFFERED=1

say(){ echo; echo "============================================================"; \
       echo "== $* @ $(date +%H:%M:%S)"; echo "============================================================"; }

say "STAGE 1/8  generate_versions (grid,sample,composition)  family=$FAM"
python agentic/tools/generate_versions.py --family "$FAM" --sources grid,sample,composition

say "STAGE 2/8  gate  family=$FAM"
python agentic/tools/gate.py --family "$FAM"

say "STAGE 3/8  generate_versions (generation)  family=$FAM"
python agentic/tools/generate_versions.py --family "$FAM" --sources generation

say "STAGE 4/8  gate  family=$FAM"
python agentic/tools/gate.py --family "$FAM"
# PYTHONPATH=tools python agentic/tools/gate.py --family "$FAM"

say "STAGE 5/8  gen_tests (adversarial corner cases)  family=$FAM"
python agentic/tools/gen_tests.py --family "$FAM" --n 12

say "STAGE 6/8  run_students (baseline attempts)  family=$FAM"
python agentic/tools/run_students.py --family "$FAM"

say "STAGE 7/8  harden_loop (lineage/depth, full depth)  family=$FAM"
python agentic/tools/harden_loop.py --family "$FAM"

say "STAGE 8/8  reports  family=$FAM"
python agentic/tools/report.py --family "$FAM"
python agentic/tools/report_lineage.py --family "$FAM" || true

say "PIPELINE COMPLETE  family=$FAM"
