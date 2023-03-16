from Student import Student
from openpyxl import Workbook
import math

listSV = []
mini = [3, 10]


def getlistSV():
    return listSV


def SortCri(e):
    return e.DTB


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def max(i):
    max = 0
    if i == 0:
        for j in range(len(listSV)):
            if max < len(listSV[j].MaSV):
                max = len(listSV[j].MaSV)

    if i == 1:
        for j in range(len(listSV)):
            if max < len(listSV[j].HovaTen):
                max = len(listSV[j].HovaTen)

    if max < mini[i]:
        max = mini[i]

    return max


def tinhdtb(a, b, c):
    return (a + b + c) / 3


def nhapsv():
    masv = str(input("Nhập Mã Sinh Viên:"))

    name = input("Nhập Họ và Tên:")
    while name.isnumeric() is True:
        name = input("Nhập lại Họ và Tên: ")
    name = str(name)

    toan = input("Nhập điểm Toán:")
    while isfloat(toan) is False and toan.isnumeric() is False:
        toan = input("Nhập lại điểm Toán: ")
    toan = round(float(toan), 1)

    ly = input("Nhập điểm Lý:")
    while isfloat(ly) is False and ly.isnumeric() is False:
        ly = input("Nhập lại điểm Lý: ")
    ly = round(float(ly), 1)

    hoa = input("Nhập điểm Hóa:")
    while isfloat(hoa) is False and hoa.isnumeric() is False:
        hoa = input("Nhập lại điểm Hóa: ")
    hoa = round(float(hoa), 1)

    dtb = tinhdtb(toan, ly, hoa)
    stu = Student(masv, name, toan, ly, hoa, round(dtb, 2))
    listSV.append(stu)
    listSV.sort(key=SortCri)


def showsv(listSV):
    totallen = 0
    for i in range(2):
        totallen += max(i)

    print("_" * (totallen + 39))
    print(
        "| {} | {} | {:^5} | {:^5} | {:^5} | {:^5} |".format("STT".center(max(0)), "Họ và Tên".center(max(1)),
                                                             "Toán", "Lý",
                                                             "Hóa", "ĐTB"))
    for i in listSV:
        print(
            "| {:} | {:} | {:^5} | {:^5} | {:^5} | {:^5} |".format(i.MaSV.center(max(0)), i.HovaTen.center(max(1)),
                                                                   i.Toan, i.Ly, i.Hoa,
                                                                   i.DTB))
    print("|" + "_" * (totallen + 37) + "|")


def inexcel(list):
    wb = Workbook()
    ws = wb.active
    ws.append(["MãSV", "Họ và Tên", "Điểm Toán", "Điểm Lý", "Điểm Hóa", "ĐTB"])
    for item in list:
        ws.append([item.MaSV, item.HovaTen, item.Toan, item.Ly, item.Hoa, item.DTB])
    wb.save("Student.xlsx")


check = -1
while check != 0:
    print("1. Nhập dữ liệu sinh viên")
    print("2. Xem danh sách sinh viên")
    print("3. In ra file excel")

    check= int(input("Nhập số: "))
    while check < 0 or check > 3:
        check = int(input("Nhập lại số: "))

    print("*" * 50)
    if check ==1:
        nhapsv()
    elif check == 2:
        showsv(getlistSV())
    elif check == 3:
        inexcel(getlistSV())
    else:
        break

    print("*" * 50)
