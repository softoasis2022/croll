from openpyxl import load_workbook
import pandas as pd

# 새로운 데이터
new_data = {
    "판매회사": "회사4",
    "제품이름": "제품D",
    "용량": 400,
    "가격": 40000,
    "배송비": 4000,
    "링크": "http://link4.com"
}

# 파일 경로 변경: D 드라이브로 변경
filename = "원두.xlsx"

# 엑셀 파일 로드
wb = load_workbook(filename)
ws = wb.active

# 새로운 데이터를 엑셀 파일에 추가
new_row = [new_data["판매회사"], new_data["제품이름"], new_data["용량"], new_data["가격"], new_data["배송비"], new_data["링크"]]
ws.append(new_row)

# 변경사항 저장
wb.save(filename)

print(f"{filename}에 새로운 데이터가 추가되었습니다.")


'''

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
에러 확인 : 확이 방법은 chatgpt 4사용
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


에러 메시지 ValueError: All arrays must be of the same length는 pandas의 DataFrame을 생성할 때 제공된 데이터 중 하나 이상의 배열(리스트)의 길이가 다른 배열과 다르기 때문에 발생합니다. 즉, 모든 컬럼(딕셔너리의 키에 해당하는 값들의 리스트)은 동일한 길이를 가져야 합니다.

코드에서 data 딕셔너리의 "가격" 키에 해당하는 리스트에만 값을 추가했기 때문에, "가격" 리스트의 길이는 4가 되지만, 다른 키("판매회사", "제품이름", "용량", "배송비", "링크")에 해당하는 리스트의 길이는 여전히 3입니다. 이로 인해 pd.DataFrame(data)를 호출할 때 에러가 발생합니다.

이 문제를 해결하기 위해서는 모든 키에 대응하는 리스트에 동일한 개수의 요소를 추가해야 합니다. 예를 들어, 각 리스트에 하나의 요소를 추가하려면 다음과 같이 할 수 있습니다:
'''
