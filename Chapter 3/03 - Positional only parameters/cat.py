def concatenate(first: str, second: str, delim: str):
    return delim.join([first, second])


if __name__ == "__main__":
    concatenate("John", "Doe", " ")
    concatenate(first="John", second="Doe", delim=" ")
    concatenate("John", "Doe", delim=" ")
