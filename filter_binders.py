import pandas as pd

# 1. Load your team's results CSV
# Adjust the filename and column names to match your pipeline's output
input_file = "binder_results.csv"
df = pd.read_csv(input_file)

# 2. Set your biological quality thresholds
# Standard starting cutoffs for de novo protein binders:
MIN_IPTM = 0.70  # Interface confidence (higher is better, max 1.0)
MIN_PLDDT = 80.0  # Overall folding confidence (0-100 scale)
MAX_PAE = 10.0  # Interface alignment error in Angstroms (lower is better)

# 3. Filter candidates
# Note: Rename 'iptm', 'plddt', 'pae_interaction' if your CSV uses slightly different headers
filtered_df = df[
    (df["iptm"] >= MIN_IPTM)
    & (df["plddt"] >= MIN_PLDDT)
    & (df["pae_interaction"] <= MAX_PAE)
]

# 4. Sort by highest interface confidence (ipTM) first
top_candidates = filtered_df.sort_values(by="iptm", ascending=False)

# 5. Save the top 20 designs to a new file for ChimeraX visual inspection
top_20 = top_candidates.head(20)
top_20.to_csv("top_20_for_chimerax.csv", index=False)

print(
    f"Filtered {len(df)} total designs down to {len(filtered_df)} passing"
    " candidates."
)
print("Top 5 candidates:")
print(top_20[["design_id", "iptm", "plddt", "pae_interaction"]].head(5))