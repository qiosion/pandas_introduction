import pandas as pd

exam_data = {
    # 열(칼럼) : 행
    'AI_SW': [90, 80, 70],
    'DS': [98, 82, 71],
    'JAVA': [92, 100, 90],
    'ML': [76, 88, 85],
}

df = pd.DataFrame(exam_data, index=['강은선', '구보람', '김권아'])

# col 추가
df['Web'] = [85, 100, 88]
print(df)

# row 추가 : loc 사용
df.loc['김나은'] = [90, 85, 99, 87, 90]
print(df)

df.loc['김은희'] = df.loc['김나은'] # 김나은의 값을 복사해서 사용
print(df)

# 원소값 변경
df.iloc[2, 0] = 90
print(df)
df.iloc[2, [0, 1, 2]] = [91, 92, 100] # df.iloc[row, 3:] = [23, 44] 처럼도 변경 가능

# transpose ( row <-> col)
df2 = df.transpose()
print(df2)