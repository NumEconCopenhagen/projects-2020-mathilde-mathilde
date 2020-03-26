import pandas as pd

def long(df, var):
    """ Convert dataframe from wide to long format

    Args:
        df (pd.DataFrame): pandas dataframe with the column "Country/Region" as a string
        var (str): string that defines variable (confirmed, deaths, recovered)
        
    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    df_long = pd.DataFrame(df.unstack())
    df_long.reset_index(inplace=True)
    df_long.rename(columns = {'level_0':'date'}, inplace=True)
    df_long.rename(columns = {'Unnamed':var, 0:var}, inplace=True)
    df_long = pd.melt(df_long,id_vars = ('Country/Region', 'date'), value_vars = var)
    df_long.rename(columns = {'value':var}, inplace=True)

    
    return df_long