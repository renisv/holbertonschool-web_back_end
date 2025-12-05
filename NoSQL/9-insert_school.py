#!/usr/bin/env python3
"""Insert a new document into a MongoDB collection."""
def insert_school(mongo_collection, **kwargs):
    """Insert a new document into a MongoDB collection.
    Args:
        mongo_collection (pymongo.collection.Collection): pymongo collection object
        **kwargs: key=value pairs representing document fields
    Returns:
        _id of the inserted document
    """
    if mongo_collection is None or len(kwargs) == 0:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
