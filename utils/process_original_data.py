'''
Description: 
Autor: zhentai
Date: 2024-01-30 12:11:36
LastEditTime: 2024-01-30 12:12:01
'''
import pandas as pd


def split_data(basic_data):

   first_row = basic_data.columns.tolist()
   first_header = [x for x in first_row if 'Unnamed' not in x]

   data_base_dict = {}
   for header in first_header[::-1]:
      df_left = basic_data.iloc[:, basic_data.columns.get_loc(header):]
      basic_data = basic_data.iloc[:, :basic_data.columns.get_loc(header)]
      df_left.columns = df_left.iloc[0]
      df_left = df_left[1:]
      data_base_dict[header] = df_left

   data_base_dict = dict(reversed(data_base_dict.items()))

   return data_base_dict