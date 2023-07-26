from abc import ABC, abstractmethod


class ViewsStorageBackend(ABC):
    @abstractmethod
    def increment(self, key: str):
        ...

    @abstractmethod
    def most_common(self, n: int) -> dict[str, int]:
        ...
