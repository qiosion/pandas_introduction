import pandas as pd
import seaborn as sns

print(">>> 누락 데이터 처리")

pd.set_option('display.max_columns', None)
df_pg = sns.load_dataset('penguins')
""" 데이터 정보 보기
print(df_pg.info())
print("====================")
print(df_pg.head())
"""

# 연습 차원에서 isnull().sum() 해보자
"""
print(len(df_pg) - df_pg.count()) # null 값의 개수를 칼럼별로 계산
- len(df_pg) : 하나의 데이터. 344. 정수
- df_pg.count() : 값이 있는 데이터의 개수
"""
print(df_pg.isnull().sum())

# 행 기준으로 하나라도 NaN 또는 null이 존재하는 행을 추출
print(df_pg.isnull().any(axis=1)) # isnull 은 칼럼 별 계산 모듈(0 : col, 1 : row)
print(df_pg[df_pg.isnull().any(axis=1)]) # 행을 기준으로 null값이 하나라도 있는 개체를 출력

"""
row 행 번호를 이용한 drop : drop(index=[..])
col 열을 이용한 drop : drop(columns=['sample'])
- 목적 : 3, 339 행을 삭제하고, sex 열을 삭제한다
"""
df_pg_nan = df_pg.drop(index=[3, 339], columns=["sex"]) # 새 변수 안두면 데이터가 아예 바뀌니까
# print(df_pg_nan.head()) # 데이터 확인 => 3번 행과 sex 칼럼이 사라졌다

# 행을 기준으로 null값이 하나라도 있는 데이터를 출력
print(df_pg_nan[df_pg_nan.isnull().any(axis=1)])

# len(df_pg_nan) 을 통해 인덱스 개수 출력 (전체 344 에서 drop을 통해 행 2개 뺐으니 342됨)
print('데이터 개수 출력 : ', len(df_pg_nan))

# drop
# 성별 drop 해줘 (축 : col)
df_pg.drop('sex', axis=1, inplace=True)

# 모든 값이 null일 경우(how='all') drop해줘
df_pg.dropna(subset=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
                how='all', inplace=True)

# 중복 데이터 처리
# 몸무게가 제일 많이 나가는 펭귄 데이터의 행 row를 복제
print(df_pg_nan['body_mass_g'].max())

print(df_pg_nan.tail(2)) # tail(2) : 데이터를 뒤에서부터 2개 보여줘

# 몸무게가 제일 많이 나가는 펭귄 데이터의 행 row를 추출 -> 237번째 행
print(df_pg_nan[df_pg_nan['body_mass_g'] == df_pg_nan['body_mass_g'].max()])

"""
duplicate : 복제
# 237번째 행의 데이터를 344번째에 복제해보자
df_pg_nan.loc[344] = ['Gentoo', 'Biscoe', 49.2, 15.2, 221.0, 6300.0]
또는 아래와 같이 작성 가능
"""
df_pg_nan.loc[344] = df_pg_nan.loc[237]
# print(df_pg_nan.tail(2)) # 데이터 확인

# 데이터 프레임 전체 행 데이터 중에서 중복값 찾기
print(df_pg_nan.duplicated()) # 344 -> Ture 나옴

print(df_pg_nan[df_pg_nan['body_mass_g'] == 6300.0]) # 237, 344 총 2개 나옴

# drop_duplicates() : 중복 행 제거
df_pg_nan.drop_duplicates(inplace=True)
print(df_pg_nan[df_pg_nan['body_mass_g'] == 6300.0]) # 237 하나만 나옴

print(">>> 이상치 제거")
"""
이상치 제거 : Z-score 활용한 데이터 전처리
Z-score : (x - u) / std
        x : 관측 데이터
        u : 평균
        std : 표준편차
- 표준편차가 시그마 2 이상인 데이터를 outlier (이상치)로 정의하자.
- def outlier : 시그마가 2 이상인 데이터의 행번호를 반환하는 함수 생성
"""
import numpy as np
print(np.mean(df_pg_nan['body_mass_g'])) # 평균
print(np.std(df_pg_nan['body_mass_g'])) # 표준편차

def outlier(input_df, col, sigma): # 이상치 계산
    # 이상치 score 값은 (x - u) / std
    return input_df[abs((input_df[col] - np.mean(input_df[col])) / np.std(input_df[col])) > sigma].index
    # abs : 절대값
    # z-score(이상치)가 sigma보다 큰 데이터의 인덱스 번호(.index)를 리턴

print()
print(outlier(df_pg_nan, 'body_mass_g', 2))
# 인덱스 번호 [233, 235, 237, 253, 297, 299, 331, 335, 337]
# drop 방법
df_pg_nan.drop(index=outlier(df_pg_nan, 'body_mass_g', 2), inplace=True)

def inlier(input_df, col, sigma):
    return input_df[abs((input_df[col] - np.mean(input_df[col])) / np.std(input_df[col])) <= sigma].index

df_preproc = df_pg_nan.loc[inlier(df_pg_nan, 'body_mass_g', 2)]
