import pandas as pd
import json


df1 = pd.read_json('./JSON file/batting_info.json')
df1.to_csv('./CSV/csv_batting_info.csv', index=False)

df2 = pd.read_json('./JSON file/bowling_info.json')
df2.to_csv('./CSV/csv _bowling_info.csv', index=False)

df3 = pd.read_json('./JSON file/link_info.json')
df3.to_csv('./CSV/csv _link_info.csv', index=False)

df4 = pd.read_json('./JSON file/match_info.json')
df4.to_csv('./CSV/csv_match_info.csv', index=False)

df5 = pd.read_json('./JSON file/player_info.json')
df5.to_csv('./CSV/csv_player_info.csv', index=False)

df6 = pd.read_json('./JSON file/unique.json')
df6.to_csv('./CSV/csv_unique.csv', index=False)

