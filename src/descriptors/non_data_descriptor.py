class NonDataDescriptor:
    """Non-data descriptor: читает данные, но ничего не записывает"""
    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Просто возвращает отформатированную строку
        return f"Задача с очень крутым айди: {instance.id} и очень крутым описанием {instance.description}"
