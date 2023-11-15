import argparse
from src.PageManager import PageManager

# ANSI color codes
GREEN = '\033[92m'
ENDC = '\033[0m'


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Get internal and external links from a webpage.')
  parser.add_argument('url', type=str, help='The URL of the webpage to analyze.')
  parser.add_argument('--cssClass', type=str, help='The class to find in', required=False)
  parser.add_argument('--id', type=str, help='The id to find in', required=False)
  args = parser.parse_args()
  url = args.url
  print(args.cssClass)


  page = PageManager.getPage(url, args)
  words = page.countWords()
  internalLinks = page.getLinks('internal')
  externalLinks = page.getLinks('external')
  print(" ")
  print(f"\033[93m NUMBER OF WORDS : {words} \033[0m")
  print(" ")

  print("\033[94m------------------------")
  print("  INTERNAL LINKS")
  print("------------------------\033[0m")
  print(" ")
  for anchorText, link in internalLinks:
    print(f"{GREEN}{anchorText}{ENDC} : {link}")
  print("\033[91m------------------------")
  print("  EXTERNAL LINKS")
  print("------------------------\033[0m")
  print(" ")

  for anchorText, link in externalLinks:
    print(f"{GREEN}{anchorText}{ENDC} : {link}")