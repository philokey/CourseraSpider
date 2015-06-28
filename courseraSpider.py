import requests
import re
import urllib.parse
class CourseraSpider(object):
	def __init__(self, url, email, password):
		self.loginUrl = "https://www.coursera.org/api/login/v3Ssr?csrf3-token=undefined"
		self.url = url
		self.email = email
		self.password = password
	def login(self): #post
		postData = {'email' :self.email, 'password' : self.password}
		header = {
		    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
			'Host':'www.coursera.org',
			'Origin':'https://www.coursera.org',
			'Referer':'https://www.coursera.org/?authMode=login'
		}
		s = requests.session()
		s.post(self.loginUrl, postData)
		return s
	def startSpider(self):
		s = self.login()
		response = s.get(self.url)
		vedioLinks, pdfLinks, subtitleLinks = self.getLinks(response.text)
		print ("vedioLinks")
		for v in vedioLinks:
			print (v)
		print ("pdfLinks")
		for p in pdfLinks:
			print (p)
		print ("subtitleLinks")
		for s in subtitleLinks:
			print (s)
	def getLinks(self, content):
		vedioLinks = re.findall(r'<a.*?href="(.*?mp4.*?)"', content)
		pdfLinks = re.findall(r'<a.*?href="(.*?pdf.*?)"', content) 
		subtitleLinks = re.findall(r'<a.*?href="(.*?srt.*?)"', content)
		return vedioLinks, pdfLinks, subtitleLinks

def main():
	email = 'philokeys@gmail.com'
	password = '19931012'
	courseName = "progfun-005"
	url = "https://class.coursera.org/{course}/lecture"
	spider = CourseraSpider(url.format(course = courseName), email, password)
	spider.startSpider()

if __name__ == '__main__':
	main()
	#r = requests.get("https://d396qusza40orc.cloudfront.net/progfun/lecture_slides/week1-1.pdf", stream = True)
	#print ("OK")
	#r = requests.get("https://class.coursera.org/progfun-005/lecture/subtitles?q=115_en&format=srt", stream = True)
	#print (r.headers)
	#r = requests.get("https://class.coursera.org/progfun-005/lecture/download.mp4?lecture_id=7", stream = True)
	#print (r.headers)
	#s = urllib.parse.unquote( r.headers['Content-Disposition'])
	#filename = re.findall(r'filename="(.*?)"', s)
	#print (filename[0])
	#with open(filename[0], "wb") as tmp:
	#	for chunk in r.iter_content(chunk_size=1024):
	#		tmp.write(chunk)
	#		tmp.flush()
