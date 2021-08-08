import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df=df.set_index('date')
df.index=pd.to_datetime(df.index)
df=df[(df['value']>=df['value'].quantile(0.025))
      &(df['value']<=df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    plt.plot(df.index, df.value, 'r')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    fig.set_size_inches(15, 5, forward=True)



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    dfcp=df.copy()
    dfcp['year'] = dfcp.index.year
    dfcp['month'] = dfcp.index.month
    caterog = dfcp.groupby([df.index.year, df.index.month], )['value'].agg(
        np.mean).rename_axis(['year', 'month'])
    caterog = caterog.reset_index()

    df_pivot = pd.pivot_table(caterog, values='value', index='year', columns='month')
    # Draw bar plot
    ax = df_pivot.plot(kind='bar')
    fig = ax.get_figure()
    fig.set_size_inches(6, 6)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axis = plt.subplots(1, 2)
    fig.set_size_inches(18, 6)
    sns.boxplot(x='year', y='value', data=df_box, ax=axis[0]).set(xlabel='Year', ylabel='Page Views')
    sns.boxplot(x='month', y='value', data=df_box, order=(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']),ax=axis[1]).set(xlabel='Month', ylabel='Page Views')
    axis[0].set_title('Year-wise Box Plot (Trend)')
    axis[1].set_title('Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
