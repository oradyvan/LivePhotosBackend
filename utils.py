"""
This module contains helper functions
"""

# System modules
from datetime import datetime
import hashlib, base64

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%dT%H:%M:%S"))

def calculate_file_hash(file_storage):
	BLOCK_SIZE = 65536
	hasher = hashlib.md5()
	buffer = file_storage.read(BLOCK_SIZE)
	while len(buffer) > 0:
		hasher.update(buffer)
		buffer = file_storage.read(BLOCK_SIZE)
    # Calculate Hash Value according to the algorithm as described in
    # https://docs.google.com/document/d/1vgjl_n6gpC4nHcHcjDLqI39CXl5NlPIDlknESW6W2YU/edit#heading=h.pd228uq40hwp
	first_conversion = base64.standard_b64encode(hasher.digest())
	hash_value = base64.standard_b64encode(first_conversion).decode("utf-8")
	return hash_value

def make_asset_identifier(hash_value):
	return "Storage::Photos::Asset::%s" % hash_value
