import pandas as pd
import requests
import time
import zipfile
import os

#  보고서 번호 확인
start_date_arr = ['20000101', '20030101', '20060101', '20090101', '20120101', '20150101', '20180101', '20210101']
end_date_arr = ['20021231', '20051231', '20081231', '20111231', '20141231', '20171231', '20201231', '20230308']


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

    with open(f'./raw/{file_name}.zip', 'wb') as stock_file:   # open in binary mode
        stock_file.write(response.content)      # write to file
        time.sleep(5)
        zip_file = zipfile.ZipFile(f'./raw/{file_name}.zip')
    #     zipfile.ZipFile(f"./raw/{file_name}.zip").extract(f"{file_name}.xml", directory)


for i in range(len(start_date_arr)):
    start_date, end_date = start_date_arr[i], end_date_arr[i]
    df = pd.read_csv(f'./data/{start_date}-{end_date}.csv')
    # print(df["rcp_num"])
    count = 1
    for rcp_num in df["rcp_num"]:
        print(count)
        if not count % 90:
            time.sleep(60)
        count += 1
        path = f'https://opendart.fss.or.kr/api/document.xml?crtfc_key=96757bd197077b9a35140d3f9e3e13683060c30b&rcept_no={str(rcp_num)}'
        download(path, str(rcp_num), rcp_num, i)

