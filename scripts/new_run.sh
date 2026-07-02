#!/usr/bin/env bash
# usage: scripts/new_run.sh <run_name>
set -euo pipefail
name="$1"; date="$(date +%Y-%m-%d)"; dir="runs/${date}_${name}"
mkdir -p "$dir"
sed "s/YYYY-MM-DD/${date}/; s/run_name: main/run_name: ${name}/" \
    runs/run_config_template.yaml > "$dir/run_config.yaml"
echo "created $dir/run_config.yaml — edit it, then run generate + evaluate"
