import argparse

try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    line_count(infile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")
    parser.add_argument('infile')
    args = parser .parse_args()
    if args.infile:
        main(args.infile)
   