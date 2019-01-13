# To run this, you need to install BeautifulSoup if you aren't using anaconda
# https://pypi.python.org/pypi/beautifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import unittest

def getSumSpans(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    lines = soup.find_all('tr')[1:]
    span_tags = 0
    for line in lines:
        span_tags += int(line.span.string)
    return span_tags

def followLinks(url, numAnchor, numTimes):
    input_html = urlopen(url).read()
    soup = BeautifulSoup(input_html, 'html.parser')
    ex = soup.find_all('a', None)[numAnchor - 1]


    for x in range(numTimes):
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        a_return = soup.find_all('a', None)[numAnchor - 1]
        url = a_return.get('href', None)

    return a_return.string

def getGradeHistogram(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.find_all('tr')[1:]
    d = {90:0 , 80:0, 70:0, 60:0, 50:0, 40:0, 30:0, 20:0, 10:0, 0:0}
    for line in trs:
        num = (line.span.string)
        if len(num) == 1:
            d[0] += 1
        else:
            if num[0] == '9':
                d[90] += 1
            elif num[0] == '8':
                d[80] += 1
            elif num[0] == '7':
                d[70] += 1
            elif num[0] == '6':
                d[60] += 1
            elif num[0] == '5':
                d[50] += 1
            elif num[0] == '4':
                d[40] += 1
            elif num[0] == '3':
                d[30] += 1
            elif num[0] == '2':
                d[20] += 1
            else:
                d[10] += 1
    l = []
    for ky in d.keys():
        l.append((ky, d[ky]))
    return l


class TestHW7(unittest.TestCase):

    def test_sumSpan1(self):
        self.assertEqual(getSumSpans("http://py4e-data.dr-chuck.net/comments_42.html"), 2553)

    def test_sumSpan2(self):
        self.assertEqual(getSumSpans("http://py4e-data.dr-chuck.net/comments_132199.html"), 2714)

    def test_followLinks1(self):
        self.assertEqual(followLinks("http://py4e-data.dr-chuck.net/known_by_Fikret.html",3,4), "Anayah")

    def test_followLinks2(self):
        self.assertEqual(followLinks("http://py4e-data.dr-chuck.net/known_by_Charlie.html",18,7), "Shannah")

    def test_getGradeHistogram(self):
        self.assertEqual(getGradeHistogram("http://py4e-data.dr-chuck.net/comments_42.html"), [(90, 4), (80, 4), (70, 7), (60, 7), (50, 6), (40, 3), (30, 5), (20, 4), (10, 6), (0, 4)])


unittest.main(verbosity=2)
