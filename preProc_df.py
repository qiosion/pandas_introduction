import pandas as pd

# DataFrame 생성
print(">>> 데이터프레임 생성")
# 1. dict 타입을 정의한 뒤, pd.DataFrame(dict) 로 데이터프레임을 생성한다
# 열 이름을 key로, 리스트를 value로 갖는 딕셔너리 정의
dict_data = {
    'c0': [1,2,3], 'c1': [4,5,6], 'c2': [7,8,9],
    'c3': [10,11,12], 'c4': [13,14,15]
}
# 데이터 프레임을 생성하는 방법은 시리즈와 동일하다
df = pd.DataFrame(dict_data)
print("타입 : " , type(df))
print(df)

# 2. 배열 지정, index 지정, 컬럼명 지정해서 데이터프레임 생성
df = pd.DataFrame(
    [
        [23, '남', '서울'],
        [22, '여', '대구'],
        [24, '여', '대전']
    ],
    index=['홍길동', '강은선', '구보람'],
    columns=['나이', '성별', '지역']
)
print(df)

# 인덱스, 열이름을 변경
print(">>> 인덱스, 칼럼명 변경")
# 1. df.index=[새로운배열], df.colums=[원하는 배열]
# 2. df.rename(index={'홍길동':'학생1', ...}, inplace=True)

# 이름 ==> 학생1, 2, 3 으로 변경 ==> rename ==> 이름으로 변경
df.index = ['학생1','학생2','학생3']
print(df)
df.rename(index={
    '학생1': '가나다',
    '학생2': '라마바',
    '학생3': '사아자'
}, inplace=True)
print(df)

# 나이, 성별 ==> 연령, 남여구분 으로 변경
df.rename(columns={
    '나이': '연령',
    '성별': '남여구분'
}, inplace=True)
print(df)

# drop
print(">>> drop 삭제")
exam_data = {
    # 열(칼럼) : 행
    'AI_SW': [90, 80, 70],
    'DS': [98, 82, 71],
    'JAVA': [92, 100, 90],
    'ML': [76, 88, 85],
    'Eng': [60, 45, 100],
    'DB': [30, 25, 20]
}
df = pd.DataFrame(exam_data, index=['학생1', '학생2', '학생3'])
print(df)

# 한 행을 삭제하고 df2에 저장
df2 = df.drop('학생1') # axis=0 (Default) : 행 기준으로 삭제
print(df2)

# 학생 1, 2를 삭제 -> for문 적어도 상관없지만 배열로 한번에 삭제 가능!
df3 = df.drop(['학생1', '학생2'])
print(df3)

# 칼럼(열) 삭제 -> 반드시 축 셋팅 axis=1 필요 !
df4 = df.drop('ML', axis=1)
print(df4)

# 원본 객체를 변경
# df.drop('DS', axis=1, inplace=True)
# print(df)

print(">>> loc와 iloc")
# loc : 인덱스의 이름으로 가지고 오는 것
# iloc : 인덱스 번호(숫자)로 가지고 오는 것
# df = pd.DataFrame(exam_data, index=['학생1', '학생2', '학생3'])
row1 = df.loc['학생1']
print(row1, type(row1))

row2 = df.iloc[0]
print(row2, type(row2))

# 컬럼을 가지고 오는 방법
# 1. df.컬럼명
# 2. df['컬럼명']
# 3. df[['col1', 'col2', 'col3']]

# 여러 행을 가지고 오기
print(">>> 여러행")
df_1 = df.loc[['학생1', '학생3']]
print(df_1)
df_1 = df.iloc[[0, 2]]
print(df_1)
# 슬라이싱
df_1 = df.loc['학생1':'학생3'] # 이상:이하
print(df_1)
df_1 = df.iloc[0:3] # 이상:미만
print(df_1)

# Series : 학생 1의 AI_SW, JAVA 점수
ai_java = df.loc['학생1', ['AI_SW', 'JAVA']]
print(ai_java)

# DataFrame : 학생 1, 3의 AI_SW, JAVA 점수
ai_java = df.loc[['학생1', '학생3'], ['AI_SW', 'JAVA']]
print(ai_java)

# loc ==> iloc 로 변경하여 동일한 데이터 추출
ai_java = df.iloc[[0, 2], [0, 2]]
print(ai_java)

# 슬라이싱 사용하여 데이터 추출
print(">>> 이차원 배열 슬라이싱")
ai_ds = df.iloc[0:2, 0:2]
print(ai_ds)