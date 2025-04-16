import pandas as pd
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

def preprocess():
    global df,region_df
    
    # Filter the dataset for Summer Olympics only
    df = df[df['Season'] == 'Summer']
    
    # Merge the athlete events data with the region data
    df = df.merge(region_df, how='left', on='NOC')
    
    # Drop duplicates
    df = df.drop_duplicates()
    
    # One hot encoding medals 
    df = pd.concat([df,pd.get_dummies(df['Medal'])], axis=1)

    return df 