import numpy as np
import pytest
from pyearthtools.utils.data.tesselator._patching.reorder import setup_formats, reorder, move_to_end

# Test the setup_formats function.
def test_setup_formats():
    # Test with one fully defined format and one partially defined format.
    assert setup_formats('RPTCHW', 'RP...HW') == ('RPTCHW', 'RPTCHW')
    assert setup_formats('TCRPHW', 'RP...HW') == ('TCRPHW', 'RPTCHW')
    assert setup_formats('RP...HW', 'TCRPHW') == ('RPTCHW', 'TCRPHW')

    # Test with both formats fully defined.
    assert setup_formats('RPTCHW', 'RPTCHW') == ('RPTCHW', 'RPTCHW')
    assert setup_formats('TCRPHW', 'RPTCHW') == ('TCRPHW', 'RPTCHW')


    # Test with different combinations of characters in the formats.
    assert setup_formats('RP...HW', 'RPXYHW') == ('RPXYHW', 'RPXYHW')

def test_setup_formats_value_error():
    with pytest.raises(ValueError):
        # Test with both formats partially defined (should raise ValueError).
        setup_formats('RP...HW', 'RP...HW')


# Test the reorder function.
def test_reorder_same_format():
    data = np.zeros((3, 4, 5))
    result = reorder(data, 'TAC', 'TAC')
    np.testing.assert_array_equal(result, data)

    # Test with same longer formats.
    data = np.zeros((3, 4, 5, 6))
    result = reorder(data, 'CTHW', 'CTHW')
    np.testing.assert_array_equal(result, data)

def test_reorder_different_formats():
    data = np.zeros((3, 4, 5))
    result = reorder(data, 'TAC', 'CAT')
    assert result.shape == (5, 4, 3)

    result = reorder(data, 'TAC', 'CTA')
    assert result.shape == (5, 3, 4)

    # Test with different longer formats.
    data = np.zeros((3, 4, 5, 6))
    result = reorder(data, 'CTHW', 'WHTC')
    assert result.shape == (6, 5, 4, 3)

    result = reorder(data, 'CTHW', 'WCTH')
    assert result.shape == (6, 3, 4, 5)

def test_reorder_invalid_format():
    data = np.zeros((3, 4, 5))
    with pytest.raises(ValueError):
        reorder(data, 'TAC', 'CT')


if __name__ == "__main__":
    pytest.main()