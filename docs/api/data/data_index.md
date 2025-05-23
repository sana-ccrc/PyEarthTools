# Data API Index

This is the data package which forms a part of the [PyEarthTools package](https://github.com/ACCESS-Community-Hub/PyEarthTools). It contains code for fetching, loading, transforming and working with a wide variety of data sources. It has support for industry standard data sources of common interest, and also has code to aid users in managing their own data in their own projects.

Many research facilities have pre-existing data holdings on disk, and it is not necessary for users to fetch data. On the other hand, many users do need to fetch their own data for their projects. Both situations are catered for, but it's important to bear in mind that this package is catering to a broad and diverse set of user requirements.

The use of the data package within PyEarthTools includes:
  - Fetching known data sources (such as ERA5 or ISD)
  - Indexing into either pre-existing or newly-fetched data that has been downloaded
  - Subsetting and reprocessing that data for efficient storage, access and reprocessing
  - Loading that data into memory for efficient use in machine learning
  - Performing scientific operations on that data as part of data pre-processing

These tasks are aided by the API presented by the data package. Users looking for "how-to guides" or worked examples should review the [Tutorial Gallery](https://pyearthtools.readthedocs.io/en/latest/notebooks/Gallery.html).

The rest of this page contains reference information for the components of the Data package. The entire data API docs can be viewed at [Data API Docs](data_api.md)

|  Module          |               Purpose                         |   API Docs    |
|------------------|-----------------------------------------------|---------------------|
|  `data.archive`  | Indexing and loading from known data holdings | - [ZarrIndex](data_api.md#pyearthtools.data.archive.ZarrIndex)     |
|                  |                                               | - [ZarrTimeIndex](data_api.md#pyearthtools.data.archive.ZarrTimeIndex) |
|                  |                                               | - [extensions.register_archive](data_api.md#pyearthtools.data.archive.extensions.register_archive) |
|                  |                                               | - [reset_root](data_api.md#pyearthtools.data.archive.reset_root) |
|                  |                                               | - [reset_root](data_api.md#pyearthtools.data.archive.set_root) |
|                  |                                               | - [reset_root](data_api.md#pyearthtools.data.archive.config_root) |
| `data.derived`   |   Calculated derived fields                   | - [DerivedValue](data_api.md#pyearthtools.data.derived.DerivedValue) |
|                  |                                               | - [TimeDerivedValue](data_api.md#pyearthtools.data.derived.TimeDerivedValue) |
|                  |                                               | - [AdvancedTimeDerivedValue](data_api.md#pyearthtools.data.derived.AdvancedTimeDerivedValue) |
|                  |                                               | - [Insolation](data_api.md#pyearthtools.data.derived.Insolation) |
| `data.indexes`   |                                               | - [Index](data_api.md#pyearthtools.data.indexes.Index) |
|                  |                                               | - [DataIndex](data_api.md#pyearthtools.data.indexes.DataIndex) |
|                  |                                               | - [FileSystemIndex](data_api.md#pyearthtools.data.indexes.FileSystemIndex) |
|                  |                                               | - [TimeIndex](data_api.md#pyearthtools.data.indexes.TimeIndex) |
|                  |                                               | - [TimeDataIndex](data_api.md#pyearthtools.data.indexes.TimeDataIndex) |
|                  |                                               | - [AdvancedTimeIndex](data_api.md#pyearthtools.data.indexes.AdvancedTimeIndex) |
|                  |                                               | - [AdvancedTimeDataIndex](data_api.md#pyearthtools.data.indexes.AdvancedTimeDataIndex) |
|                  |                                               | - [BaseTimeIndex](data_api.md#pyearthtools.data.indexes.BaseTimeIndex) |
|                  |                                               | - [DataFileSystemIndex](data_api.md#pyearthtools.data.indexes.DataFileSystemIndex) |
|                  |                                               | - [ArchiveIndex](data_api.md#pyearthtools.data.indexes.ArchiveIndex) |
|                  |                                               | - [ForecastIndex](data_api.md#pyearthtools.data.indexes.ForecastIndex) |
|                  |                                               | - [StaticDataIndex](data_api.md#pyearthtools.data.indexes.StaticDataIndex) |
|                  |                                               | - [CachingForecastIndex](data_api.md#pyearthtools.data.indexes.CachingForecastIndex) |
|                  |                                               | - [IntakeIndex](data_api.md#pyearthtools.data.indexes.IntakeIndex) |
|                  |                                               | - [IntakeIndexCache](data_api.md#pyearthtools.data.indexes.IntakeIndexCache) |
|                  |                                               | - [cacheIndex.BaseCacheIndex](data_api.md#pyearthtools.data.indexes.cacheIndex.BaseCacheIndex) |
|                  |                                               | - [cacheIndex.FileSystemCacheIndex](data_api.md#pyearthtools.data.indexes.cacheIndex.FileSystemCacheIndex) |
|                  |                                               | - [cacheIndex.CacheFactory](data_api.md#pyearthtools.data.indexes.cacheIndex.CacheFactory) |
|                  |                                               | - [cacheIndex.FunctionalCache](data_api.md#pyearthtools.data.indexes.cacheIndex.FunctionalCache) |
|                  |                                               | - [combine.InterpolationIndex](data_api.md#pyearthtools.data.indexes.combine.InterpolationIndex) |
|                  |                                               | - [fake.FakeIndex](data_api.md#pyearthtools.data.indexes.fake.FakeIndex) |
|                  |                                               | - [extensions.register_accessor](data_api.md#pyearthtools.data.indexes.extensions.register_accessor) |
| `data.modifications`   |                                         | - [Modification](data_api.md#pyearthtools.data.modifications.Modification) |
|                  |                                               | - [register_modification](data_api.md#pyearthtools.data.modifications.register_modification) |
|                  |                                               | - [variable_modifications](data_api.md#pyearthtools.data.modifications.variable_modifications) |
|                  |                                               | - [aggregations.Aggregation](data_api.md#pyearthtools.data.modifications.aggregations.Aggregation) |
|                  |                                               | - [aggregations.AggregationGeneral](data_api.md#pyearthtools.data.modifications.aggregations.AggregationGeneral) |
|                  |                                               | - [aggregations.Mean](data_api.md#pyearthtools.data.modifications.aggregations.Mean) |
|                  |                                               | - [aggregations.Accumulate](data_api.md#pyearthtools.data.modifications.aggregations.Accumulate) |
|                  |                                               | - [constants.Constant](data_api.md#pyearthtools.data.modifications.constants.Constant) |
|                  |                                               | - [decorator.VariableModification](data_api.md#pyearthtools.data.modifications.decorator.VariableModification) |
|                  |                                               | - [decorator.Modifier](data_api.md#pyearthtools.data.modifications.decorator.Modifier) |
|                  |                                               | - [reductions.Reduction](data_api.md#pyearthtools.data.modifications.reductions.Reduction) |
|                  |                                               | - [reductions.Groupby](data_api.md#pyearthtools.data.modifications.reductions.Groupby) |
|                  |                                               | - [reductions.Hourly](data_api.md#pyearthtools.data.modifications.reductions.Hourly) |
|                  |                                               | - [reductions.Daily](data_api.md#pyearthtools.data.modifications.reductions.Daily) |
|                  |                                               | - [reductions.Monthly](data_api.md#pyearthtools.data.modifications.reductions.Monthly) |
|                  |                                               | - [register.register_modification](data_api.md#pyearthtools.data.modifications.register.register_modification) |
| `data.operations`  |                                             | - [percentile](data_api.md#pyearthtools.data.operations.percentile) |
|                  |                                               | - [aggregation](data_api.md#pyearthtools.data.operations.aggregation) |
|                  |                                               | - [binning](data_api.md#pyearthtools.data.operations.binning) |
|                  |                                               | - [SpatialInterpolation](data_api.md#pyearthtools.data.operations.SpatialInterpolation) |
|                  |                                               | - [TemporalInterpolation](data_api.md#pyearthtools.data.operations.TemporalInterpolation) |
|                  |                                               | - [FullInterpolation](data_api.md#pyearthtools.data.operations.FullInterpolation) |
|                  |                                               | - [index_routines.series](data_api.md#pyearthtools.data.operations.index_routines.series) |
|                  |                                               | - [index_routines.safe_series](data_api.md#pyearthtools.data.operations.index_routines.safe_series) |
|                  |                                               | - [index_operations.split_ds](data_api.md#pyearthtools.data.operations.index_operations.split_ds) |
|                  |                                               | - [index_operations.split_ds_gen](data_api.md#pyearthtools.data.operations.index_operations.split_ds_gen) |
|                  |                                               | - [index_operations.aggregation](data_api.md#pyearthtools.data.operations.index_operations.aggregation) |
|                  |                                               | - [index_operations.find_range](data_api.md#pyearthtools.data.operations.index_operations.find_range) |
|                  |                                               | - [utils.identify_time_dimension](data_api.md#pyearthtools.data.operations.utils.identify_time_dimension) |
|                  |                                               | - [forecast_op.forecast_series](data_api.md#pyearthtools.data.operations.forecast_op.forecast_series) |
|                  |                                               | - [forecast_op.forecast_as_basetime](data_api.md#pyearthtools.data.operations.forecast_op.forecast_as_basetime) |
|                  |                                               | - [forecast_op.forecast_select_time](data_api.md#pyearthtools.data.operations.forecast_op.forecast_select_time) |
