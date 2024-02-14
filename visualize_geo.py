import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Connect to SQLite database
conn = sqlite3.connect('mortality_data.db')
c = conn.cursor()

# Execute SQL query to fetch the average age of death by state
c.execute('''
    SELECT state, AVG(age_in_years) AS avg_age
    FROM mortality_data
    GROUP BY state
''')

# Fetch all rows of the result
state_data = pd.DataFrame(c.fetchall(), columns=['state', 'avg_age'])

# Close database connection
conn.close()

# Load the map of the United States
usa = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')).query('continent == "North America" and name == "United States of America"')

# Merge the state data with the map
usa = usa.merge(state_data, left_on='iso_a2', right_on='state', how='left')

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

usa.boundary.plot(ax=ax)
usa.plot(column='avg_age', ax=ax, legend=True, cax=cax)

plt.title('Average Age of Death by State')
plt.show()
