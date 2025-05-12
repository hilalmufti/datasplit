# %%
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

LOGO = [
    r" ____   __  ____  __   ____  ____  __    __  ____ ",
    r"(    \ / _\(_  _)/ _\ / ___)(  _ \(  )  (  )(_  _)",
    r" ) D (/    \ )( /    \\___ \ ) __// (_/\ )(   )( ",
    r"(____/\_/\_/(__)\_/\_/(____/(__)  \____/(__) (__) "
]

# %%
def main() -> None:
    parser = ArgumentParser(prog='datasplit',
                            description='datasplit splits your data into train and test sets',
                            epilog="\n".join(LOGO),
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("-p", "--percent", type=float, default=0.9,
                        help="Percentage of data to use for training (default: 0.9)")
    args = parser.parse_args()

    percent = args.percent

    lines = sys.stdin.read().strip().split("\n")

    ix = int(percent*len(lines))
    train = lines[:ix]
    test = lines[ix:]

    for line in train:
        print("train", line)

    for line in test:
        print("test", line)

# TODO:
# - [ ] Add examples and extra description to CLI help
# - [ ] feat: randomize indices split
