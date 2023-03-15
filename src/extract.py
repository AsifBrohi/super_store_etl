import os
import kaggle

from zipfile import ZipFile
def extract_kaggle_api():
    file_exist = os.path.exists('../data/SampleSuperstore.csv')
    if not file_exist:

        print("collecting data from kaggle api")
        file_download = "bravehart101/sample-supermarket-dataset/SampleSuperstore.csv"
        kaggle.api.dataset_download_file(dataset=file_download,file_name='SampleSuperstore.csv',path='../data/zip')
        print("successfully downloaded dataset")
        with ZipFile('../data/zip/SampleSuperstore.csv.zip','r') as file:
            file.extractall('../data/')
        print("unzipped file")
    print("file already exist")
extract_kaggle_api()