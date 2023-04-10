import pandas as pd

std1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})

# 시리즈 객체 vs 숫자 연산
# 100분율 norm (정규화 Normalize)
percentage = std1 / 100
print(percentage)

# 시리즈 객체 vs 시리즈 연산
# 모든 데이터가 존재할 때 사칙연산
# 시리즈와 시리즈를 계산할때 인덱스 기준으로 정렬sorting 한다
std1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
std2 = pd.Series({'수학': 100, '국어': 80, '영어': 90})

# 사칙연산
add = std1 + std2
sub = std1 - std2
mul = std1 * std2
div = std1 / std2

# 결과를 DataFrame 형태로 표현
result = pd.DataFrame([add, sub, mul, div], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
# 시리즈들이 들어가고 그 각각들이 행을 구성할 것 ..? 뭐래니..
print(result)

# NaN가 발생하는 예시를 만들어보자 => 모든 데이터가 존재하지 않음
std1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
std2 = pd.Series({'수학': 100, '국어': 80})

# 사칙연산
add = std1 + std2
print(add) # 영어 더하기 값이 나오지 않음

# fill_value를 통해 값을 집어넣어서 해보자
# 사칙연산
add_data = std1.add(std2, fill_value=0)
sub_data = std1.sub(std2, fill_value=0)
mul_data = std1.mul(std2, fill_value=0)
div_data = std1.div(std2, fill_value=1) # 나누기를 0으로 대체하면 무한대 inf 가 뜸

result2 = pd.DataFrame([add_data, sub_data, mul_data, div_data], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result2)
