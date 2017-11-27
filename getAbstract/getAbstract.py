


from urllib2 import HTTPError
import xml.etree.ElementTree
import os,re, sys, httplib
from urlparse import urlparse


def isNodeTag (node,nodeTag): ## Breadth-first search approach. 
  queue = [node]
  if node.tag == nodeTag: 
    return node, node.text 
  if len(node.getchildren())==0: 
    return "tag+not+found"
  queue.remove(node)
  queue = queue + node.getchildren()
  while len(queue)>0: ## not empty 
    node = queue[0] ## node to be removed 
    queue.remove(node)
    if node.tag == nodeTag: 
      return node
    if len(node.getchildren())>0: ## add more nodes to "probe" 
      queue = queue + node.getchildren()
  return "tag+not+found"
  

def getAbstract (paperName,genericFunc,**kwargs):
  argList = {'Year':0,'ISOAbbreviation':'none'}
  for key in kwargs: 
    if key not in argList: 
      print key + ' option not supported' 
      continue
    argList[key] = kwargs[key]
  ##
  tree = xml.etree.ElementTree.parse(paperName)
  for node in tree.iter():
    if node.tag == "PubmedArticle" :
      try: 
        DateCreated = isNodeTag(node,"DateCreated") ## @DateCreated is a node in the xml, gets time when paper was completed
        year = isNodeTag(DateCreated,"Year").text     
        date = isNodeTag(DateCreated,"Day").text
        month = isNodeTag(DateCreated,"Month").text
        ArticleTitle = isNodeTag(node,"ArticleTitle").text ## paper title 
        Abstract = isNodeTag(node,"Abstract")
        AbstractText = isNodeTag(Abstract,"AbstractText").text ## abstract text (may be limited if over 400 words)
        Journal = isNodeTag(node,"Journal")
        JournalTitle = isNodeTag(Journal,"Title").text 
        JournalAbbrev = isNodeTag(Journal,"ISOAbbreviation").text
      except: 
        continue ## something not found. like Journal not found/ Abstract not found etc...
      ### filter the output 
      if argList['Year']!=0:
        if int(year) != argList['Year']:
          continue
      if argList['ISOAbbreviation']!='none':
        if JournalAbbrev != argList['ISOAbbreviation']:
          continue
      ## do something to @AbstractText with @genericFunc generic function 
      thisPaperOutcome = genericFunc(AbstractText)

    
paperName = "/u/flashscratch/d/datduong/pubmedAbstractBaseLineYearly/baseline/medline17n0305.xml" 

getAbstract(paperName)

