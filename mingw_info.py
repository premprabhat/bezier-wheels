import pathlib


def main():
    mingw_w64 = pathlib.Path(r"C:\mingw-w64")
    print(mingw_w64)

    print("-" * 60)
    for contained in mingw_w64.glob("*"):
        print(repr(contained))


if __name__ == "__main__":
    main()
