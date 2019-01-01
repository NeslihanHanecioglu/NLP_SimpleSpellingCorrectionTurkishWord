#!/usr/bin/env python
# -*- coding: utf-8 -*-


#This code computes edit distances  of words in the corpus and entering word
from random import randint
import xml.etree.ElementTree as ET
import MySQLdb
import os

#This method calculates edit distance and return this result
def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

s = raw_input("Please enter a word: ")
db=MySQLdb.connect("localhost","root","Password","NLPOdev",charset='utf8')
with db: 

    cursor = db.cursor()
#The following query Retrieve all words from MSTT whose length is between |s|-1 and |s|+1 and whose first two letters are the same as the first two letters of s.
    cursor.execute("SELECT TRIM(Word) from NLP where LENGTH(TRIM(Word)) BETWEEN %d AND %d AND SUBSTRING(TRIM(Word),1,1) LIKE '%s' AND SUBSTRING(TRIM(Word),2,1) LIKE '%s'"%(len(s)-1,len(s)+1,s[0],s[1], ))
#The following code travers all words,which result of the above query.and calculates edit distance between these words and s.   
    while (1):
     row = cursor.fetchone ()
     if row == None:
        break
     if edit_distance(s, row[0]) ==0:    
        print  "Did you mean ? %s" % row[0]
db.close()




