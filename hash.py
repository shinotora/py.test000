import new

aMap = ['abc','efg']
key = 'osa','tky'

def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to
    an index for the aMap's buckets."""
    return hash(key) % len(aMap)
	
print aMap
