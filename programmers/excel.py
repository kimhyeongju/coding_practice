import win32com.client
excel = win32com.client.Dispatch("Excel.Application")

excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\superuser\\Desktop\\test.xlsx')
ws = wb.ActiveSheet

array = []


for i in range(3,30):
    if ws.Cells(i,8).Value ==


print(ws.Cells(4,3).Value)