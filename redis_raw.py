import redis

redis_connection = redis.Redis(host='localhost', port='6379', db=0)

# Key Value
redis_connection.set('chave_1', 'Hello_World_From_Python')
chave_1 = redis_connection.get('chave_1').decode('utf-8')
redis_connection.delete('chave_1')


# Hash
redis_connection.hset('User', 'name', 'Ana')
redis_connection.hset('User', 'country', 'Cabo Verde')
redis_connection.hset('User', 'field', 'Software Engineer')
User = redis_connection.hscan('User')
name = redis_connection.hget('User', 'name').decode('utf-8')
redis_connection.hdel('User', 'field')


# exist
exist_key = redis_connection.exists('chave_1')
exist_hash = redis_connection.exists('User')
exist_hash_key = redis_connection.exists('User', 'field')

print(exist_key)
print(exist_hash)
print(exist_hash_key)
