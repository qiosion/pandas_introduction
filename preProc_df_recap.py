import pandas as pd

exam_data = {
    # 열(칼럼) : 행
    'AI_SW': [90, 80, 70],
    'DS': [98, 82, 71],
    'JAVA': [92, 100, 90],
    'ML': [76, 88, 85],
    'Eng': [60, 45, 100],
    'DB': [30, 25, 20]
}

df = pd.DataFrame(exam_data, index=['강은선', '구보람', '김권아'])
# 인덱스값 주지 않으면 0부터 순서대로 들어감
print(df)

# 자료구조 Data Structure의 점수 : df.DS
exam_dataStructure = df['DS']
print(exam_dataStructure)

# AI 소프트웨어와 자바 점수
exam_ai_java = df[['AI_SW', 'JAVA']]
print(exam_ai_java)

# 학생1의 AI_SW 점수 : df[row, col]
point_ai_sw = df.loc['강은선', 'AI_SW'] # iloc[0, 0], iloc[0, 1]
print(point_ai_sw)

# 학생1에 대한 두개 이상의 시험 성적
point_ai_java = df.loc['강은선', ['AI_SW', 'JAVA']] # iloc[0, [0, 2]]
print(point_ai_java)

# 슬라이싱 : AI_SW ~ ML 성적
slice_ai_ml = df.loc['강은선', 'AI_SW' : 'ML']
print(slice_ai_ml)
# DS ~ DB(끝까지) 성적
slice_ai_ml2 = df.iloc[0, 1:]
print(slice_ai_ml2)

# 특정 행들의 특정 열 가져오기
exam_partial = df.loc[['구보람', '김권아'], ['DS', 'JAVA']]
print(exam_partial)