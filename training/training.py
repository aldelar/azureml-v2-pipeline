import argparse,json,os
import pandas as pd

# data engineering
def training(args):
    # read source data
    training_data_df = pd.read_csv(os.path.join(args.training_data_folder, "training_data.csv"))
    # do model training here, and then perform predictions and save results to datalake
    # fake predictions here, we just output the training data to the predictions folder to showcase how pipelines work
    training_data_df.to_csv(os.path.join(args.predictions_data_folder, "predictions_data.csv"), index=False)

# read arguments
def parse_args():
    # retrieve output location
    parser = argparse.ArgumentParser()
    parser.add_argument('--training_data_folder', type=str)
    parser.add_argument('--predictions_data_folder', type=str)
    args, unknown_args = parser.parse_known_args()
    print(f"training_data_folder: {args.training_data_folder}")
    print(f"predictions_data_folder: {args.predictions_data_folder}")
    return args

# main
if __name__ == "__main__":
    args = parse_args()
    training(args)