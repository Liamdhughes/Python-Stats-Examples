import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import spm1d
import os

# Set global font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# Read the CSV data
data = pd.read_csv('ANKLE_X_LEAD.csv', header=None).to_numpy()

# Trim the data to include only the first 101 columns
data = data[:, :101]

# Extract the relevant portions of the data
conditionA = data[0:7, :]
conditionB = data[7:14, :]
conditionC = data[14:21, :]
conditionD = data[21:28, :]

# Calculate the average across participants for each condition
avgConditionA = np.mean(conditionA, axis=0)
avgConditionB = np.mean(conditionB, axis=0)
avgConditionC = np.mean(conditionC, axis=0)
avgConditionD = np.mean(conditionD, axis=0)

# Load the independent variables data (IV) without headers
IV = pd.read_csv('independent_variable.csv', header=None)
IV.columns = ['Knee', 'Ankle']

# Now extract the independent variable columns as numpy arrays
A = IV['Knee'].to_numpy()  # Factor A (Knee component)
B = IV['Ankle'].to_numpy()  # Factor B (Ankle component)

# Ensure that A, B, and Y have the same number of rows (should be 28)
if data.shape[0] == A.shape[0] == B.shape[0]:
    alpha = 0.05
    # Perform the two-way ANOVA
    FF = spm1d.stats.anova2(data, A, B)
    
    # Conduct inference
    FFi_list = FF.inference(alpha)
    
    # Create a 1x4 subplot
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))  # Adjusted for 1x4 layout
    
    # Plot the first figure (Mean lead ankle Flexion)
    axs[0].plot(np.arange(1, 102), avgConditionA, color=[0.2, 0.2, 0.2], linewidth=1.5, label='Mech + Hyd')
    axs[0].plot(np.arange(1, 102), avgConditionB, color=[0.4, 0.4, 0.4], linewidth=1.5, label='Mech + Rig')
    axs[0].plot(np.arange(1, 102), avgConditionC, '--', color=[0.6, 0.6, 0.6], linewidth=1.5, label='MPK + Hyd')
    axs[0].plot(np.arange(1, 102), avgConditionD, '--', color=[0.8, 0.8, 0.8], linewidth=1.5, label='MPK + Rig')
    axs[0].set_title('Mean lead Ankle Dorsilexion', fontsize=12)
    axs[0].set_xlabel('% of step cycle', fontsize=10)
    axs[0].set_ylabel('Plantar/Dorsiflexion Degrees', fontsize=8)
    axs[0].legend(loc='upper left', fontsize=8)  # Legend inside the plot
    
    # Plot the ANOVA results
    effect_labels = [
        'Knee Effect on lead Ankle Dorsilexion',
        'Ankle Effect on lead Ankle Dorsilexion',
        'Knee & Ankle Interaction Effect on lead Ankle Dorsilexion'
    ]
    
    for i, FFi in enumerate(FFi_list):
        ax = axs[i + 1]  # Adjust indexing for 1x4 layout
        ax.plot(FFi.z, label='Observed F-values')
        ax.axhline(y=FFi.zstar, color='r', linestyle='--', label=f'Significance Threshold (F* = {FFi.zstar:.2f}, α = {alpha})')
        ax.set_title(effect_labels[i], fontsize=12)
        ax.set_xlim([0, 100])  # Set x-axis limit to 100
        ax.set_xlabel('% Step Cycle', fontsize=8)
        ax.set_ylabel('F-value', fontsize=8)
        ax.legend(loc='center right', fontsize=8) 

        # Print statistics
        print(f'\nStatistics for {effect_labels[i]}:')
        print(f' - F-values: {FFi.z}')
        print(f' - Degrees of Freedom: {FFi.df}')
        print(f' - p-value: {FFi.p_set}')
        print(f' - Critical Threshold (z*): {FFi.zstar}')
        print(f' - Null Hypothesis Rejected: {"Yes" if FFi.h0reject else "No"}')
    
    # Adjust layout with increased space between plots
    plt.subplots_adjust(wspace=0.5)  # Increase wspace for more horizontal space between plots
    plt.tight_layout()

    # Save the figure to the specified path
    save_path = r'C:\Users\liamd\OneDrive - Nottingham Trent University\obstacle\SPM\Figures SPM\lead_ankle_x.tiff'
    plt.savefig(save_path, format='tiff', dpi=300, bbox_inches='tight')

    # Display the plot
    plt.show()
    
else:
    print("Mismatch in the number of observations. Please check the data.")
