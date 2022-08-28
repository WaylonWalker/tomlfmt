import argparse

import toml


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--infile", type=argparse.FileType("r", encoding="UTF-8"), required=True
    )
    args = parser.parse_args()
    content = toml.loads(args.infile.read())
    formatted = toml.dumps(content).replace("[ ", "[\n ").replace(",", ",\n")
    args.infile.close()
    with open(args.infile.name, "w") as f:
        f.write(formatted)


if __name__ == "__main__":
    cli()
