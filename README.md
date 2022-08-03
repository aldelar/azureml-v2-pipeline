# azureml-v2-pipeline

## project description

This is an Azure ML CLIv2 template project demonstrating a very simple pipeline with inputs/outputs connected to a datalake.

We here have a simple pipeline with 2 steps:
- data-engineering, grabs data from a raw_data.csv file (this needs to be setup in your Azure ML environment, in a storage account container (recommending DataLake Gen2)), and defined as a datastore in AML (datastore named 'datalake' here in this example)
- training: sources data from the output of the data-engineering step, would in real life train a model, then perform predictions, and save these predictions to an output folder in the datalake

![pipeline](doc/pipeline.png)

See:
```
outputs:
      predictions_data_folder:
        type: uri_folder
        mode: rw_mount
        path: azureml://datastores/datalake/paths/aml_v2_pj_prediction_data
```

## how to create and run the pipeline

[Install the Azure CLI + the Azure CLI 'ml' extension](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?tabs=public), then run the following to create the steps runtime environment (repeat this any time you need to modify the 'conda' files in each step folder to support code changes):

```
az ml environment create -f ./data-engineering/data-engineering-environment.yml
az ml environment create -f ./training/training-environment.yml
```
To trigger a pipeline creation/run, run the following (note the flag to turn on the parallel job private preview feature if it isn't in public preview when you run this):

```
az ml job create -f pipeline.yml --web
```