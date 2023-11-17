# INU

Inu is a command line interface

## Overview

This CLI is designed to provide SEO Feedbacks using simple terminal commands :
- The number of words,
- The internal links,
- The external links.

It allows filtering based on CSS class and ID attributes.


## Prerequisites

Before you install Inu, make sure you have the following prerequisites installed:

- Python 3
- Git
- Pip (Python package installer)

## Installation

You can install Inueither by using pip.

1. Clone the repository:

```bash
git clone https://github.com/your-username/inu.git inu
# Navigate to the cloned directory:
cd inu
```

2. Run the following command to install the CLI :

```bash
pip install .
```

## Usage

After installation, you can use the inu command to interact with the SEO tools.
Here are some examples:

```bash
# Display help information
inu --help

# Analyse the provided page to get fast insights (number of words, internal & external links with anchors)
inu analyze http://example.com --css-class=someClass --id=someId

# Get a volume estimation for a specific keyword with the provided locale restrictions (or not).
inu kw_volume "keyword" --locale=en
```

Replace http://example.com, someClass, someId, and "keyword" with the actual values you wish to use.

## Support

For support, issues, or contributions, please visit the GitHub repository.