# Webpage Link Analyzer

## Overview

This script is designed to analyze a specific webpage and extract useful information such as :
- The number of words,
- The internal links,
- The external links.

It allows filtering based on CSS class and ID attributes.

## Requirements

- Python3

Make sure Python 3 is installed on your system. You can install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line, passing the URL of the webpage you want to analyze as an argument. You can also specify optional arguments for CSS class and ID to filter the content

### Command Line Arguments

- `url`: The URL of the webpage to analyze (required).
- `--cssClass`: The CSS class to filter the content (optional).
- `--id`: The ID to filter the content (optional).

### Exemple

```bash
python main.py https://www.example.com --id content
```

This command analyzes the webpage at https://www.example.com, included into the div with id 'content'.

### Output
The script outputs the following information:

- Number of words on the page.
- List of internal links (links to the same domain).
- List of external links (links to different domains).
- Each link is presented with its anchor text and URL.

##  Customization
You can customize the script by modifying the source code to suit specific requirements, such as adding more filtering options or extracting different types of data from the webpage.

**Note: This script is for educational and analytical purposes. Ensure you have permission to scrape the website and respect the website's terms of service and robots.txt file.**