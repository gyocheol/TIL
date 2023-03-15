import pandas as pd
import requests
import os
import time
import datetime
import urllib3
'''
20000101 은 완료
'''
start = ['20080101']
end = ['20081231']

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


# 회사번호, 회사이름

createDirectory('fslist')
col_list = ['cor_name', 'rpt_year', 'rpt_month', 'rcpNo', 'dcmNo', 'eleId', 'offset', 'length', 'dtd', 'tocNo']

for i in range(len(start)):
    start_time = datetime.datetime.now()
    val_list = []
    df = pd.read_csv(f'./rpt_info/{start[i]}-{end[i]}.csv', engine='python')
    for j in range(len(df["rcp_num"])):
        rcp_no = df["rcp_num"][j]
        year = df["rpt_year"][j]
        print(len(df["rcp_num"]), '/', j)
        try:
            urllib3.disable_warnings()
            path = f'https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcp_no}'
            js = requests.get(path, verify=False).text
            idx = js.find('요약재무정보')
            idx2 = js.find('재무에 관한 사항')
            value = js[idx:idx + 300]
            value2 = js[idx2:idx2 + 300]
            val = value.split('"')
            val2 = value2.split('"')
            val_l = [df["cor_name"][j], year, df["rpt_month"][j]]
            if idx == -1:
                for k in range(2, len(val2)+1, 2):
                    try:
                        val_l.append(val2[k])
                    except:
                        pass
            else:
                for k in range(2, len(val)+1, 2):
                    try:
                        val_l.append(val[k])
                    except:
                        pass
            try:
                val_list.append(val_l[:3] + val_l[4:])
                print(val_l)
                time.sleep(1)
            except:
                time.sleep(1)
                pass
        except:
            pass

    df = pd.DataFrame(val_list, columns=col_list)
    end_time = datetime.datetime.now()
    df.to_csv(f"./fslist/{start[i]}-{end[i]}.csv", encoding="utf-8-sig")
    print(f"============{start[i]}-{end[i]}.csv 완료!! 걸린시간 : {end_time-start_time}============")
