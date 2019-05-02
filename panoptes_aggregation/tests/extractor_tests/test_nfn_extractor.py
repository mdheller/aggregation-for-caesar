from panoptes_aggregation import extractors
from .base_test_class import ExtractorTest

classification = {
    "annotations": [
        {
            "task": "T10",
            "value": [
                {
                    "value": 1982,
                    "option": True
                }
            ]
        },
        {
            "task": "T1",
            "value": [
                {
                    "value": "United States",
                    "option": True
                }
            ]
        }
    ],
    "metadata": {
        "utc_offset": "21600",
    },
    "created_at": "2019-01-14T19:28:13.667Z",
}

expected = {
    "workflow": "herbarium",
    "decade": "80s",
    "time": "nightowl",
    "country": "United States"
}

TestNfN = ExtractorTest(
    extractors.nfn_extractor,
    classification,
    expected,
    'Test NfN with year and country tasks specified done at night',
    kwargs={'year': 'T10', 'workflow': 'herbarium', 'country': "T1"}
)

classification = {
    "annotations": [{
        "task": "T31",
        "value": [
            {
                "task": "T10",
                "value": [
                    {
                        "value": 1999,
                        "option": True
                    }
                ]
            }
        ]
    }],
    "metadata": {
        "utc_offset": "21600",
    },
    "subject": {
        "metadata": {
            "country": "United States",
        }
    },
    "created_at": "2019-04-22T06:28:13.667Z",
}

expected = {
    "workflow": "herbarium",
    "decade": "90s",
    "time": "lunchbreak",
    "earth_day": True,
    "country": "United States"
}

TestNfN = ExtractorTest(
    extractors.nfn_extractor,
    classification,
    expected,
    'Test NfN on Earth Day with year as nested task and country from metadata. At lunchtime, local time.',
    kwargs={'year': 'T10', 'workflow': 'herbarium', 'country': 'metadata'}
)
