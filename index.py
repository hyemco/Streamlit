import streamlit as st
import FinanceDataReader as fdr
import pandas as pd
import datetime

st.title('특화 부트캠프 Day 2')
st.header('주가 데이터 시각화 (w. Streamlit) ')
st.text('* 네이버(035420) 주가 시각화하기')
st.header('')

st.divider()
st.subheader('설정')
st.title('')

# text input 활용
str_code = st.text_input('종목 코드 : ', '035420')
st.subheader('')

# data input 활용
duration = st.date_input('조회일 : ' , [datetime.date(2022, 1, 1), datetime.date(2023, 7, 31)])

st.divider()
st.subheader('Data Chart')
st.title('')

start_date = duration[0].strftime("%Y-%m-%d")
end_date = duration[1].strftime("%Y-%m-%d")

df_krx = fdr.StockListing('KRX')
df = fdr.DataReader(str_code, start_date, end_date)

#이평선 데이터 추가
ma5 = pd.DataFrame(  df['Close'].rolling(window=5).mean())
ma20 = pd.DataFrame( df['Close'].rolling(window=20).mean())
ma60 = pd.DataFrame( df['Close'].rolling(window=60).mean())
ma120 = pd.DataFrame(df['Close'].rolling(window=120).mean())
ma240 = pd.DataFrame(df['Close'].rolling(window=240).mean())

df.insert(len(df.columns), '5일', ma5)
df.insert(len(df.columns), '20일', ma20)
df.insert(len(df.columns), '60일', ma60)
df.insert(len(df.columns), '120일', ma120)
df.insert(len(df.columns), '240일', ma240)

# dataframe 활용
st.dataframe(df)

st.divider()
st.subheader('Data 시각화')
st.title('')

# linechart 활용
st.line_chart(df[['5일', '20일', '60일', '120일', '240일']])
st.header('')

# barchart 활용
st.bar_chart(df['Volume'])
