#!/usr/bin/env python3
"""Logs stats."""
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    nginx = db.nginx
    
    total_logs = nginx.count_documents({})
    print("{} logs".format(total_logs))
    
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print("    method {}: {}".format(method, count))
    
    status_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
