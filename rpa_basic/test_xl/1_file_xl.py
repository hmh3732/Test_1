from openpyxl import Workbook
wb = Workbook()  # 새 워크북 생성
ws = wb.active  # 현재 활성화된 Sheet 가져옴
ws.title = "exam test"  # Sheet의 이름을 변경
wb.save("d:/sample.xlsx")  # 워크북을 sample.xlsx 파일로 저장
wb.close()  # 워크북 닫기