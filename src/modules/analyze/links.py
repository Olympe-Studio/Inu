from colors import RED, GREEN, YELLOW, BLUE, ENDC
from src.PageManager import PageManager

def analyze_links(url, css_class=None, element_id=None):
    page = PageManager.get_page(url, {
      "cssClass": css_class,
      "id": element_id
    })
    words = page.count_words()
    internal_links = page.get_links("internal")
    external_links = page.get_links("external")

    print(" ")
    print(f"{YELLOW}|> NUMBER OF WORDS : {words} {ENDC}")
    print(" ")

    print(f"{BLUE}------------------------")
    print("  INTERNAL LINKS")
    print(f"------------------------{ENDC}")

    for anchor_text, link in internal_links:
        print(f"{GREEN}{anchor_text}{ENDC} : {link}")

    print(f"{RED}------------------------")
    print("  EXTERNAL LINKS")
    print(f"------------------------{ENDC}")

    for anchor_text, link in external_links:
        print(f"{GREEN}{anchor_text}{ENDC} : {link}")
