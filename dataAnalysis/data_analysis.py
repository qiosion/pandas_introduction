import pandas as pd

# 모든 칼럼 확인가능
pd.set_option('display.max_columns', None)

# header = None 으로 지정할 필요 있음. 데이터 첫줄에 칼럼이 없어서
df = pd.read_csv("../Data/auto-mpg.csv", header=None)

# 열이름 지정
df.columns = ["mpg", "cylinders", "displacement", "horsepower",
              "weight", "acceleration", "model year", "origin", "name"]

# # head(n), tail(n) : 상위 몇개 또는 하위 몇개를 볼 수 있음. n 디폴트 5
# print(df.head()) # 5개
# print(df.tail(10)) # 10개
#
# print(df.shape) # (398, 9) : 398개의 행, 9개의 열
# print(df.info()) # df의 각 열에 대한 상세 정보를 출력
#
# print(df.describe()) # 산술 가능한 컬럼에 대해서만 계산해서 통계를 보여줌
#
# # object(string) 데이터에 대해서도 통계 정보를 보고싶은 경우,
# # include 옵션에 all
# print(df.describe(include="all"))
#
# # object 만 보고싶을 경우 include="object"
# # 숫자형만 보고싶을 경우 include="number"
#
# print(df.count())
#
# # value_counts : 특정 열이 가지고 있는 고유값의 개수를 반환
# unique_values = df['origin'].value_counts()
# print(unique_values)
#
# # dropna = True : NaN을 카운팅하지 않음
# unique_values = df.origin.value_counts(dropna=True)
# print(unique_values)
#
# import seaborn as sns
# # 타이타닉에서 남여별 생존자 수 / 사망자 수
# titanic = sns.load_dataset("titanic")
# # print(titanic.info())
# print(titanic.head())
# # print(titanic.describe())
#
# print(titanic[["survived", "sex"]].value_counts())
#
# # 통계
# # mean : 평균
# print(df.mean()) # 모든 칼럼에 대한 평균
#
# # median : 중간값
# print(df.mpg.median()) # mpg 칼럼에 대한 중간값
#
# # min / max
# print(df[['mpg', 'weight']].max())# 두개의 컬럼에 대한 max값
#
# # std : 표준편차
# print(df[['origin']].std())
#
# # corr : 상관계수
# print(df.corr())# 모든 열의 상관계수
#
# # mpg와 weight 의 상관관계를 출력
# print(df[["mpg", "weight"]].corr(method="spearman")) # 두 열의 상관계수
#
# print(df.corrwith(df['mpg'])) # mpg와 다른 열들 간의 상관관계

# horsepower 에 있는 값 ? 를 처리해보자
print(df.horsepower.unique()) # '?'가 포함되어있는지를 확인

"""
1. ? 를 NaN 로 변경
2. NaN를 포함한 행을 삭제 : drona
3. type 을 object 에서 float 으로 변경
4. corr 이용하여 마력(horsepower)과 mpg 가 음의 상관관계인지 확인
"""
import numpy as np

# 1. ?를 np.nan 으로 교체해라. 당장(inplace=True)
df['horsepower'].replace('?', np.nan, inplace=True)

# 2. NaN을 포함한 행을 삭제
df.dropna(axis=0, inplace=True)
print(df.horsepower.unique())
print(df.info()) # horsepower 칼럼의 데이터 타입은 여전히 object

# 3. horsepower 칼럼의 타입을 float으로 바꿔주자 : 형변환 astype(타입)
df['horsepower'] = df['horsepower'].astype('float')
print(df.info())

# 4. 상관계수 확인
print(df[['mpg', 'horsepower']].corr(method='spearman'))


