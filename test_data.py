import pandas as pd

# Define the data
data = {
    'MDVP:Fo(Hz)': [119.992, 162.568, 197.076],
    'MDVP:Fhi(Hz)': [157.302, 198.346, 206.896],
    'MDVP:Flo(Hz)': [74.997, 77.630, 192.055],
    'MDVP:Jitter(%)': [0.00784, 0.00502, 0.00289],
    'MDVP:Jitter(Abs)': [0.00007, 0.00003, 0.00001],
    'MDVP:RAP': [0.00370, 0.00280, 0.00166],
    'MDVP:PPQ': [0.00554, 0.00253, 0.00168],
    'Jitter:DDP': [0.01109, 0.00841, 0.00498],
    'MDVP:Shimmer': [0.04374, 0.01791, 0.01098],
    'MDVP:Shimmer(dB)': [0.426, 0.168, 0.097],
    'Shimmer:APQ3': [0.02182, 0.00793, 0.00563],
    'Shimmer:APQ5': [0.03130, 0.01057, 0.00680],
    'MDVP:APQ': [0.02971, 0.01799, 0.00802],
    'Shimmer:DDA': [0.06545, 0.02380, 0.01689],
    'NHR': [0.02211, 0.01170, 0.00339],
    'HNR': [21.033, 25.678, 26.775],
    'RPDE': [0.414783, 0.427785, 0.422229],
    'DFA': [0.815285, 0.723797, 0.741367],
    'spread1': [-4.813031, -6.635729, -7.348300],
    'spread2': [0.266482, 0.209866, 0.177551],
    'D2': [2.301442, 1.957961, 1.743867],
    'PPE': [0.284654, 0.135242, 0.085569]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('test_data.xlsx', index=False)
print("test_data.xlsx created successfully.")