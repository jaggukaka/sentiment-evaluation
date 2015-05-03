import sys
import csv
import codecs
import re

def seg_file(dfile):

    inpTweets = csv.reader(open(dfile, 'rU'), dialect=csv.excel_tab, delimiter=',', quotechar='|')
    pfile = codecs.open(dfile + '_gs', 'w', 'utf8')
    for row in inpTweets:
        sentiment = row[0]
        tweet = unicode(row[1], errors='ignore').replace('\n', ' ').strip()
        if sentiment == 'positive':
            pfile.write(tweet + '\t' + '+' + '\n')
        elif sentiment == 'negative':
            pfile.write(tweet + '\t' + '-' + '\n')
        elif sentiment == 'neutral':
            pfile.write(tweet + '\t' + '0' + '\n')
        else :
            pfile.write(tweet + '\t' + 'X' + '\n')


if __name__ == '__main__':

    seg_file(sys.argv[1])

