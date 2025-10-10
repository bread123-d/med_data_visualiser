import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2


df['overweight'] = (df['weight']/(df['height']/100)**2).apply(lambda x: 1 if x>25 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x>1 else 0)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x>1 else 0)

# 4
def draw_cat_plot():

    df_cat = df.melt(id_vars = 'cardio', 
                     value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                     value_name='value')


    
    df_cat = df.melt(id_vars='cardio', 
                 value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat.rename(columns={'size': 'total'}, inplace=True)
    

    
    catplot = catplot = sns.catplot(
    data=df_cat, 
    x='variable', 
    y='total', 
    hue='value', 
    col='cardio', 
    kind='bar'
)


   
    fig = catplot.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])&
                 (df['height'] >= df['height'].quantile(0.025))&
                 (df['height'] <= df['height'].quantile(0.975))\
                    &(df['weight'] >= df['weight'].quantile(0.025))&
                    (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr().round(1)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(data=corr, 
                annot=True, 
                fmt=".1f", 
                linewidth=.5, 
                mask=mask, 
                annot_kws={'fontsize':6}, 
                cbar_kws={"shrink": .7}, 
                square=False, 
                center=0, 
                vmax=0.30)


    # 16
    fig.savefig('heatmap.png')
    return fig
