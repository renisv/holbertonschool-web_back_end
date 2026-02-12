#!/usr/bin/env python3
<<<<<<< HEAD
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
=======
"""9-insert_school.py"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key/value pairs representing document fields

    Returns:
        The _id of the inserted document
    """
    if mongo_collection is None or not kwargs:
        return None

>>>>>>> upstream/main
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
