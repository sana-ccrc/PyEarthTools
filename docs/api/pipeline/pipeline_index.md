# Pipeline API Index

This is the Pipeline package which forms a part of the [PyEarthTools package](https://github.com/ACCESS-Community-Hub/PyEarthTools).

The rest of this page contains reference information for the components of the Pipeline package. The entire data API docs can be viewed at [Pipeline API Docs](pipeline_api.md).

|  Module              |       Purpose                        |   API Docs     |
|----------------------|--------------------------------------|----------------|
|  `pipeline`          |                                      | - [Sampler](pipeline_api.md#pyearthtools.pipeline.Sampler)  |
|                      |                                      | - [Iterator](pipeline_api.md#pyearthtools.pipeline.Iterator)  |
|                      |                                      | - [Pipeline](pipeline_api.md#pyearthtools.pipeline.Pipeline)  |
|                      |                                      | - [Operation](pipeline_api.md#pyearthtools.pipeline.Operation)  |
|                      |                                      | - [PipelineException](pipeline_api.md#pyearthtools.pipeline.PipelineException)  |
|                      |                                      | - [PipelineFilterException](pipeline_api.md#pyearthtools.pipeline.PipelineFilterException)  |
|                      |                                      | - [PipelineRuntimeError](pipeline_api.md#pyearthtools.pipeline.PipelineRuntimeError)  |
|                      |                                      | - [PipelineTypeError](pipeline_api.md#pyearthtools.pipeline.PipelineTypeError)  |
| `pipeline.branching` |                                      | - [PipelineBranchPoint](pipeline_api.md#pyearthtools.pipeline.branching.PipelineBranchPoint)  |
|                      |                                      | - [Unifier](pipeline_api.md#pyearthtools.pipeline.branching.Unifier)  |
|                      |                                      | - [Joiner](pipeline_api.md#pyearthtools.pipeline.branching.Joiner)  |
|                      |                                      | - [Spliter](pipeline_api.md#pyearthtools.pipeline.branching.Spliter)  |
| `pipeline.filters`   |                                      | - [Filter](pipeline_api.md#pyearthtools.pipeline.filters.Filter)  |
|                      |                                      | - [Filter](pipeline_api.md#pyearthtools.pipeline.filters.Filter)  |
|                      |                                      | - [Filter](pipeline_api.md#pyearthtools.pipeline.filters.Filter)  |
|                      |                                      | - [Filter](pipeline_api.md#pyearthtools.pipeline.filters.Filter)  |
| `pipeline.iterators` |                                      | - [Iterator](pipeline_api.md#pyearthtools.pipeline.iterators.Iterator)  |
|                      |                                      | - [Range](pipeline_api.md#pyearthtools.pipeline.iterators.Range)  |
|                      |                                      | - [Predefined](pipeline_api.md#pyearthtools.pipeline.iterators.Predefined)  |
|                      |                                      | - [File](pipeline_api.md#pyearthtools.pipeline.iterators.File)  |
|                      |                                      | - [DateRange](pipeline_api.md#pyearthtools.pipeline.iterators.DateRange)  |
|                      |                                      | - [DateRangeLimit](pipeline_api.md#pyearthtools.pipeline.iterators.DateRangeLimit)  |
|                      |                                      | - [Randomise](pipeline_api.md#pyearthtools.pipeline.iterators.Randomise)  |
|                      |                                      | - [SuperIterator](pipeline_api.md#pyearthtools.pipeline.iterators.SuperIterator)  |
|                      |                                      | - [IterateResults](pipeline_api.md#pyearthtools.pipeline.iterators.IterateResults)  |
| `pipeline.samplers`  |                                      | - [EmptyObject](pipeline_api.md#pyearthtools.pipeline.samplers.EmptyObject)  |
|                      |                                      | - [Sampler](pipeline_api.md#pyearthtools.pipeline.samplers.Sampler)  |
|                      |                                      | - [Default](pipeline_api.md#pyearthtools.pipeline.samplers.Default)  |
|                      |                                      | - [SuperSampler](pipeline_api.md#pyearthtools.pipeline.samplers.SuperSampler)  |
|                      |                                      | - [Random](pipeline_api.md#pyearthtools.pipeline.samplers.Random)  |
|                      |                                      | - [DropOut](pipeline_api.md#pyearthtools.pipeline.samplers.DropOut)  |
|                      |                                      | - [RandomDropOut](pipeline_api.md#pyearthtools.pipeline.samplers.RandomDropOut)  |
| `pipeline.operations.xarray`  |                             | - [Compute](pipeline_api.md#pyearthtools.pipeline.operations.xarray.Compute)  |
|                      |                                      | - [Merge](pipeline_api.md#pyearthtools.pipeline.operations.xarray.Merge)  |
|                      |                                      | - [Concatenate](pipeline_api.md#pyearthtools.pipeline.operations.xarray.Concatenate)  |
|                      |                                      | - [Sort](pipeline_api.md#pyearthtools.pipeline.operations.xarray.Sort)  |
|                      |                                      | - [Chunk](pipeline_api.md#pyearthtools.pipeline.operations.xarray.Chunk)  |
|                      |                                      | - [RecodeCalendar](pipeline_api.md#pyearthtools.pipeline.operations.xarray.RecodeCalendar)  |
|                      |                                      | - [AlignDates](pipeline_api.md#pyearthtools.pipeline.operations.xarray.AlignDates)  |
| `pipeline.operations.xarray.conversion`  |                  | - [ToNumpy](pipeline_api.md#pyearthtools.pipeline.operations.xarray.conversion.ToNumpy)  |
|                      |                                      | - [ToDask](pipeline_api.md#pyearthtools.pipeline.operations.xarray.conversion.ToDask)  |
| `pipeline.operations.xarray.filters`  |                     | - [XarrayFilter](pipeline_api.md#pyearthtools.pipeline.operations.xarray.filters.XarrayFilter)  |
|                      |                                      | - [DropAnyNan](pipeline_api.md#pyearthtools.pipeline.operations.xarray.filters.DropAnyNan)  |
|                      |                                      | - [DropAllNan](pipeline_api.md#pyearthtools.pipeline.operations.xarray.filters.DropAllNan)  |
|                      |                                      | - [DropValue](pipeline_api.md#pyearthtools.pipeline.operations.xarray.filters.DropValue)  |
|                      |                                      | - [Shape](pipeline_api.md#pyearthtools.pipeline.operations.xarray.filters.Shape)  |
| `pipeline.operations.xarray.reshape`  |                     | - [Dimensions](pipeline_api.md#pyearthtools.pipeline.operations.xarray.reshape.Dimensions)  |
|                      |                                      | - [CoordinateFlatten](pipeline_api.md#pyearthtools.pipeline.operations.xarray.reshape.CoordinateFlatten)  |
| `pipeline.operations.xarray.select`  |                      | - [SelectDataset](pipeline_api.md#pyearthtools.pipeline.operations.xarray.select.SelectDataset)  |
|                      |                                      | - [DropDataset](pipeline_api.md#pyearthtools.pipeline.operations.xarray.select.DropDataset)  |
|                      |                                      | - [DropDataset](pipeline_api.md#pyearthtools.pipeline.operations.xarray.select.DropDataset)  |
| `pipeline.operations.xarray.split`  |                       | - [OnVariables](pipeline_api.md#pyearthtools.pipeline.operations.xarray.split.OnVariables)  |
|                      |                                      | - [OnCoordinate](pipeline_api.md#pyearthtools.pipeline.operations.xarray.split.OnCoordinate)  |
| `pipeline.operations.xarray.values`  |                      | - [FillNan](pipeline_api.md#pyearthtools.pipeline.operations.xarray.values.FillNan)  |
|                      |                                      | - [MaskValue](pipeline_api.md#pyearthtools.pipeline.operations.xarray.values.MaskValue)  |
|                      |                                      | - [ForceNormalised](pipeline_api.md#pyearthtools.pipeline.operations.xarray.values.ForceNormalised)  |
|                      |                                      | - [Derive](pipeline_api.md#pyearthtools.pipeline.operations.xarray.values.Derive)  |
| `pipeline.operations.xarray.metadata`  |                    | - [Rename](pipeline_api.md#pyearthtools.pipeline.operations.xarray.metadata.Rename)  |
|                      |                                      | - [Encoding](pipeline_api.md#pyearthtools.pipeline.operations.xarray.metadata.Encoding)  |
|                      |                                      | - [MaintainEncoding](pipeline_api.md#pyearthtools.pipeline.operations.xarray.metadata.MaintainEncoding)  |
|                      |                                      | - [Attributes](pipeline_api.md#pyearthtools.pipeline.operations.xarray.metadata.Attributes)  |
|                      |                                      | - [MaintainAttributes](pipeline_api.md#pyearthtools.pipeline.operations.xarray.metadata.MaintainAttributes)  |
| `pipeline.operations.xarray.normalisation`  |               | - [xarrayNormalisation](pipeline_api.md#pyearthtools.pipeline.operations.xarray.normalisation.xarrayNormalisation)  |
|                      |                                      | - [Anomaly](pipeline_api.md#pyearthtools.pipeline.operations.xarray.normalisation.Anomaly)  |
|                      |                                      | - [Deviation](pipeline_api.md#pyearthtools.pipeline.operations.xarray.normalisation.Deviation)  |
|                      |                                      | - [Division](pipeline_api.md#pyearthtools.pipeline.operations.xarray.normalisation.Division)  |
|                      |                                      | - [Evaluated](pipeline_api.md#pyearthtools.pipeline.operations.xarray.normalisation.Evaluated)  |
| `pipeline.operations.xarray.remapping`  |                   | - [HEALPix](pipeline_api.md#pyearthtools.pipeline.operations.xarray.remapping.HEALPix)  |






