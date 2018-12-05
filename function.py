import random

def mix_array(array):
    result = []
    result = array[:]
    result = random.sample(array[:], len(result))
    return result
