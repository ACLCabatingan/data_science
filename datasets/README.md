# Datasets


## Kaggle Datasets

#### [Setup Kaggle API](https://github.com/Kaggle/kaggle-api/blob/master/README.md):


#### [Download a Dataset](https://medium.com/analytics-vidhya/fetch-data-from-kaggle-with-python-9154a4c610e3):

```python

from kaggle.api.kaggle_api_extended import KaggleApi

#connect
api = KaggleApi()
api.authenticate()

#download
api.dataset_download_file('publisher/dataset','*_.csv')

#extract
zf = ZipFile('*_.csv.zip')
zf.extractall() 
zf.close()
```

## Other Public Datasets

- [Open Data Philippines](https://data.gov.ph/)
- [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets.php)
- [IBM Data Asset eXchange](https://developer.ibm.com/exchanges/data/)