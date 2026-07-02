#!/usr/bin/env bash
# tiny end-to-end check on family 01 only, one model, 1 sample
set -euo pipefail
python -m harness.generate --config "$1" --only "${2:-phi4}" --sample 3
python -m harness.evaluate --config "$1"
