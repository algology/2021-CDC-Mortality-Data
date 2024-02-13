import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
conn = sqlite3.connect('mortality_data.db')

# Query to extract occupation codes and ages at death
query = "SELECT method_of_disposition, age_in_years FROM mortality_data;"
df = pd.read_sql_query(query, conn)
conn.close()

# Mapping occupation codes to names
occupation_mapping = {
    '01': 'Management Occupations',
    '02': 'Business & Financial Operations Occupations',
    '03': 'Computer & Mathematical Occupations',
    '04': 'Architecture & Engineering Occupations',
    '05': 'Life, Physical, & Social Science Occupations',
    '06': 'Community & Social Services Occupations',
    '07': 'Legal Occupations',
    '08': 'Education, Training, & Library Occupations',
    '09': 'Arts, Design, Entertainment, Sports, & Media Occupations',
    '10': 'Healthcare Practitioners & Technical Occupations',
    '11': 'Healthcare Support Occupations',
    '12': 'Protective Service Occupations',
    '13': 'Food Preparation & Serving Related Occupations',
    '14': 'Building & Grounds Cleaning & Maintenance Occupations',
    '15': 'Personal Care & Service Occupations',
    '16': 'Sales & Related Occupations',
    '17': 'Office & Administrative Support Occupations',
    '18': 'Farming, Fishing, & Forestry Occupations',
    '19': 'Construction & Extraction Occupations',
    '20': 'Installation, Maintenance, & Repair Occupations',
    '21': 'Production Occupations',
    '22': 'Transportation & Material Moving Occupations',
    '24': 'Military',
    '25': 'Other—Misc (Exc Housewife)',
    '26': 'Other—Housewife'
}

# Mapping education codes to names
education_mapping = {
    '1': '8th grade or less',
    '2': '9 - 12th grade, no diploma',
    '3': 'High school graduate or GED completed',
    '4': 'Some college credit, but no degree',
    '5': 'Associate degree',
    '6': 'Bachelor’s degree',
    '7': 'Master’s degree',
    '8': 'Doctorate or professional degree',
    '9': 'Unknown'
}

# Mapping resident status codes to names
resident_status_mapping = {
    '1': 'Residents',
    '2': 'Intrastate Nonresidents',
    '3': 'Interstate Nonresidents',
    '4': 'Foreign Residents'
}

# Mapping month of death codes to names
month_mapping = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

# Mapping gender codes to descriptive names
gender_mapping = {
    'M': 'Male',
    'F': 'Female'
}

# Mapping marital status codes to descriptive names
marital_status_mapping = {
    'S': 'Never married, single',
    'M': 'Married',
    'W': 'Widowed',
    'D': 'Divorced',
    'U': 'Marital Status unknown'
}
# Mapping manner of death codes to descriptive names
manner_of_death_mapping = {
    '1': 'Accident',
    '2': 'Suicide',
    '3': 'Homicide',
    '4': 'Pending investigation',
    '5': 'Could not determine',
    '6': 'Self-Inflicted',
    '7': 'Natural',
    ' ': 'Not specified'  # Assuming blank is represented by a space
}

# Mapping method of disposition codes to descriptive names
method_of_disposition_mapping = {
    'B': 'Burial',
    'C': 'Cremation',
    'D': 'Donation',
    'E': 'Entombment',
    'O': 'Other',
    'R': 'Removal from jurisdiction',
    'U': 'Unknown'
}

df['method_of_disposition'] = df['method_of_disposition'].map(method_of_disposition_mapping)

# Handle any missing or undefined method of disposition
df['method_of_disposition'].fillna('Unknown', inplace=True)

# Calculate average age for each method of disposition
average_ages = df.groupby('method_of_disposition')['age_in_years'].mean()

# Sort the average ages in descending order
average_ages = average_ages.sort_values(ascending=False)

# Seaborn styling
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

# Create the plot with Seaborn
sns.barplot(x=average_ages.values, y=average_ages.index, palette="mako")

# Customizing the plot
plt.title('Average Age at Death by Method of Disposition (Descending Order)', fontsize=16)
plt.xlabel('Average Age at Death', fontsize=14)
plt.ylabel('Method of Disposition', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()