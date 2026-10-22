"""Tiny sample app used to verify GitHub Actions."""


def greet(name: str = "GitHub Actions") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
