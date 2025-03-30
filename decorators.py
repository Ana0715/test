# 1
from datetime import datetime
import requests

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f'Function completed in {execution_time.seconds}s {milliseconds}ms')
        return result
    return wrapper


@measure_execution_time
def get_response(text):
    response = requests.get(text)
    if response.status_code == 200:
        return f'Успешно! {response.headers['Date']}'
    else:
        return f'Ошибка {response.status_code}'


print(get_response("https://www.example.com"))





# 2
def requires_admin(func):
    def wrapper(*args, **kwargs):
        user = next((arg for arg in args if isinstance(arg, dict) and 'role' in arg), None)
        if user and user.get('role') == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError('Неверный пользователь')

    return wrapper


@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}."


admin_user = {
    'username': 'Alice',
    'role': 'admin'
    }

regular_user = {
    'username': 'Bob',
    'role': 'user'
    }


print(delete_user(admin_user, 'Charlie'))
print(delete_user(regular_user, 'Charlie'))