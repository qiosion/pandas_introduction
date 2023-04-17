import pandas as pd


# HTML
url = './Data/sample.html'
tables = pd.read_html(url)
print(tables)
print('테이블 갯수 : ', len(tables)) # 테이블 갯수

# 테이블 별로 데이터 프레임에 담아줄 수 있음
print('>>> df1')
df1 = tables[0]
print(df1)
print('>>> df2')
df2 = tables[1]
print(df2)

print('>>> df2의 name을 인덱스로 사용')
df2.set_index(['name'], inplace=True)
print(df2)

# 데이터 출력(저장)
# CSV 저장
# 판다스 DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
data = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ["A", "A+", "B"],
        'basic' : ["C", "B", "B+"],
        'c++' : ["B+", "C", "C+"]
        }
df = pd.DataFrame(data)
df.set_index('name', inplace=True) # name 열을 인덱스로 지정
print(df)
# to_csv() 메서드를 통해 CSV 파일로 저장하기
df.to_csv('./Data/df_sample.csv')


# # EXCEL 저장
# # ExcelWriter : 여러 시트 사용 -> sheet 지정
# writer = pd.ExcelWriter('./Data/df_excelWriteExam.xlsx')
# df1.to_excel(writer, sheet_name="html_tb1")
# df2.to_excel(writer, sheet_name="html_tb2")
# writer.save()

# # EXCEL
# df = pd.read_excel('./Data/남북한발전전력량.xlsx',
#                    engine='openpyxl',
#                    header=None)
# print(df)

# # JSON
# # 파일경로를 변수에 저장
# filePath = './Data/read_json_sample.json'
#
# df = pd.read_json(filePath)
# print(df)
# print("인덱스 : ", df.index)

# # CSV
# 파일경로를 변수에 저장
# filePath = './Data/read_csv_sample.csv'
#
# df = pd.read_csv(filePath)
# print(df)
#
# # header : 열 이름이 되는 행을 지정
# # 컬럼 이름이 자동으로 갯수만큼 증가 (0부터 n-1까지)
# # c0, c1, c2, c3 : 칼럼명을 그냥 그대로 데이터로 사용
# df = pd.read_csv(filePath, header=None)
# # print(df)
#
# # 특정 행을 열이름으로 사용 -> header=행번호(index)
# # 헤더로 지정한 행 부터 그 아래를 출력
# df = pd.read_csv(filePath, header=1)
# # print(df)
#
# # index_col : 행주소가 되는 열을 지정
# df = pd.read_csv(filePath, index_col='c1')
# print(df)