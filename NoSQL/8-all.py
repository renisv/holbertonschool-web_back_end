#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection."""
def list_all(mongo_collection):
    """List all documents in a MongoDB collection.
    Args:
        mongo_collection (pymongo.collection.Collection): pymongo collection object
    Returns:
        list: list of documents, empty list if none
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
