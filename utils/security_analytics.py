import pandas as pd

def load_security_data(filepath="data/endpoints_incidents.csv"):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        return pd.DataFrame()

def get_antivirus_summary(df):
    if df.empty:
        return pd.Series(dtype=int)
    return df['antivirus_status'].value_counts()

def get_incident_summary(df):
    if df.empty:
        return pd.Series(dtype=int)
    return df[df['incident_type'] != 'None']['incident_type'].value_counts()
