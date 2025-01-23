import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the combined data (assuming the data is in a usable format from previous steps)
file_paths = {
    "Category A": r"C:\Users\liamd\OneDrive - Nottingham Trent University\KTP\Category A_parameters.txt",
    "Category B": r"C:\Users\liamd\OneDrive - Nottingham Trent University\KTP\Category B_parameters.txt",
    "Category C": r"C:\Users\liamd\OneDrive - Nottingham Trent University\KTP\Category C_parameters.txt",
    "Category D": r"C:\Users\liamd\OneDrive - Nottingham Trent University\KTP\Category D_parameters.txt",
}

# Function to load and clean data
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                param, val = line.strip().split(':', 1)
                try:
                    val = float(val.strip())
                except ValueError:
                    val = None
                data.append({'Parameter': param.strip(), 'Value': val})
    return pd.DataFrame(data)

# Load data from all categories
dataframes = {category: load_data(path) for category, path in file_paths.items()}

# Combine all data into a single DataFrame
for category, df in dataframes.items():
    df['Category'] = category
combined_data = pd.concat(dataframes.values(), ignore_index=True)

# Pivot using pivot_table to handle duplicates
scatter_data = combined_data.pivot_table(index='Category', columns='Parameter', values='Value', aggfunc='mean').reset_index()

# Scatterplot for two parameters (e.g., "area" vs. "tortuosity_index")
if 'area' in scatter_data.columns and 'tortuosity_index' in scatter_data.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=scatter_data, x="area", y="tortuosity_index", hue="Category")
    plt.title('Scatterplot: Tortuosity Index vs. Area')
    plt.xlabel('Area')
    plt.ylabel('Tortuosity Index')
    plt.legend(title="Category")
    plt.show()
else:
    print("Required columns 'area' or 'tortuosity_index' are missing in the pivoted data.")
