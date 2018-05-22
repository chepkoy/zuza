import pandas as pd
from urlextract import URLExtract

dataset = pd.read_csv('zuza.tsv', delimiter = '\t', quoting = 3)
extractor = URLExtract()
urls = extractor.find_urls(dataset['Notes'][63])
