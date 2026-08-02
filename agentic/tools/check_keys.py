#!/usr/bin/env python3
"""Startup check: does every enabled model's API key resolve, and is Ollama reachable?

Prints `ok` / `missing` per model and reachable / unreachable for Ollama. Never prints
a key. Run this once after pasting keys into config/local_secrets.py, before the pipeline.

Usage: python tools/check_keys.py
"""
import sys
import urllib.request

import backends as B


def key_status(model_cfg) -> str:
    if model_cfg.get("backend") == "ollama":
        return "n/a (local)"
    env_name = model_cfg.get("api_key_env")
    if not env_name:
        return "no api_key_env in config"
    try:
        B.get_key(env_name)   # never returns/prints the value
        return "ok"
    except RuntimeError:
        return "missing"


def ollama_reachable() -> bool:
    try:
        with urllib.request.urlopen(f"{B.ollama_host()}/api/tags", timeout=5) as r:
            return r.status == 200
    except Exception:
        return False


def main():
    models = B.load_models()
    roles = []
    if "teacher" in models:
        roles.append(("teacher", models["teacher"]))
    if "verifier" in models:
        roles.append(("verifier", models["verifier"]))
    for s in models.get("students", []):
        if s.get("enabled", True):
            roles.append(("student", s))

    print("Key resolution for enabled models (keys are never printed):")
    any_ollama = False
    all_keys_ok = True
    for role, cfg in roles:
        st = key_status(cfg)
        if cfg.get("backend") == "ollama":
            any_ollama = True
        elif st != "ok":
            all_keys_ok = False
        print(f"  {role:9} {cfg.get('id','?'):26} backend={cfg.get('backend','?'):13} key={st}")

    if any_ollama:
        reachable = ollama_reachable()
        print(f"\nOllama at {B.ollama_host()}: "
              f"{'reachable' if reachable else 'UNREACHABLE (start `ollama serve`)'}")
    else:
        reachable = True

    ok = all_keys_ok and reachable
    print("\n" + ("All good." if ok
                  else "Some checks failed - fix the 'missing'/UNREACHABLE items above."))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
