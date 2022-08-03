import argparse,json,os
import pandas as pd

# data engineering
def prepare_training_data(args):
    # read source data
    raw_df = pd.read_csv(args.raw_data_file)
    # do data engineering here... and save to output folder (typically here you would output as parquet and partitioned for speed depending on the use cases)
    raw_df.to_csv(os.path.join(args.training_data_folder, "training_data.csv"), index=False)

# read arguments
def parse_args():
    # retrieve output location
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_data_file', type=str)
    parser.add_argument('--training_data_folder', type=str)
    args, unknown_args = parser.parse_known_args()
    print(f"raw_data_file: {args.raw_data_file}")
    print(f"training_data_folder: {args.training_data_folder}")
    return args

# main
if __name__ == "__main__":
    args = parse_args()
    prepare_training_data(args)