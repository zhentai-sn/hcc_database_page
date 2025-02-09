import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from pygwalker.api.streamlit import StreamlitRenderer
import pygwalker as pyg
from utils.grid_config import configure_grid

from utils import process_original_data

# 设置页头页面布局
st.set_page_config(page_title='HCC Database',  layout='wide',)
t1, t2,  = st.columns((0.8, 0.2, )) 

t1.title("原发性肝癌手术与综合治疗临床数据库")
t1.markdown(" **地址:** 广州市广州大道北1838号 **| website:** https://www.nfyy.com/ks/wk/gdwk/ksjj/a_101553.html ") # **| email:** 


# 读取并处理原始数据
data_base_path = 'data/data_base.xlsx'  
hosp_df = pd.read_excel(data_base_path)
data_base_dict = process_original_data.split_data(hosp_df)


# 筛选数据
multi_header_df = pd.read_excel('./data/data_base.xlsx',header=[0,1,2])
multi_header_df.columns = multi_header_df.columns.map(lambda x: '_'.join([ y for y in x if not y.startswith('Unnamed')]))

# 读取数据
follow_up_data = pd.read_excel('data/follow_up_data_base.xlsx')
# follow_up_datadict = process_original_data.split_data(follow_up_data)

# 数据选择控件
selected_db = st.radio(
    "选择数据库：",
    ["手术数据库", "随访数据库"],
    horizontal=True  # 水平排列选项
)
st.markdown("---")

# 根据选择加载数据
if selected_db == "手术数据库":
    display_df = multi_header_df
    
else:
    display_df = follow_up_data
    

# 配置 AgGrid
grid_options = configure_grid(display_df)


tabs = st.tabs(
    [
        "原始数据",
        "选中数据",
        "分析数据"
    ]
)

with tabs[0]:
    # 显示 AgGrid 表格
    grid_response = AgGrid(
        display_df,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=False,
        height=600,
        width='100%',
        theme='streamlit'  # 或者使用 'light', 'dark', 'blue', 'material'
    )

with tabs[1]:
    selected_data = grid_response.selected_data

    if selected_data is None:
        st.write("请先在原始数据中选中数据!")
    else:
        st.write(grid_response.selected_data)

with tabs[2]:
    selected_data = grid_response.selected_data

    if selected_data is None:
        st.write("请先在原始数据中选中数据!")
    else:
        # 将选中的数据转换为DataFrame并使用pygwalker分析
        selected_df = pd.DataFrame(selected_data)
        pyg_app = StreamlitRenderer(selected_df)
        pyg_app.explorer()


