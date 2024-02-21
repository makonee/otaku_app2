import streamlit as st
import pandas as pd
import os

# 初回のセッションで csv_created を初期化
if 'csv_created' not in st.session_state:
    if os.path.isfile("purchase_records.csv"):
        st.session_state.csv_created = True
    else:
        st.session_state.csv_created = False

# CSV ファイルからデータを読み込む
filename = "purchase_records.csv"
existing_data = pd.read_csv(filename) if st.session_state.csv_created else pd.DataFrame()

# ユーザーからの入力を受け付ける
st.header('活動の記録')
date = st.date_input('日付選択')
group = st.text_input('グループ選択（自由入力）')
kounyuu = st.selectbox('購入種選択', ['チケット', 'CD・Mカード', 'チェキ', '生写真', 'アクキー', 'グッズ'])
kounyuusuu = st.number_input('購入数', min_value=0, step=1)
purchase = st.number_input('購入単価（円）', min_value=0)
result = kounyuusuu * purchase
st.write(f"合計金額: {result}円")

# ユーザーが入力したデータを新しい行として追加
new_data = {'日付': date, 'グループ': group, '購入種': kounyuu, '購入数': kounyuusuu, '購入単価': purchase, '合計金額': result}
existing_data = existing_data.append(new_data, ignore_index=True)

# '記録を保存'ボタンが押された場合にデータを CSV ファイルに保存
if st.button('保存'):
    existing_data.to_csv(filename, index=False)
    st.success(f'{filename} にデータを保存しました。')
    st.session_state.csv_created = True


# CSVファイルからデータを読み込む
filename = "purchase_records.csv"
df = pd.read_csv(filename)

# データを表示
st.write(df)

# グループごとの購入数の合計を計算
st.subheader('グループごとの購入数')
group_total = df.groupby('グループ')['購入数'].sum()

# グラフにプロット
st.bar_chart(group_total)

# グループごとの購入金額の合計を計算
st.subheader('グループごとの購入金額')
group_total_price = df.groupby('グループ')['購入単価'].sum()

# グラフにプロット
st.bar_chart(group_total_price)

# 購入種別ごとの購入数の合計を計算
st.subheader('購入種ごとの購入数')
purchase_type_total = df.groupby('購入種')['購入数'].sum()

# グラフにプロット
st.bar_chart(purchase_type_total)

# 購入種別ごとの購入金額の合計を計算
st.subheader('購入種別ごとの購入金額')
purchase_type_total_price = df.groupby('購入種')['購入単価'].sum()

# グラフにプロット
st.bar_chart(purchase_type_total_price)