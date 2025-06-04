from django.core.cache import cache


def cache_fun(data_key, query, cache_time):  
    # data = cache.get(data_key)
    # if data:  return data 
     
    # data = query
    # cache.set(data_key, query, cache_time) 
    # return data 
    return cache.get_or_set(data_key, query, cache_time)
