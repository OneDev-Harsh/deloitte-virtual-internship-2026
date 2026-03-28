# This module normalizes telemetry data from multiple device formats
# into a unified schema for downstream processing and analytics.

# import the necessary modules and libraries
import json
import unittest
import datetime

# use the open function to open and read the three json files
# using 'ecoding="utf-8"' to ensure proper handling of any special characters (UTF-8 supports all Unicode characters (including ō))
with open("./data-1.json", "r", encoding="utf-8") as f:
    jsonData1 = json.load(f)

with open("./data-2.json", "r", encoding="utf-8") as f:
    jsonData2 = json.load(f)

with open("./data-result.json", "r", encoding="utf-8") as f:
    jsonExpectedResult = json.load(f)


# convert json data from format 1 to the expected format
def convertFromFormat1(jsonObject):

    # Split the location string into its components
    locationParts = jsonObject.get("location", "").split("/")

    # Basic validation to ensure correct structure
    if len(locationParts) != 5:
        raise ValueError("Invalid location format in Type 1 data")

    result = {
        'deviceID': jsonObject.get('deviceID'),
        'deviceType': jsonObject.get('deviceType'),
        'timestamp': jsonObject.get('timestamp'),
        'location': {
            'country': locationParts[0],
            'city': locationParts[1],
            'area': locationParts[2],
            'factory': locationParts[3],
            'section': locationParts[4]
        },
        'data': {
            'status': jsonObject.get('operationStatus'),
            'temperature': jsonObject.get('temp')
        }
    }

    return result


# convert json data from format 2 to the expected format
def convertFromFormat2(jsonObject):

    # Convert ISO 8601 timestamp to milliseconds since epoch
    try:
        dt = datetime.datetime.strptime(
            jsonObject['timestamp'],
            '%Y-%m-%dT%H:%M:%S.%fZ'
        )
    except ValueError:
        raise ValueError("Invalid timestamp format in Type 2 data")

    epoch = datetime.datetime(1970, 1, 1)
    timestamp = int((dt - epoch).total_seconds() * 1000)

    result = {
        'deviceID': jsonObject['device'].get('id'),
        'deviceType': jsonObject['device'].get('type'),
        'timestamp': timestamp,
        'location': {
            'country': jsonObject.get('country'),
            'city': jsonObject.get('city'),
            'area': jsonObject.get('area'),
            'factory': jsonObject.get('factory'),
            'section': jsonObject.get('section')
        },
        'data': {
            'status': jsonObject['data'].get('status'),
            'temperature': jsonObject['data'].get('temperature')
        }
    }

    return result


def main(jsonObject):

    # Determine input format based on presence of 'device' key
    if jsonObject.get('device') is None:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)


# Test cases using unittest module
class TestSolution(unittest.TestCase):

    # Sanity test to ensure the expected result is as intended
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )


if __name__ == '__main__':
    # run the tests
    unittest.main()