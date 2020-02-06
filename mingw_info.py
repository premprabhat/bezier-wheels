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
    # describe(r"C:\msys64")
    # print("*" * 60)
    # describe(r"C:\msys64\mingw32")
    # print("*" * 60)
    describe(r"C:\msys64\mingw32\bin")
    print("*" * 60)
    # describe(r"C:\msys64\mingw64")
    # print("*" * 60)
    describe(r"C:\msys64\mingw64\bin")
    print("*" * 60)
    describe(r"C:\mingw-w64")
    print("*" * 60)
    describe(r"C:\MinGW")
    print("*" * 60)
    describe(r"C:\MinGW\bin")
    print("*" * 60)
    # describe(r"C:\MinGW\msys")
    # print("*" * 60)
    # describe(r"C:\MinGW\msys\1.0")
    # print("*" * 60)
    describe(r"C:\MinGW\msys\1.0\bin")
    print("*" * 60)
    # describe(r"C:\MinGW\mingw32")
    # print("*" * 60)
    describe(r"C:\MinGW\mingw32\bin")


if __name__ == "__main__":
    main()
