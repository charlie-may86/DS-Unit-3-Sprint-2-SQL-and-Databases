import os
import json
import pymongo
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from pdb import set_trace as breakpoint

load_dotenv()

MONGODB_USER = os.getenv("MONGODB_USER", default = 'oops')
MONGODB_PASS = os.getenv("MONGODB_PASS", default = 'oops')
MONGODB_CLUSTER = os.getenv("MONGODB_CLUSTER", default = 'oops')


uri = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_CLUSTER}?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
print('URI: ', uri)

breakpoint()

