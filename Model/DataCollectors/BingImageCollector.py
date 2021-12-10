from bing_image_downloader import downloader
import pandas as pd
import os

data=pd.read_csv('DiseaseList.csv')

# print(data.head())


for disease in data.iloc[1:9,0]:
    downloader.download(disease, limit=1200,  output_dir='../Data_V/', adult_filter_off=False, force_replace=False, timeout=15)

print("Dataset construction complete!")

