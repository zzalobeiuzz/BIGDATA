#---------------------- Bai 1 -------------------------
t = int(input())
if 0<t and t<=100:
    for i in range (1,t+1):
        c=input()
        print(f"Test{i}:\n{c.title()}")
        
        
#---------------------- Bai 2 ------------------------
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
