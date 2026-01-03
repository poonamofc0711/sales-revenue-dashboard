import pandas as pd
import numpy as np

np.random.seed(42)

departments = ['Assembly', 'Painting', 'Packaging']
ideal_cycle_times = {'Assembly': 8, 'Painting': 10, 'Packaging': 5}
dates = pd.date_range('2025-12-01', '2025-12-30')

data = []
for date in dates:
    for dept in departments:
        units = np.random.randint(100, 201)
        defects = np.random.randint(0, 11)
        ideal_ct = ideal_cycle_times[dept]
        cycle_time = ideal_ct + np.random.uniform(0, 5)
        downtime = np.random.uniform(0, 120)
        expected = 480 // ideal_ct
        data.append({
            'Date': date,
            'Department': dept,
            'Units_Produced': units,
            'Defects': defects,
            'Cycle_Time': round(cycle_time, 2),
            'Downtime': round(downtime, 2),
            'Expected_Output': expected,
            'Ideal_Cycle_Time': ideal_ct
        })

df = pd.DataFrame(data)
df.to_csv('data/sample_data.csv', index=False)

# Optional: Compute OEE for verification
planned_time = 480
df['Run_Time'] = planned_time - df['Downtime']
df['Availability'] = df['Run_Time'] / planned_time
df['Performance'] = (df['Units_Produced'] * df['Ideal_Cycle_Time']) / df['Run_Time']
df['Quality'] = (df['Units_Produced'] - df['Defects']) / df['Units_Produced']
df['OEE'] = df['Availability'] * df['Performance'] * df['Quality'] * 100
print(df[['Department', 'OEE']].groupby('Department').mean())
