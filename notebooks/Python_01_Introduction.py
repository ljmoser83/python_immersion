#!/usr/bin/env python
# coding: utf-8

# # Python Immersion Course
# 
# ### An Introduction to Python
# 
# ### Joe Blankenship - Just some dude

# ## 5 Initial Sections
# 
# * Introduction to Python Programming Language - Part 1
# * Introduction to Python Programming Language - Part 2
# * Data Collection
# * Data Analysis
# * Data Visualization

# ## Learning Objectives
# 
# * Gain a working understanding of the Python programming language
# * Gain a working knowledge of how to collect and process data in Python
# * Gain a good understanding of how to perform data manipulation and analysis in Python
# * Gain a good understanding of how to visualize your analytic results using Python

# ## Meetings and Discussions
# 
# * Group dictates schedule
# * Notebooks are on GitHub ([here](https://github.com/bluegrass-devs/python_immersion))
# * Discussions on Slack
#   * [bluegrassdevs.org](https://www.bluegrassdevs.org/)
# * Email me (joe[at]cgrii.org)

# ## Introduction - Part 1
# 
# * Introduction
#   * What is Python?
#   * Why use it?
# * Setup
#   * Operating Systems
#   * Virtual Environments
#     * Python 3.X
#     * Anaconda
#   * IDEs
#     * Jupyter Lab/Notebooks
#     * Spyder
#     * PyCharm
#     * Text editors
#   * VCS
#     * GitHub
#     * GitLab
#     * BitBucket
# * Demo
#   * Hello World
#   * Virtual Environments
# * Install Python3 and pip3

# ## What is Python?
# 
# * "Interpreted high-level programming language" (Wikipedia)
#   * JIT
#   * Multiple interpreters
# * General-purpose programming
# * Created by Guido van Rossum (1991)
# * Named after Monty Python

# ## Why Python?
# 
# * Simple to Use!
# * Broad Spectrum of Application
# * Full Stack Solutions
# * Numerous 3rd Party Libraries
# * Active, Open Source Community

# ## Setup - Operating Systems
# 
# * Go here for your respective OS download
#   * https://www.python.org/
# * Windows
#   * load executable installer or ZIP
#   * Add to Path!
# * Mac OS
#   * Python for Mac OS
#   * For latest versions, have to download
# * Linux
#   * Just the best ;)
#   * Already have Python and Legacy Python installed

# ## Setup - Package Management
# 
# * PyPI
#   * [Python Package Index](https://pypi.python.org/pypi)
#   * pip3 package utility
#     * May need to install depending on OS
#   * Anyone can publish their packages here
# * Many other package managers
#   * Do your research
#     * Aptitude
#     * Homebrew
#     * Anaconda
#     * Enthought

# ## Setup - Virtual Environments
# 
# * Why?
#   * Maintain project environment
#   * Prevent clutter
#     * System packages – Python Standard library
#     * Site packages - 3rd party libraries
#   * Prevent package version issues
#   * Makes sharing your research/projects easier

# ## Setup - Virtual Environments
# 
# * Command
#   * I currently recommend using [pipenv](https://pipenv.readthedocs.io/en/latest/)
#   * Inside your project directory use pipenv
#     * `pip3 install pipenv`
#     * `pipenv shell`
#     * `pipenv install`

# ## Setup - Virtual Environments
# 
# * Python has a [default virtual environment tool](https://docs.python.org/3/library/venv.html)
# * To create your project directory with virtual environment
#   * `python3 -m venv /path/to/new/virtual/environment`
#   * `cd /path/to/new/virtual/environment`
#   * `source bin/activate`
# * To create a requirements.txt
#   * activate the virtual environment
#   * `pip3 freeze > requirements.txt`

# ## Setup - Virtual Environments
# 
# * Anaconda is a popular data science environment
#   * Package management/virtual environments are unique to their system
# * Enthought is another data science-focused environment
# * You can go one of these routes if you choose
#   * Keep in mind these are companies with partially proprietary setups

# ## Setup - IDEs
# 
# * Python comes with a REPL and Idle
# * You can use Integrated Development Environments (IDEs)
#   * Jupyter Lab
#     * Jupyter Notebooks
#     * iPython
#   * Spyder
#   * PyCharm
#   * Sublime
#   * Atom
#   * Visual Studio Code
#   * Notepad++ (Windows)
#   * Any text editor really...

# ## Version Control Software
# 
# ** Always back-up your projects with a VCS **
# 
# #### Git is an industry standard version control system
# 
# * Github
#   * Go [here](https://guides.github.com/) to get started
# * GitLab
#   * Go [here](https://docs.gitlab.com/ee/README.html#getting-started-with-gitlab) to get started
# * BitBucket
#   * Go [here](https://www.atlassian.com/git/tutorials) to get started
# 
# #### There are several others you can use

# ## Demos!

# In[1]:


# Python Easter Egg!
import antigravity


# In[ ]:


# Another Python Easter Egg!
import this


# In[2]:


# A simple app to open multiple search tabs on a browser for same query

# from core Python3, import open_new_tab module from webbrowser library
from webbrowser import open_new_tab

# Define list of search engine URLs
websites = [
    "https://www.google.com/search?q=",
    "https://duckduckgo.com/?q=",
    "https://search.yahoo.com/search?p=",
    "https://www.bing.com/search?q=",
    "https://www.ask.com/web?q=",
    "https://www.startpage.com/do/dsearch?query="
]

# Define the search query
query = 'dogs' # what do we need here?

# For each URL in the list
# open a new tab and populate the URL with the search engine and query 
for i in websites:
    open_new_tab(i + query)  # what should we give our function here?


# In[3]:


# An app with a function which opens multiple search tabs on a browser for same query

# from core Python3, import open_new_tab module from webbrowser library
from webbrowser import open_new_tab

# Define a reusable function named 'search' that takes arguments for a search phrase and engines
def search(search_phrase, search_engines):
    # For each URL in the list
    for i in search_engines:
        # open a new tab and populate the URL with the search engine and query 
        open_new_tab(i + search_phrase)  # does this do what we want?


# In[4]:


websitez= [
    "https://www.google.com/search?q=",
    "https://duckduckgo.com/?q=",
    "https://search.yahoo.com/search?p=",
    "https://www.bing.com/search?q=",
    "https://www.ask.com/web?q=",
    "https://www.startpage.com/do/dsearch?query="
]
lookup = 'dogs'
# use our search function for our query
# place your code below
search(lookup, websitez)


# ## Resources
# 
# * Public/Univeristy Libraries
#   * Books, E-books, and online education resources
# * [Pycoder's Weekly](http://pycoders.com/)
# * [KDNuggets](https://www.kdnuggets.com/news/index.html)
# * [Data Science Weekly](https://www.datascienceweekly.org/newsletters/data-science-weekly-newsletter-issue-217)
# * [DataCamp](https://www.datacamp.com/)
# * [Codecademy](https://www.codecademy.com/)
# * [Python Packages](https://packaging.python.org/tutorials/installing-packages/)
# * [Real Python](https://realpython.com/)
# * [Full Stack Python](https://www.fullstackpython.com/)
# * [PyCon talks](http://pyvideo.org/)
# * [Dan Bader’s stuff](https://dbader.org/)
