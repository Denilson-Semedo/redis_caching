from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository


redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)

redis_repository.insert("Hello!", "World!")
value = redis_repository.get("Hello!")

redis_repository.insert_hash('User', 'name', 'john')
redis_repository.insert_hash('User', 'age', 21)

name = redis_repository.get_hash('User', 'name')
age = redis_repository.get_hash('User', 'age')

print(value)
print(name)
print(age)

