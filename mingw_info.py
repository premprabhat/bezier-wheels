import pathlib


def describe(directory):
    as_path = pathlib.Path(directory)
    print(as_path)
    print("-" * 60)
    for contained in as_path.glob("*"):
        if contained.is_dir():
            print(f"{contained!r} (directory)")
        else:
            print(repr(contained))


def main():
    describe(r"C:\mingw-w64")
    print("*" * 60)
    describe(r"C:\MinGW")
    print("*" * 60)
    describe(r"C:\MinGW\bin")
    print("*" * 60)
    describe(r"C:\MinGW\mingw32")
    print("*" * 60)
    describe(r"C:\MinGW\mingw32\bin")


if __name__ == "__main__":
    main()
