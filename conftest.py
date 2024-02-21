import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def driver(request):
    options = Options()