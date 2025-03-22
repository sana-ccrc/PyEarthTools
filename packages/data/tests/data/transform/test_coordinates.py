from pyearthtools.data.transforms import coordinates
import xarray as xr
import numpy as np
import pytest


# Test data, re-used across tests
lon180 = list(range(-180, 180))
lon360 = list(range(0, 360))
lon_unclear = list(range(10, 120))
data = list(range(-180, 180))
data_unclear = list(range(10, 120))
da180 = xr.DataArray(coords={"longitude": lon180}, dims=["longitude"])
da360 = xr.DataArray(coords={"longitude": lon360}, dims=["longitude"])
da_wrongname = xr.DataArray(coords={"longname": lon180}, dims=["longname"])
da_unclear = xr.DataArray(coords={"longitude": lon_unclear}, dims=["longitude"])

def test_get_longitude():

    longitude_type = coordinates.get_longitude(da180, transform=False)
    assert longitude_type == "-180-180"
    transform = coordinates.get_longitude(da180, transform=True)
    assert transform._type == "-180-180"

    longitude_type = coordinates.get_longitude(da360, transform=False)
    assert longitude_type == "0-360"
    transform = coordinates.get_longitude(da360, transform=True)
    assert transform._type == "0-360"

    with pytest.raises(ValueError):
        longitude_type = coordinates.get_longitude(da_wrongname, transform=False)
        assert longitude_type == "-180-180"

    with pytest.raises(ValueError):
        result = coordinates.get_longitude(da_unclear, transform=False)

def test_StandardLongitude():

	conform = coordinates.StandardLongitude("0-360")
	fixed = conform.apply(da180)
	assert fixed is not None
	unchanged = conform.apply(da360)
	# TODO - shouldn't this be true?
	# assert xr.testing.assert_equal(fixed, da360)

	conform = coordinates.StandardLongitude("-180-180")
	fixed = conform.apply(da360)
	unchanged = conform.apply(da180)
	assert fixed is not None	
	# TODO - shouldn't this be true?
	# assert xr.testing.assert_equal(fixed, da180)	

