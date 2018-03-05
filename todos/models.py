from django.db import models
import requests
from bs4 import BeautifulSoup
import os
import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy


class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)
    def __str__(self):
        return self.item_text


class Market(models.Model):
    def __str__(self):
        return self.form_text