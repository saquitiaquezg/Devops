from main import get_wheaher
import unittest
from unittest.mock import patch

@patch("main.request.get")
def test_get_wheather(mock_get):
    mock_get.return_value.json.return_value = {"temperature": 22}

    result = get_wheaher()
#    assert result == 22
    self.assertTrue(result,22)

if _name_ == '_main_':
    unittest.main()