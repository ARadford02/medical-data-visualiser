import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')#Read in the data

# 2
df['overweight'] = (df['weight'])/(df['height']*0.01)**2 #An overweight column with BMI values
#This passes a condition, the 2nd arg is if the condition is satisfied and 3rd arg is if the condition is not
#NORMALIZED DATA
df['overweight'] = np.where(df['overweight'] >25,1, 0)

# 3
#Normalise the gluc column
df['gluc'] = np.where(df['gluc']==1,0,1)
#Normalise the cholestrol column
df['cholesterol'] = np.where(df['cholesterol']==1,0,1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars='cardio',value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
    #has cardio column, varaible column and value column (corresponds to a given variable)
    

    # 7
    graph = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')
    graph.set(xlabel ="variable", ylabel = "total")


    # 8
    fig = graph.fig #The .fig makes it a matplotlib fig to make the tests work


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    #Cleaning the data by removing weight and height in the outer 2.5th percentiles (0.025 and 0.975)
    df_heat = df.loc[(df['height']>=df['height'].quantile(0.025)) & (df['height']<=df['height'].quantile(0.975)) &
                     (df['weight']>=df['weight'].quantile(0.025)) & (df['weight']<=df['weight'].quantile(0.975)) &
                     (df['ap_lo']<=df['ap_hi'])]

    # 12
    #Correlation Matrix
    corr = df_heat.corr()

    # 13
    #Upper triangle mask
    mask = np.triu(np.ones_like(corr))



    # 14
    #Set up plot env
    fig, ax =plt.subplots(figsize=(7,7))

    # 15
    sns.heatmap(corr,annot=True, mask=mask,ax=ax,fmt=".1f", linewidths=0.5)


    # 16
    fig.savefig('heatmap.png')
    return fig
