import pandas as pd
import requests
import os
import time
import datetime

'''
start=['20000101','20010101','20020101','20030101','20040101','20050101','20060101','20070101','20080101','20090101'
    ,'20100101','20110101','20120101','20130101','20140101','20150101','20160101','20170101','20180101','20190101','20200101'
    ,'20210101','20220101','20230101']
end=['20001231','20011231','20021231','20031231','20041231','20051231','20061231','20071231','20081231','20091231'
    ,'20101231','20111231','20121231','20131231','20141231','20151231','20161231','20171231','20181231','20191231','20201231'
    ,'20211231','20221231','20230308']
'''
start = ['20080101','20090101'
    ,'20100101','20110101','20120101','20130101','20140101','20150101','20160101','20170101','20180101','20190101','20200101'
    ,'20210101','20220101','20230101']
end = ['20081231','20091231'
    ,'20101231','20111231','20121231','20131231','20141231','20151231','20161231','20171231','20181231','20191231','20201231'
    ,'20211231','20221231','20230308']

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


createDirectory('fslist')   # fslist 폴더가 없다면 만들고 있다면 pass
col_list = ['name', 'yyyymm', 'eleId', 'offset', 'length', 'dtd', 'tocNo']  # name : 회사 이름 / yyyymm : 만들어진 년도와 월

# for i in range(len(start)):
for i in range(1):
    start_time = datetime.datetime.now()
    val_list = []
    df = pd.read_csv(f'./crp_num/{start[i]}-{end[i]}.csv')
    for j in range(len(df["rcp_num"])):
        rcp_no = df["rcp_num"][j]
        path = f'https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcp_no}'
        js = requests.get(path).text
        idx = js.find('요약재무정보')
        value = js[idx:idx+300]         # javascript 로 만들어진 파일이 와서 인덱스로 짜름
        val = value.split('"')
        # val_l = [df["name"][j], df["year"][j]]        # csv 랑 이름 맞추기
        val_l = [0, 0]
        for v in val:
            try: val_l.append(int(v))
            except: pass

        val_list.append(val_l[:2] + val_l[4:])
        time.sleep(1)

    df = pd.DataFrame(val_list, columns=col_list)
    df.to_csv(f"./fslist/{start[i]}-{end[i]}.csv")
    end_time = datetime.datetime.now()
    print(f"============{start[i]}-{end[i]}.csv 완료!! 걸린시간 : {end_time-start_time}============")
