import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class PageManager:
  _instances = {}

  def __new__(cls, url, args):
    if url not in cls._instances:
      cls._instances[url] = super(PageManager, cls).__new__(cls)
    return cls._instances[url]


  def __init__(self, url, args):
    if hasattr(self, 'initialized'):
      return
    self.initialized = True
    self.url = url
    self.args = args
    self.page = None

  def fetchPage(self):
    if self.page is not None:
      return self.page

    self.setPage()
    return self.page

  def setPage(self):
    response = requests.get(self.url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      config = {}
      if (self.args.cssClass is not None):
        config['class'] = self.args.cssClass
      if (self.args.id is not None):
        config['id'] = self.args.id

      contentDiv = soup.find('div', config)
      self.page = contentDiv


  def getLinks(self, linkType):
    links = []
    contentDiv = self.fetchPage()

    if contentDiv is not None:
      if contentDiv:
        anchors = contentDiv.find_all('a')
        for anchor in anchors:
          href = anchor.get('href')
          anchorText = anchor.string
          if href:
            parsedUrl = urlparse(href)
            currentDomain = urlparse(self.url).netloc
            if linkType == 'internal' and (href.startswith('/') or parsedUrl.netloc == currentDomain):
              links.append((anchorText, href))
            elif linkType == 'external' and parsedUrl.netloc and parsedUrl.netloc != currentDomain:
              links.append((anchorText, href))
    return links

  def countWords(self):
    div = self.fetchPage()
    if div is not None:
      text = div.stripped_strings
      words = ' '.join(text).split()
      return len(words)

    return 0

  @staticmethod
  def getPage(url, args):
    return PageManager(url, args)
