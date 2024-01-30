"""
Bureau of Meteorology Atmospheric Regional Projections for Australia (BARRA_V2)
"""

from __future__ import annotations
from pathlib import Path
from typing import Type

from edit.data import EDITDatetime, transform, DataNotFoundError
from edit.data.indexes import ArchiveIndex, decorators, VariableDefault
from edit.data.transform import Transform, TransformCollection
from edit.data.archive import register_archive

from edit_archive_NCI.utilities import check_project


BARRA_V2_DIR_STRUCTURE = "{nature}/{activity}/{domain}/{institution}/{driving_source}/{experiment}/{variant}/{source}/{version_realisation}/{frequency}/"

VARIABLE_DEFAULT = Type[VariableDefault]

@register_archive('BARRA_V2')
class BARRA_V2(ArchiveIndex):
    """Bureau of Meteorology Atmospheric high-resolution Regional Reanalysis for Australia, BARRA Version 2"""

    @property
    def _desc_(self):
        return {
            "singleline": "Bureau of Meteorology Atmospheric high-resolution Regional Reanalysis for Australia, BARRA Version 2",
            "Documentation": "https://dx.doi.org/10.25914/1x6g-2v48",
        }
    
    @decorators.alias_arguments(variables=["variable"])
    @decorators.check_arguments(struc="edit_archive_NCI.structure.BARRA_V2.struc")
    def __init__(
        self,
        variables: list[str] | str,
        frequency: str,
        *,
        nature: str | VARIABLE_DEFAULT = VariableDefault,
        activity: str | VARIABLE_DEFAULT = VariableDefault,
        domain: str | VARIABLE_DEFAULT = VariableDefault,
        institution: str | VARIABLE_DEFAULT = VariableDefault,
        driving_source: str | VARIABLE_DEFAULT = VariableDefault,
        experiment: str | VARIABLE_DEFAULT = VariableDefault,
        variant: str | VARIABLE_DEFAULT = VariableDefault,
        source: str | VARIABLE_DEFAULT = VariableDefault,
        version_realisation: str | VARIABLE_DEFAULT = VariableDefault,
        version: str | VARIABLE_DEFAULT = 'v20231001', # VariableDefault,
        transforms: Transform | TransformCollection = TransformCollection(),
    ):
        """
        Bureau of Meteorology Atmospheric high-resolution Regional Reanalysis for Australia (BARRA_V2)

        BARRA2 provides the Bureau's higher resolution regional atmospheric reanalysis 
        over Australia and surrounding regions, spanning 1979-present day time period. 
        When completed, it replaces the first version of BARRA (Su et al., 
        doi: 10.5194/gmd-14-4357-2021; 10.5194/gmd-12-2049-2019).

        All arguments with `VariableDefault` as default might not have to be given,
        If based upon on the structure only one option is available, that will be picked.
        Otherwise an error will be raised.

        Args:
            variables (list[str] | str): 
                Variables to retrieve. 
                Mostly based on https://docs.google.com/spreadsheets/d/1qUauozwXkq7r1g-L4ALMIkCNINIhhCPx/edit#gid=1672965248
            frequency (str): 
                Temporal Frequency. 1hr (1-hourly), 3hr, 6hr, day (daily), mon (monthly), fx
            transforms (Transform | TransformCollection, optional): 
                Transforms to apply to the data. Defaults to TransformCollection().

            nature (str | VARIABLE_DEFAULT, optional):
                'output'
            activity (str | VARIABLE_DEFAULT, optional):
                'reanalysis'
            domain (str | VARIABLE_DEFAULT, optional):
                Spatial domain and grid resolution of the data, namely AUS-11, AUS-22, AUS-04.
            institution (str | VARIABLE_DEFAULT, optional):
                'BOM', RCM-institution
            driving_source (str| VARIABLE_DEFAULT, optional): 
                'ERA5', global model that drives BARRA2 at the lateral boundary
            experiment (str | VARIABLE_DEFAULT, optional):
                'historical'
            variant (str | VARIABLE_DEFAULT, optional):
                labels the nature of ERA5 data used, either hres or eda
            source (str | VARIABLE_DEFAULT, optional):
                BARRA-R2, BARRA-RE2, or BARRA-C2
            version_realisation (str | VARIABLE_DEFAULT, optional):
                identifies the modelling version of BARRA2 (TBC on identifying data version)
            version (str | VARIABLE_DEFAULT, optional):                    
                Denotes the date of data generation or date of data release
        """        

        self.make_catalog()
        check_project(project_code='ob53')

        variables = [variables] if isinstance(variables, str) else variables
        self.dir = Path(BARRA_V2_DIR_STRUCTURE.format(**locals()))
        
        self.variables = variables
        self.version = str(version)


        super().__init__(transforms = transforms)

    def filesystem(
        self,
        querytime: str | EDITDatetime,
    ) -> Path | dict[str, str]:
        BARRA_V2_HOME = Path(self.ROOT_DIRECTORIES["BARRA_V2"])

        discovered_paths = {}

        querytime_month = EDITDatetime(querytime).at_resolution("month")

        for variable in self.variables:
            dir_path = BARRA_V2_HOME / self.dir / variable / self.version

            paths = list(dir_path.glob(f"*{querytime_month.strftime('%Y%m')}-{querytime_month.strftime('%Y%m')}.nc"))

            if len(paths) == 0:
                raise DataNotFoundError(f"Could not find data at {dir_path!r} at time {querytime!r}")
            discovered_paths[variable] = paths[0]
        return discovered_paths
