from collections import deque

class CachedGenerations:
    seed_generation = None
    latest_generation = None
    general_cache = {}

    cache_capacity = 1000

    @classmethod
    def store_seed(cls, population):
        cls.seed_generation = population
        cls.latest_generation = population

    @classmethod
    def store_latest(cls, population):
        cls.latest_generation = population
        cls.store_generation(population)

    @classmethod
    def store_generation(cls, population):
        if population.generation not in cls.general_cache:
            if len(cls.general_cache) >= cls.cache_capacity:
                del cls.general_cache[min(cls.general_cache.keys())]
                print("Tuhottiin cachesta", min(cls.general_cache.keys()))
            cls.general_cache[str(population.generation)] = population
        
    @classmethod
    def retrieve_generation(cls, generation_number):
        try:
            return cls.general_cache.get(str(generation_number))
        except:
            return None
        
    @classmethod
    def get_nearest_lesser_generation(cls, generation_number):
        keys = deque(cls.general_cache.keys())

        if len(keys) == 0:
            return None
        else:
            key = keys.pop()
            while(key > generation_number and len(keys) > 0):
                key = keys.pop()
                
            return cls.general_cache[key]