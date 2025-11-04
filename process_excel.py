import pandas as pd

# Read Excel file
df = pd.read_excel("data.xlsx")

# Add a new column
df["Total"] = df["A"] + df["B"]

# Save to a new Excel file
output_path = "output.xlsx"
df.to_excel(output_path, index=False)

print("✅ Excel processed and saved as", output_path)
