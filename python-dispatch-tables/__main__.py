from os_ import OS
from os_to_inception import OS_TO_INCEPTION


def os_to_str(os: OS) -> str:
    inception = OS_TO_INCEPTION[os]
    return f"{os.value}@{inception}"


if __name__ == '__main__':
    print(list(map(os_to_str,OS)))
