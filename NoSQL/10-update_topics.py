#!/usr/bin/env python3
<<<<<<< HEAD
"""Update the topics of a school document based its name."""
def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document based its name.
    Args:
        mongo_collection (pymongo.collection.Collection): pymongo collection object
=======
"""10-update_topics.py"""

def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on its name.

    Args:
        mongo_collection: pymongo collection object
>>>>>>> upstream/main
        name (str): the school name to update
        topics (list of str): list of topics to set
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return
<<<<<<< HEAD
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
=======

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
>>>>>>> upstream/main
