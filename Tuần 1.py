##---------------------- Bài 1. Viết hoa toàn bộ chữ cái đầu từ trong câu cho trước nhập vào từ bàn phím. Các chữ cái còn lại viết thường. -------------------------
t = int(input())
if 0<t and t<=100:
    for i in range (1,t+1):
        c=input()
        print(f"Test{i}:\n{c.title()}")

##---------------------- Bài 2. Đếm số lượng nguyên âm, phụ âm trong câu cho trước. ------------------------
t = int(input())
nguyenAm = "ueoaiUEOAI"
tongNguyenAm = 0
if 0<t and t<=100:
    for i in range(1, t + 1):
        chuoi=input()
        for dem in nguyenAm:
            tongNguyenAm += chuoi.count(dem)
        khoangtrang=chuoi.count(" ")
        khoangtab=chuoi.count("\t")
        tongPhuAm=len(chuoi)-tongNguyenAm-khoangtrang-khoangtab
        print(f"Text {i}:\n",tongNguyenAm,"\n",tongPhuAm)

##---------------------- Bài 3. Đếm số từ có trong một chuỗi kí tự cho trước nhập vào từ bàn phím. ------------------------
t= int(input())
a=" \t"
if 0<t and t<=100:
    for i in range(1, t + 1):
        chuoi = input()
        for dem in a:
            sotu=chuoi.split()
        print(f"Test {i} :",len(sotu))

##---------------------- Bài 4. Liệt kê các từ theo thứ tự xuất hiện trong câu. Các từ phân tách nhau bằng 1 dấu cách. ------------------------
t = int(input())
a=" \t"
if 0 < t and t <= 100:
    for i in range(1, t + 1):
        chuoi = input()
        for dem in a:
            c = chuoi.split()
        print(" ".join(c))
##---------------------- Bài 5. Tìm số lần xuất hiện của chuỗi s2 trong chuỗi s1 ------------------------
t = int(input())
if 0 < t and t <= 100:
    for i in range(1, t + 1):
        s1=input()
        s2=input()
        print(f"Test {i}:",s1.count(s2))

##---------------------- Bài 6. Thay thế toàn bộ chuỗi old bởi chuỗi new trong chuỗi string.-------------
t = int(input())
if 0 < t and t <= 100:
    for i in range(1, t + 1):
        s=input()
        old=input()
        new=input()
        print(f"Test {i}:",s.replace(old,new))

##---------------------- Bài 7. Hiển thị các từ sao cho chúng chỉ xuất hiện duy nhất 1 lần theo đúng thứ tự xuất hiện từ đầu chuỗi đến cuối chuỗi.-------------
t = int(input())
for i in range(1, t+1):
    c = [x for x in input().split()]
    m = set()
    print(f"Test {i}: ")
    for i in c :
        if i not in m:
            print(f'{i} ', end='')
            m.add(i)
    print()
