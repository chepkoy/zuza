import numpy as np
import pandas as pd
from urlextract import URLExtract

extracted_links = []

for i in range(0, 2003):
    dataset = pd.read_csv('zuza.tsv', delimiter = '\t', quoting = 3)
    extractor = URLExtract()
    urls = extractor.find_urls(dataset['Notes'][i])
    extracted_links.append(urls)

np.savetxt("urls.csv", extracted_links, delimiter=",", fmt='%s')
    