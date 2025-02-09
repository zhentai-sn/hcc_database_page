'''
Description: 
Autor: zhentai
Date: 2024-01-22 16:33:11
LastEditTime: 2024-01-22 17:41:49
'''
import streamlit as st
import cv2
import pandas as pd
import numpy as np

st.set_page_config(page_title='Southern Medical University - zhentai',  layout='wide',)

## st.sidebar 下的内容会被渲染到侧边栏
with st.sidebar:
    st.title('欢迎来到我的应用')
    st.markdown('---')
    st.markdown('这是它的特性：\n- feature 1\n- feature 2\n- feature 3')
    


t1, t2 = st.columns((0.10,1)) 

t1.image('images\logo.jpg', width = 100)
t2.title("Southern Medical University - zhentai")
t2.markdown(" **tel:** 01392 451192 **| website:** https://www.smu.edu.cn/ **| email:** zhentai-smu@outlook.com")


st.title('学习使用 streamlit')
st.button("Re-run")

# 展示一级标题
st.header('1. 创建虚拟环境')

code1 = '''conda create -n ycfl python==3.10'''
st.code(code1, language='bash')


# 展示一级标题
st.header('2. 安装 streamlit ')
code2 = '''conda create -n ycfl python==3.10'''
st.code(code2, language='bash')


# 展示二级标题
st.subheader('2.1 尝试运行官方的domo')

# 纯文本
st.text('导入 streamlit 后，就可以直接使用 st.markdown() 初始化')

# 展示代码，有高亮效果
code3 = '''streamlit hello'''
st.code(code3, language='python')

st.subheader('2.2 展示一张图片')

st.image(r'images/1686562124702.jpg', width = 600)

st.subheader('2.3 展示表格')

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns = ["a", "b", "c"])

st.dataframe(chart_data.style.highlight_max(axis=0))


st.bar_chart(chart_data)

