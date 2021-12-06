import os
from dotenv import load_dotenv

load_dotenv()


def get_env(name: str, terminal_action: bool = True) -> str:
    if name in os.environ:
        return os.environ[name]
    if terminal_action:
        value = input(f'ENTER YOUR {name}: ')
        with open('.env', 'a') as env:
            env.write(f'{name}={value}\n')
        return value
    else:
        return name
