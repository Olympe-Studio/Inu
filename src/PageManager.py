from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


class PageManager:
    """
    A class to manage webpage fetching and parsing.
    It maintains instances based on URLs to avoid duplicate processing.
    """
    _instances = {}

    def __new__(cls, url, args):
        """
        Ensures a single instance per URL.
        """
        if url not in cls._instances:
            cls._instances[url] = super(PageManager, cls).__new__(cls)
        return cls._instances[url]

    def __init__(self, url, args):
        """
        Initializes the PageManager instance with a URL and arguments.
        """
        if hasattr(self, "initialized"):
            return

        self.initialized = True
        self.url = url
        self.args = args
        self.page = None

    def fetch_page(self):
        """
        Fetches the webpage content. If already fetched, returns the cached page.
        """
        if self.page is not None:
            return self.page

        self.set_page()
        return self.page

    def set_page(self):
        """
        Fetches the webpage from the internet and sets the page content.
        """
        try:
            response = requests.get(self.url, timeout=10)  # Timeout in seconds
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                config = {}

                if self.args.get('cssClass') is not None:
                    content_div = soup.select_one("." + self.args.get('cssClass'))

                if self.args.get('id') is not None:
                    content_div = soup.select_one("#" + self.args.get('id'))

                if content_div is None:
                    return

                self.page = content_div
        except requests.Timeout:
            print("Request timed out")
            self.page = None
        except requests.RequestException as e:
            print(f"Error fetching the page: {e}")
            self.page = None


    def get_links(self, link_type):
        """
        Extracts and returns links from the page based on the specified link type
        (internal / external).

        Args:
            - link_type  str  The type of link, either internal or external.
        """
        links = []
        content_div = self.fetch_page()

        if content_div is not None:
            if content_div:
                anchors = content_div.find_all("a")
                for anchor in anchors:
                    href = anchor.get("href")
                    anchor_text = anchor.string
                    if href:
                        parsed_url = urlparse(href)
                        current_domain = urlparse(self.url).netloc
                        if link_type == "internal" and (
                            href.startswith("/") or parsed_url.netloc == current_domain
                        ):
                            links.append((anchor_text, href))
                        elif (
                            link_type == "external"
                            and parsed_url.netloc
                            and parsed_url.netloc != current_domain
                        ):
                            links.append((anchor_text, href))
        return links

    def count_words(self):
        """
        Counts and returns the number of words in the content of the fetched page.
        """
        div = self.fetch_page()
        if div is not None:
            text = div.stripped_strings
            words = " ".join(text).split()
            return len(words)

        return 0

    @staticmethod
    def get_page(url, args):
        """
        Static method to get or create a PageManager instance for a given URL and arguments.
        """
        return PageManager(url, args)
