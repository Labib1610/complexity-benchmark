import os
import json

# Directories
ATTEMPTS_DIR = "/home/labib/Desktop/labib_codes/research_codes/np_completeness/complexity-benchmark/agentic/attempts"

# Target filters
TARGET_FAMILIES = [1, 2, 5, 9, 14, 16, 17, 18, 19, 20, 21, 22]
CRITERIA = ["criterion_1_npc", "criterion_2_p"]
TARGET_MODELS = [
    "deepseek-v4-flash",
    "gemini-3.7-flash-frontier",
    "glm-5",
    "gpt-5.6-sol",
    "gpt-oss-120b",
    "qwen3-coder"
]

def get_verdict_category(overall_verdict):
    """Categorizes the verdict based on your targeted metrics."""
    if not overall_verdict:
        return "OTHER"
    
    verdict = overall_verdict.upper()
    if verdict == "PASS":
        return "PASS"
    elif verdict == "WRONG_ANSWER":
        return "WRONG_ANSWER"
    elif verdict in ["RUNTIME_ERROR", "TLE", "TIME_LIMIT_EXCEEDED"]:
        return "RE_TLE"
    else:
        return "OTHER"

def main():
    # Initialize data structures to hold statistics
    base_stats = lambda: {"PASS": 0, "WRONG_ANSWER": 0, "RE_TLE": 0, "OTHER": 0, "TOTAL": 0}
    
    model_stats = {model: base_stats() for model in TARGET_MODELS}
    family_stats = {fid: base_stats() for fid in TARGET_FAMILIES}
    family_model_stats = {fid: {model: base_stats() for model in TARGET_MODELS} for fid in TARGET_FAMILIES}

    # Traverse directory structure
    for fid in TARGET_FAMILIES:
        family_name = f"family_{fid:02d}"
        family_path = os.path.join(ATTEMPTS_DIR, family_name)
        
        if not os.path.isdir(family_path):
            continue
            
        for criterion in CRITERIA:
            criterion_path = os.path.join(family_path, criterion)
            if not os.path.isdir(criterion_path):
                continue
                
            # Iterate over dynamic version folders (v000, v001, etc.)
            for version_folder in os.listdir(criterion_path):
                version_path = os.path.join(criterion_path, version_folder)
                if not os.path.isdir(version_path):
                    continue
                    
                for model in TARGET_MODELS:
                    verdict_path = os.path.join(version_path, model, "verdict.json")
                    
                    if not os.path.isfile(verdict_path):
                        continue
                        
                    # Parse and validate the verdict JSON
                    try:
                        with open(verdict_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            
                        # Standard pattern check: ignore if essential keys are missing
                        if "overall" not in data or "cases" not in data:
                            continue
                            
                        category = get_verdict_category(data.get("overall"))
                        
                        # Accumulate totals
                        model_stats[model][category] += 1
                        model_stats[model]["TOTAL"] += 1
                        
                        family_stats[fid][category] += 1
                        family_stats[fid]["TOTAL"] += 1
                        
                        family_model_stats[fid][model][category] += 1
                        family_model_stats[fid][model]["TOTAL"] += 1
                        
                    except (json.JSONDecodeError, OSError):
                        # Silently ignore files that are corrupted or unreadable
                        continue

    # ------------------
    # Display Format
    # ------------------
    def print_percentages(label, stats, title_width):
        total = stats["TOTAL"]
        if total == 0:
            print(f"{label:<{title_width}} | No valid standard verdict.json found.")
            return

        pass_pct = (stats["PASS"] / total) * 100
        wa_pct = (stats["WRONG_ANSWER"] / total) * 100
        retle_pct = (stats["RE_TLE"] / total) * 100
        
        print(f"{label:<{title_width}} | Total: {total:<4} | PASS: {pass_pct:5.1f}% | WA: {wa_pct:5.1f}% | RE+TLE: {retle_pct:5.1f}%")

    print("\n" + "=" * 85)
    print(f"{'1. ACCURACY PERCENTAGES BY MODEL (Across all families and versions)':^85}")
    print("=" * 85)
    for model in TARGET_MODELS:
        print_percentages(model, model_stats[model], 28)

    print("\n" + "=" * 85)
    print(f"{'2. ACCURACY PERCENTAGES BY FAMILY (Across all models and versions)':^85}")
    print("=" * 85)
    for fid in TARGET_FAMILIES:
        family_label = f"family_{fid:02d}"
        print_percentages(family_label, family_stats[fid], 28)

    print("\n" + "=" * 85)
    print(f"{'3. ACCURACY PERCENTAGES PER FAMILY PER MODEL':^85}")
    print("=" * 85)
    for fid in TARGET_FAMILIES:
        family_label = f"family_{fid:02d}"
        print(f"\n--- {family_label.upper()} ---")
        for model in TARGET_MODELS:
            # Indent slightly for readability
            print_percentages(f"  {model}", family_model_stats[fid][model], 28)
            
    print("\n" + "=" * 85 + "\n")

if __name__ == "__main__":
    main()