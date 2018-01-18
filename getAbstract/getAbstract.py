from urllib2 import HTTPError
import xml.etree.ElementTree
import os,re,sys
import argparse
import httplib
from urlparse import urlparse

from urlXmlUtil import * 
  
 
paperName = "/u/flashscratch/d/datduong/pubmedArticle4Dec17/journalWanted/Bioinformatics/PMC2530882.nxml" 
getHttpStatus(paperName,'abstract')

## see outpt in the format
## PubmedId, Year, KeyWord related to link, Link, LinkStatus, StatusCode. 
## '18628289 2008 download http://www.systemsbiology.co.kr/PathCluster/ -1 '

## Status code: 
# -1 is Connection Timeout 
# 200-299: working link
# 300-399: redirected link 
# 400 and over: broken link
