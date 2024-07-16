# FourCastNext Model for use with the EDIT Package

## Installation

Clone the repository, then run
```shell
pip install -e .
```

## Training

Once data has been cached to disk, training can be run with `fourcastnext/Training/train.py`. This contains a python script to run, and a dgxa100 compute job.

If you have changed the pipeline, ensure you update it in the script.

Additionally, you can change

- Save path
- Batch size
- Number of workers

## Predictions / Inference

If you have successfully run the training, you can now run some predictions with `edit.models`.

Again, if you have changed the pipeline, you will need to create the configs necessary for inference. 

Simply these configs are the original pipeline broken into data retrieval and then pipeline operations with the removal of caches.

### Setup

Set the config path

```shell
export EDIT_MODELS_CONFIGS=PATH_TO_CONFIGS:$EDIT_MODELS_CONFIGS
```

Set the dynamic import

```shell
export EDIT_MODELS_IMPORTS='fourcastnext'@PATH_TO_FOURCASTNEXT/src
```

Once those have been set you should be able to run

```shell
edit-models models
```

and `Development/FourCastNeXt` should be visible.

If so, you can now run some inference.

```shell
edit-models interactive --model Development/FourCastNeXt
```

When running the command, it will prompt for other kwargs (which fyi could be included in the initial command call),

Set `ckpt_path` to the full path of the checkpoint of the model you wish to load. It will then be copied to your asset folder and loaded

#### Example

```shell
edit-models interactive --model Development/FourCastNeXt --ckpt_path PATH_TO_CHECKPOINT
```
