import argparse

parse = argparse.ArgumentParser()
# parse.add_argument("name")
# arg = parse.parse_args()

# print(f"Hello: {arg.name}")

parse.add_argument("--epochs", type=int, default=10)
parse.add_argument("-lr", "--learning_rate", type=float, default=0.001)
arg = parse.parse_args()
print(arg)