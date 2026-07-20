mablagh=int(input('mablagh kharid ro begoo: '))
if mablagh>50000:
    mablagh_ba_off = int(mablagh-((20*mablagh)/100))
    print(mablagh_ba_off)
elif 20000<mablagh<50000 :
    mablagh_ba_off = int(mablagh-((10*mablagh)/100))
    print(mablagh_ba_off)
else:
    print(mablagh)