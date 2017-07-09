from __future__ import division
import pandas as pd
from pandas import Series, DataFrame
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.io.data import DataReader
from datetime import datetime


tech_list=['AAPL','GOOG','MSFT','AMZN']
end=datetime.now()
start=datetime(end.year-1,end.month,end.day)

for stock in tech_list:
    globals()[stock]=DataReader(stock,'Yahoo',start,end) #read from yahoo finance

#print AAPL.describe() #Apple stocks
AAPL['Adj Close'].plot(legend=True,figsize=(10,4))
plt.show()
AAPL['Volume'].plot(legend=True,figsize=(10,4))
plt.show()

ma_day=[10,20,50] #moving average days
for ma in ma_day:
    column_name="MA for %s days" %(str(ma))
    AAPL[column_name]=pd.rolling_mean(AAPL['Adj Close'],ma)

AAPL[['Adj Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,figsize=(10,4))
plt.show()

AAPL['Daily Return']=AAPL['Adj Close'].pct_change()
AAPL['Daily Return'].plot(legend=True,figsize=(10,4),linestyle='--',marker='o')
plt.show()

sns.distplot(AAPL['Daily Return'].dropna(),bins=100,color='purple')
plt.show()

closing_df=DataReader(tech_list,'yahoo',start,end)['Adj Close']
tech_rets=closing_df.pct_change()

#sns.jointplot('GOOG','MSFT',tech_rets,kind='scatter',color='seagreen')
#plt.show()

#sns.pairplot(tech_rets.dropna())
#plt.show()

#kernel density estimate plots in lower triangle plot, hist in diag, scatter at top plots
returns_fig=sns.PairGrid(closing_df.dropna())
returns_fig.map_upper(plt.scatter,color='purple')
returns_fig.map_lower(sns.kdeplot,cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)
plt.show()
#show how strong correlation are
#sns.corrplot(closing_df,annot=True)
#plt.show()

#--------------------risk analysis----------------------

#rets=tech_rets.dropna()
#area=np.pi*20
#plt.scatter(rets.mean(),rets.std(),s=area)
#plt.xlabel("Expected Return")
#plt.ylabel("Risk")
#for label,x,y in zip(rets.columns,rets.mean(),rets.std()):
#    plt.annotate(
#        label,
#        xy=(x,y),xytest=(50,50),
#        textcoords='offset points',ha='right',va='bottom',
#        arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=0.3')
#    )
#plt.show()
