from os_ import OS
from os_to_inception import os_to_inception


def os_to_str(os: OS) -> str:
    inception = os_to_inception[os]
    return f"{os.value}@{inception}"


if __name__ == '__main__':
    print(list(map(os_to_str,OS)))
