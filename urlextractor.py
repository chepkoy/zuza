# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

"""

import re
import tldextract
import esm

# It doesn't work with naked TLDs - that is where you have a top-level domain but no domain i.e "com" which is technically valid
# It won't work with non-ascii domains unless they've been IDNA encode, if you've got these in your text you can run encode("IDNA") on your string before passing it ind

def extractUrl(text, match):
	pretld, posttld = None, None
	url = ""

	tld = match[1]
	startpt, endpt = match[0][0], match[0][1]

	# check the next character is valid
	if len(text) > endpt:
		nextcharacter = text[endpt]
		if re.match("[a-z0-9-.]", nextcharacter):
			return None

		posttld = re.match(':?[0-9]*[/[!#$&-;=?a-z]+]?', text[endpt:])
	pretld = re.search('[a-z0-9-.]+?$', text[:startpt])

	if pretld:
		url = pretld.group(0)
		startpt -= len(pretld.group(0))
	url += tld
	if posttld:
		url += posttld.group(0)		
		endpt += len(posttld.group(0))

	# if it ends with a . or , strip it because it's probably unintentional
	url = url.rstrip(",.") 

	return (startpt, endpt), url

def parseText(text):
	results = []
	tlds = (tldextract.TLDExtract()._get_tld_extractor().tlds)
	tldindex = esm.Index()
	for tld in tlds:
		tldindex.enter("." + tld.encode("idna"))
	tldindex.fix()
	tldsfound = tldindex.query(text)
	results = [extractUrl(text, tld) for tld in tldsfound]
	results = [x for x in results if x] # remove nulls
	return results

# example usage
# parseText("The website google.com is often user to search the internet, I used it to discover news.ycombinator.com which in turn led me to www.paulgraham.com/articles.html")
