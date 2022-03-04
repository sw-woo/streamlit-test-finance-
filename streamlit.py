import streamlit as st
import pandas as pd
import yfinance as yf
from sklearn.datasets import load_iris


#Title
st.title('간단한 주식 차트 종가(closing price)와 거래량(volume) 보기 테슬라')

st.header('종가')



Stock_Symbol = 'TSLA'
StockData = yf.Ticker(Stock_Symbol)
StockChart = StockData.history(period='1d',start='2019-1-1',end='2022-3-3')

st.line_chart(StockChart.Close)

st.header('거래량')


st.line_chart(StockChart.Volume)





# iris = load_iris()
# iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
# iris_df['target'] = iris['target']
# iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))
# ## Return table/dataframe
# # table
# st.table(iris_df.head())

# # dataframe
# st.dataframe(iris_df)
# st.write(iris_df)



