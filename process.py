import sqlite3

# Function to decode reported age into years
def decode_age(reported_age):
    if reported_age.startswith('1'):
        return int(reported_age[1:])
    elif reported_age.startswith('2'):
        return int(reported_age[1:]) / 12.0
    elif reported_age.startswith('4'):
        return int(reported_age[1:]) / 365.0
    elif reported_age.startswith('5'):
        return int(reported_age[1:]) / (365.0 * 24.0)
    elif reported_age.startswith('6'):
        return int(reported_age[1:]) / (365.0 * 24.0 * 60.0)
    else:
        return None

# Connect to SQLite database
conn = sqlite3.connect('mortality_data.db')
c = conn.cursor()

# Create table with additional column for age in years
c.execute('''CREATE TABLE IF NOT EXISTS mortality_data (
                record_type TEXT,
                resident_status TEXT,
                education TEXT,
                education_reporting_flag TEXT,
                month_of_death TEXT,
                sex TEXT,
                reported_age TEXT,
                age_substitution_flag TEXT,
                age_recode_52 TEXT,
                age_recode_27 TEXT,
                age_recode_12 TEXT,
                infant_age_recode_22 TEXT,
                place_of_death_and_status TEXT,
                marital_status TEXT,
                day_of_week_of_death TEXT,
                current_data_year TEXT,
                injury_at_work TEXT,
                manner_of_death TEXT,
                method_of_disposition TEXT,
                autopsy TEXT,
                activity_code TEXT,
                place_of_injury TEXT,
                underlying_cause_of_death TEXT,
                icd_code_10 TEXT,
                cause_recode_358 TEXT,
                cause_recode_113 TEXT,
                infant_cause_recode_130 TEXT,
                cause_recode_39 TEXT,
                entity_axis_conditions TEXT,
                record_axis_conditions TEXT,
                race_imputation_flag TEXT,
                hispanic_origin TEXT,
                race_recode_40 TEXT,
                occupation_4_digit_code TEXT,
                occupation_recode TEXT,
                industry_4_digit_code TEXT,
                industry_recode TEXT,
                age_in_years REAL
            )''')

# Read data from the file and insert into the database
with open('data.txt', 'r') as file:
    for line in file:
        record_type = line[18:19]
        resident_status = line[19:20]
        education = line[62:63]
        education_reporting_flag = line[63:64]
        month_of_death = line[64:66]
        sex = line[68:69]
        reported_age = line[69:73]
        age_substitution_flag = line[73:74]
        age_recode_52 = line[74:76]
        age_recode_27 = line[76:78]
        age_recode_12 = line[78:79]
        infant_age_recode_22 = line[79:81]
        place_of_death_and_status = line[82:83]
        marital_status = line[83:84]
        day_of_week_of_death = line[84:85]
        current_data_year = line[101:105]
        injury_at_work = line[105:106]
        manner_of_death = line[106:107]
        method_of_disposition = line[107:108]
        autopsy = line[108:109]
        activity_code = line[143:144]
        place_of_injury = line[144:145]
        underlying_cause_of_death = line[145:149]
        icd_code_10 = line[145:155]
        cause_recode_358 = line[152:153]
        cause_recode_113 = line[153:157]
        infant_cause_recode_130 = line[156:157]
        cause_recode_39 = line[158:159]
        entity_axis_conditions = line[162:163]
        record_axis_conditions = line[342:343]
        race_imputation_flag = line[447:448]
        hispanic_origin = line[483:484]
        race_recode_40 = line[489:491]
        occupation_4_digit_code = line[805:809]
        occupation_recode = line[809:811]
        industry_4_digit_code = line[815:819]
        industry_recode = line[816:817]
        
        # Calculate age in years
        age_in_years = decode_age(reported_age)
        
        # Insert data into table
        c.execute('''INSERT INTO mortality_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (record_type, resident_status, education, education_reporting_flag, month_of_death, sex,
                   reported_age, age_substitution_flag, age_recode_52, age_recode_27, age_recode_12,
                   infant_age_recode_22, place_of_death_and_status, marital_status, day_of_week_of_death,
                   current_data_year, injury_at_work, manner_of_death, method_of_disposition, autopsy,
                   activity_code, place_of_injury, underlying_cause_of_death, icd_code_10, cause_recode_358,
                   cause_recode_113, infant_cause_recode_130, cause_recode_39, entity_axis_conditions,
                   record_axis_conditions, race_imputation_flag, hispanic_origin, race_recode_40,
                   occupation_4_digit_code, occupation_recode, industry_4_digit_code, industry_recode,
                   age_in_years))

# Commit changes and close connection
conn.commit()
conn.close()
