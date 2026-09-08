m_str = '"서울특별시  (1100000000)","9,330,658","4,482,949","          2.08","4,504,432","4,826,226","          0.93"'
test=m_str.split('","')
for i,t in enumerate(test):
    t=t.replace('"','')
    t=t.replace(',','')
    t=t.replace('\xa0','')
    t=t.replace('\u200b','')
    t=t.replace('\ufeff','')
    t=t.strip()
    if t.isdigit():
        test[i]=float(t)
    print(t)
print(test)
# ---------------------------------------------
print("서울 전체 인구의 남성 비율:{:.2f}% ".format(test[4]/test[1*100]))
print("서울 전체 인구의 여성 비율:{:.2f}% ".farmat(test[5]/test[1*100]))