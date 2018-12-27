#!/usr/bin/env python3

"""
wcount.py: This module count words from an Internet file
and return the most frequent words.

__author__ = "张序年"
__pkuid__  = "1800094603"
__email__  = "1800094603@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import urllib.error

def wcount(lines, topn=10):
    """count words, which is in small letters and punctuation-removed, 
    from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    If the topn(word count) exceed the number of words avaiable in the given text,
    output all the results of word count.
    """
    wdict = {}
    wlist = []
    
    for word in lines.split():
        fword = word.strip(""",./;'[]`-=~!@#$%^&*"()_+{}?><'""").lower()
        wdict[fword] = wdict.get(fword,0) + 1
    
    for wkey in wdict:
        wlist.append((wkey,int(wdict[wkey])))
  
    wlist.sort(key = lambda x:x[1],reverse = True)
    
    if topn > len(wlist):
        topn = len(wlist)
        
    for times in range(topn):
        print(wlist[times][0]+"\t"+str(wlist[times][1]))

if __name__ == '__main__':
    if  len(sys.argv) == 1:      #if the user doesnt enter anything except the file name return instructions
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:     #get text from url, try the error which might happen, and decode it, send the data to the wcount function
        try:    
            doc = urlopen(sys.argv[1])
            content = doc.read().decode("utf-8")
            if len(sys.argv)==2:
                wcount(content)
            else:
                wcount(content,int(sys.argv[2]))
        except urllib.error.URLError:
            print("Oops,your URL is wrong!")
        except ValueError:
            print("Oops,you have enter a non-integer for the topn words!") 
        except Exception:
            print("Oops,an unexpected error has happened!")
            
