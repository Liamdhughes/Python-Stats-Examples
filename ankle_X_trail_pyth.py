import pandas as pd
import spm1d
import numpy as np
import matplotlib.pyplot as plt

# Load the dependent variable data (Y) without assuming any header
Y = pd.read_csv('ANKLE_X_TRAIL.csv', header=None).to_numpy()

# Load the independent variables data (IV) without headers
IV = pd.read_csv('independent_variable.csv', header=None)
IV.columns = ['Knee', 'Ankle']

# Now extract the independent variable columns as numpy arrays
A = IV['Knee'].to_numpy()  # Factor A (Knee component)
B = IV['Ankle'].to_numpy()  # Factor B (Ankle component)

# Check the shapes of the arrays to make sure they match
print("Shape of Y:", Y.shape)
print("Shape of A:", A.shape)
print("Shape of B:", B.shape)

# Ensure that A, B, and Y have the same number of rows (should be 28)
if Y.shape[0] == A.shape[0] == B.shape[0]:
    alpha = 0.05
    # Perform the two-way ANOVA
    FF = spm1d.stats.anova2(Y, A, B)
    
    # Conduct inference
    FFi_list = FF.inference(alpha)
    
    # Print and plot the results for each effect
    effect_labels = ['Factor A (Knee)', 'Factor B (Ankle)', 'Interaction (Knee x Ankle)']
    
    for i, FFi in enumerate(FFi_list):
        # Plot results
        plt.figure()
        FFi.plot()
        FFi.plot_threshold_label()
        FFi.plot_p_values()
        plt.title(f'{effect_labels[i]}')
        plt.show()
        
        # Print statistics
        print(f'\nStatistics for {effect_labels[i]}:')
        print(f' - F-values: {FFi.z}')
        print(f' - Degrees of Freedom: {FFi.df}')
        print(f' - p-value: {FFi.p_set}')
        print(f' - Critical Threshold (z*): {FFi.zstar}')
        print(f' - Null Hypothesis Rejected: {"Yes" if FFi.h0reject else "No"}')
else:
    print("Mismatch in the number of observations. Please check the data.")
