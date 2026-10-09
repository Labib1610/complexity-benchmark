# Per-Family Run Guide — change only `FAM`

Everything is parameterized. To run a family end-to-end, set `FAM` to its number (obscure families:
17 exact_cover · 18 linear_arrangement · 19 multicommodity_flow · 20 edge_colouring · 21 multiway_cut ·
22 precedence_scheduling) and either run the **one-command driver** or the **step-by-step** stages.

All reference.py/validator.py wrappers use a robust path (they find `tools/` from any cwd), and all
12 seed problems (6 families × NPC+P) are verified error-free with 30-case tiers
(01–05 anchor · 06–15 scaled · 16–30 worst). Corner cases are generated automatically in Stage 5.

## Option 1 — one command (recommended)
```bash
cd /home/labib/Desktop/labib_codes/research_codes/np_completeness/complexity-benchmark
rm -rf agentic/versions/family_17            # clean slate on a first run (match the number!)
FAM=17 bash run_family_full.sh
```
This runs, in order: hardening (8 stages) → worst-case probe → frontier eval → final report, and prints
the standard table at the end. To do another family, change both the `rm` line and `FAM`.

## Option 2 — step by step (same thing, manual control)
Set the number once, then run each line (re-export FAM in each new terminal):
```bash
cd /home/labib/Desktop/labib_codes/research_codes/np_completeness/complexity-benchmark
export FAM=17
rm -rf agentic/versions/family_$FAM                                         # first run only
# --- hardening (8 stages) ---
python agentic/tools/generate_versions.py --family $FAM --sources grid,sample,composition   # 1
python agentic/tools/gate.py             --family $FAM                                       # 2
python agentic/tools/generate_versions.py --family $FAM --sources generation                # 3
python agentic/tools/gate.py             --family $FAM                                       # 4
python agentic/tools/gen_tests.py        --family $FAM --n 12                                # 5 (corner cases)
python agentic/tools/run_students.py     --family $FAM                                       # 6
python agentic/tools/harden_loop.py      --family $FAM                                       # 7  (resume: add --resume)
python agentic/tools/report.py           --family $FAM                                       # 8
# --- worst-case + frontier + final table ---
python worstcase_probe.py                                                                    # 9  (uses $FAM)
python run_frontier_variants.py                                                              # 10 (uses $FAM)
python family_report.py                                                                      # 11 (uses $FAM)
```

## What each extra script does
- **worstcase_probe.py** — generates one solution per model from the NPC statement, grades on SEED
  (small) + WORST (hard/large) tiers, prints the table, and saves `agentic/reports/worstcase_family_$FAM.json`.
  If it prints "strong models still pass the WORST tier", the regime needs bigger sizes — raise them in
  `worstcase_probe.py` `_adapters()` (one-line edit; witness families 17 & 20 give real TLE drops, the
  optimization families 18/19/21/22 are scale tiers by nature).
- **run_frontier_variants.py** — runs gpt-5.6-sol + gemini on the hardened variants (NPC + P).
- **family_report.py** — prints per-model NPC test / P test / NPC worst / NPC overall + averages.

## Monitoring while a stage runs
```bash
grep -E "^\[gate\]|seeds=" agentic/logs/pipeline_family_$FAM.log agentic/logs/harden_loop.log | tail
ps aux | grep -E "generate_versions|gate.py|gen_tests|run_students|harden_loop|worstcase_probe|run_frontier" | grep -v grep
```
Stage 7 (harden) is the long one; it is checkpointed — re-run with `--resume` if interrupted.

## Notes
- Run long stages with `nohup ... &` from your own terminal so they survive.
- `report.py` (Stage 8) is the hardening-pool report; `family_report.py` (Stage 11) is the full
  test→worst→overall+frontier table.
- The already-run families (01 colouring, 05 3-D matching, 09 clique/IS, 14 steiner, 16 job-shop) keep
  their own worst-case tools; the parameterized scripts here cover the 6 obscure families 17–22.

## Worst-case adapter coverage
- **Full worst-case column (witness TLE tier):** 17,18,19,20,21,22 AND 02,03,04,08,10,11,13
  (SAT, Hamiltonian, subset-sum, vertex-cover, dominating-set, set-cover, partition — witness graders in
  `tools/originals_worst.py`, dispatched from `worstcase_probe.py _adapters()`).
- **Scale-only (probe skips gracefully, worst-case `-`):** 06 bin-packing, 07 SCS, 12 knapsack, 15 LCS —
  pure optimization (need the optimum to grade), so like job-shop/Steiner no cheap gradeable TLE tier.
  These still run hardening + frontier + report.
- **No adapter yet (probe skips gracefully; worst-case shows `-`):** 02,03,04,06,07,08,10,11,12,13,15.
  These still run hardening + frontier + report via `run_family_full.sh`. Base statements for all of
  these were hardened (disguised/long, I/O preserved) on 2026. Worst-case tiers are bespoke per family
  (their gen tools differ and validators recompute) — added incrementally; witness-clean ones (SAT,
  Hamiltonian, subset-sum, vertex-cover, partition, dominating-set) give real TLE drops, the rest scale.
