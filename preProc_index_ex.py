import pandas as pd

exam_data = {
    '이름': ['학생1', '학생2', '학생3'],
    'AI_SW': [90, 80, 70],
    'DataS': [98, 82, 71],
    'JAVA': [92, 100, 90],
    'ML': [80, 80, 80]
}

df = pd.DataFrame(exam_data)
# print(df)

# set_index : 이름 컬럼을 행 인덱스로 사용
new_df = df.set_index(['이름']) # df.columns[0]
# print(new_df)

# 인덱스 두개도 설정 가능 -> 이런경우 잘 없긴 하지만..
new_df2 = df.set_index(['AI_SW', 'JAVA'])
# print(new_df2)



# reindex : 행 인덱스 재배열
# fill_value을 통해 NaN 대신 특정 값을 넣을 수 있음
dict_data = {
    'c0': [1,2,3], 'c1': [4,5,6], 'c2': [7,8,9],
    'c3': [10,11,12], 'c4': [13,14,15]
}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
# print(df)

new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
# 해당되지 않는 것은(기존에 없던 인덱스로 인해 생긴 빈칸은) Not a Number로 뜬다.
ndf = df.reindex(new_index, fill_value=0) # NaN 대신 0으로 채운다
# print(ndf)

# Reset Index : 기존 인덱스를 정수형 인덱스로 변경
# 기존 인덱스는 삭제되는 것이 아니라, 그대로 columns로 사용됨
ndf = df.reset_index()
# print(ndf)

# 행인덱스를 기준으로 정렬 sorting
# 디폴트 Default : 오름차순 Ascending
ndf = df.sort_index(ascending=False) # 내림차순 정렬
# print(ndf)

# 열 기준으로 정렬 sorting 가능
dict_data = {
    'c0': [1,2,3], 'c1': [5,4,6], 'c2': [7,8,9],
    'c3': [10,11,12], 'c4': [13,14,15]
}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)

