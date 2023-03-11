import pandas as pd
import requests
import time
import zipfile
import os

#  보고서 번호 확인
start_date_arr=['20000101','20010101','20020101','20030101','20040101','20050101','20060101','20070101','20080101','20090101'
    ,'20100101','20110101','20120101','20130101','20140101','20150101','20160101','20170101','20180101','20190101','20200101'
    ,'20210101','20220101','20230101']
end_date_arr=['20001231','20011231','20021231','20031231','20041231','20051231','20061231','20071231','20081231','20091231'
    ,'20101231','20111231','20121231','20131231','20141231','20151231','20161231','20171231','20181231','20191231','20201231'
    ,'20211231','20221231','20230308']



def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def download(url, file_name, num, index):
    directory = start_date_arr[index][:4]
    createDirectory(directory)
    response = requests.get(url)  # get request
    print(response.content.__sizeof__(), num)
    if response.content.__sizeof__() == 180:
        return
    with open('./raw/'+file_name+'.zip', 'wb') as stock_file:   # open in binary mode
        stock_file.write(response.content)      # write to file

    zipfile.ZipFile(f'./raw/{file_name}.zip').extract(f'{file_name}.xml',directory)


for i in range(len(start_date_arr)):
    start_date, end_date = start_date_arr[i], end_date_arr[i]
    df = pd.read_csv(f'./{start_date}-{end_date}.csv')
    # print(df["rcp_num"])
    count = 1
    for rcp_num in df["rcp_num"]:
        print(count)
        if not count % 90:
            time.sleep(60)
        count += 1
        url = f'https://opendart.fss.or.kr/api/document.xml?crtfc_key=9bf5e691d036fe31c77b693b8958ebc167d62a1e&rcept_no={str(rcp_num)}'
        download(url, str(rcp_num), rcp_num, i)