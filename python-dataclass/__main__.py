from typing import Protocol
from kb import OSES


# Too specific
# def os_to_str(os: OS) -> str:
#     return f"{os.name}@{os.inception}"


class NameInception(Protocol):
    @property
    def name(self) -> str: ...
    
    @property
    def inception(self) -> int: ...


def name_inception_to_str(name_inception: NameInception) -> str:
    return f"{name_inception.name}@{name_inception.inception}"


if __name__ == '__main__':
    print(list(map(name_inception_to_str, OSES)))
