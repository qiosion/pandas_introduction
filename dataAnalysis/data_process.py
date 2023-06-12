import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
# header = "None" 지정할 필요 있음
df = pd.read_csv('../Data/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ["mpg", "cylinders", "displacement", "horsepower",
              "weight", "acceleration", "model year", "origin", "name"]


# 데이터 표준화
# mpg -> km, per, liter
# 1마일 = 1.60934km
# 1갤론 = 3.78541리터


# 자료형 변환
print(df.info())

# dataset 내에 ? 문자가 포함되어 있을 경우, ? 를 nan 로 변환
df['horsepower'].replace('?', np.nan, inplace=True)

# nan인 행 모두 삭제
df.dropna(axis=0, inplace=True)

# 마력 컬럼에서 nan가 있으면 해당 행을 삭제
df.dropna(subset=['horsepower'], axis=0, inplace=True)

print(df.horsepower.unique())

# object 를 float 으로 변경
df['horsepower'] = df['horsepower'].astype('float')

# 변경된 마력 칼럼의 데이터 타입 확인
print(df['horsepower'].dtype)


# 범주형 데이터 처리
# numpy의 히스토그램으로 binning하고, pandas 의 cut 메서드로 범주형 데이터로 변환하여 처리
# 마력의 binning을 3개로 나누어 사용 : low, normal, high
count, bin_divider = np.histogram(df['horsepower'], bins=3)
print(count, bin_divider) # [257 103  32] [ 46.         107.33333333 168.66666667 230.        ]

# pd.cut 사용
df['bin_horsepower'] = pd.cut(x=df['horsepower'],
                              bins=bin_divider,
                              labels=['low', 'normal', 'high'],
                              include_lowest=True
                              )

print(df[['horsepower', 'bin_horsepower']].head(20))

# 더미 데이터
horsepower_dummies = pd.get_dummies(df['bin_horsepower'])
print(horsepower_dummies.head(20))


# 정규화
# 일반적으로는 해당 칼럼의 최대 값으로 나누어서 0~1 사이의 값으로 변경
df['horsepower'] = df['horsepower'] / (df['horsepower'].max())
print(df['horsepower'].head())

"""
정규화할 때, 0~1 사이 값은 그냥 최대 값으로 사용
           -1~1 사이의 값으로 정규화를 할 경우
                1. 절대값
                2. 절대값의 최대값
           으로 정규화
- 주의점 : outlier 를 삭제한 후에 정규화하는 것이 좋음
"""
tmp = [-7, -2, -3, 2, 4, 6]

abs_list = []
for val in tmp:
    abs_list.append(abs(val))

norm_data = []
max_data = max(abs_list)
for data in tmp:
    norm_data.append(data / max_data)

print(norm_data)
# [-1.0, -0.2857142857142857, -0.42857142857142855, 0.2857142857142857, 0.5714285714285714, 0.8571428571428571]

# 리스트의 중첩으로 간단하게..
comp_ex = [data / max([abs(val) for val in tmp]) for data in tmp] # 중첩
print(comp_ex)