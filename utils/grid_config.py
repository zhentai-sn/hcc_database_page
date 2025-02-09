from st_aggrid import GridOptionsBuilder

def configure_grid(dataframe):
    """
    配置 AgGrid 的选项
    
    Args:
        dataframe: 需要显示的 DataFrame
        
    Returns:
        grid_options: 配置好的 AgGrid 选项
    """
    gb = GridOptionsBuilder.from_dataframe(dataframe)
    
    # 配置默认列属性
    gb.configure_default_column(
        enablePivot=True, 
        enableValue=True, 
        enableRowGroup=True,
        sortable=True,
        resizable=True,
        filterable=True
    )
    
    # 配置多行选择
    gb.configure_selection(
        selection_mode='multiple',
        use_checkbox=True,
        header_checkbox=True,
    )
    
    # 配置侧边栏
    gb.configure_side_bar()
    
    return gb.build() 