class CachedGenerations:
    cache_capacity = 1000
    latest = None
    general_cache = {}

    @classmethod
    def store_latest(cls, population):
        cls.latest = population

    @classmethod
    def store_generation(cls, population):
        pass

    @classmethod
    def retrieve_generation(cls, generation_number):
        pass