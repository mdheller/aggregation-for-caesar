import unittest
import urllib
import flask
import json
from panoptes_aggregation.reducers.poly_line_text_reducer import process_data, poly_line_text_reducer
from panoptes_aggregation.reducers.test_utils import extract_in_data

extracted_data = [
    {
        'frame0': {
            'points': {
                'x': [
                    [775.17333984375, 1105.0302734375, 1358.499267578125, 1719.605712890625],
                    [782.1177368164062, 1282.111328125, 1605.0238037109375],
                    [782.1177368164062, 1313.3609619140625],
                    [809.8951416015625, 855.033447265625, 837.6725463867188],
                    [1004.3370361328125, 1025.170166015625, 1007.809326171875],
                    [1174.4737548828125, 1153.6407470703125, 1139.7520751953125],
                    [882.8109130859375, 1302.9443359375, 1594.6072998046875],
                    [848.089111328125, 1063.3641357421875, 1330.7218017578125, 1670.9952392578125]
                ],
                'y': [
                    [754.0413208007812, 754.0413208007812, 760.9856567382812, 747.0968627929688],
                    [955.4275512695312, 945.0110473632812, 931.1223754882812],
                    [1108.203369140625, 1104.731201171875],
                    [1250.562744140625, 872.0952758789062, 517.9331665039062],
                    [1222.78515625, 712.3751831054688, 458.90618896484375],
                    [1243.618408203125, 823.4848022460938, 267.9364013671875],
                    [917.2335815429688, 639.4594116210938, 438.07305908203125],
                    [1160.2861328125, 979.7328491210938, 823.4848022460938, 601.2654418945312]
                ]
            },
            'text': [
                ['This', 'is', 'A', 'test'],
                ['phrase', 'that', 'is'],
                ['going', 'horizontal'],
                ['And', 'this', 'test'],
                ['phrase', 'is', 'in'],
                ['the', 'vertical', 'direction'],
                ['Finally', 'this', 'phrase'],
                ['is', 'at', 'an', 'angle']
            ],
            'slope': [
                -0.3003687513450744,
                -1.6490187347355578,
                -0.37447581115123063,
                -84.322199370481954,
                -85.191381677072215,
                -92.084552300929801,
                -33.913994334734355,
                -33.694706994247483
            ]
        },
        'frame1': {
            'points': {'x': [[1, 180]], 'y': [[1, 1.1]]},
            'text': [['page', '2']],
            'slope': [0.81845546168862027]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [841.1447143554688, 872.3943481445312, 855.033447265625],
                    [802.9508056640625, 1302.9443359375, 1608.4959716796875],
                    [761.28466796875, 1282.111328125],
                    [806.4229736328125, 1087.6693115234375, 1375.860107421875, 1747.3831787109375],
                    [743.9237670898438, 1236.9730224609375, 1608.4959716796875],
                    [1174.4737548828125, 1164.0572509765625, 1184.890380859375],
                    [980.0318603515625, 1004.3370361328125, 997.3927001953125],
                    [882.8109130859375, 1070.3084716796875, 1341.1383056640625, 1650.162109375]
                ],
                'y': [
                    [1243.618408203125, 892.9284057617188, 504.04449462890625],
                    [979.7328491210938, 646.4037475585938, 410.295654296875],
                    [1111.675537109375, 1111.675537109375],
                    [771.4021606445312, 760.9856567382812, 747.0968627929688, 760.9856567382812],
                    [976.2606811523438, 951.9553833007812, 924.1779174804688],
                    [1240.146240234375, 840.8457641601562, 288.76947021484375],
                    [1278.340087890625, 736.6803588867188, 479.73919677734375],
                    [1149.86962890625, 997.0936889648438, 854.7344360351562, 632.5150756835938]
                ]
            },
            'text': [
                ['And', 'this', 'test'],
                ['Finally', 'this', 'phrase'],
                ['going', 'horizontal'],
                ['This', 'is', 'A', 'test'],
                ['phrase', 'that', 'is'],
                ['the', 'vertical', 'direction'],
                ['phrase', 'is', 'in'],
                ['is', 'at', 'an', 'angle']
            ],
            'slope': [
                -84.199673504615362,
                -35.105493581327558,
                0.0,
                -0.74857785202443772,
                -3.4142190235833518,
                -87.838924383831099,
                -87.866765532833455,
                -33.296892364919216
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [768.22900390625, 1164.0572509765625, 1396.693115234375, 1750.8553466796875],
                    [809.8951416015625, 1087.6693115234375, 1334.1939697265625, 1702.244873046875],
                    [736.9794311523438, 1257.8060302734375, 1611.9681396484375]
                ],
                'y': [
                    [754.0413208007812, 764.4578247070312, 743.6246948242188, 743.6246948242188],
                    [1177.64697265625, 983.2050170898438, 833.9013061523438, 604.7376098632812],
                    [958.8997192382812, 945.0110473632812, 927.6502075195312]
                ]
            },
            'text': [
                ['This', 'is', 'A', 'test'],
                ['is', 'at', 'an', 'angle'],
                ['phrase', 'that', 'is']
            ],
            'slope': [
                -0.83450919465025142,
                -32.547529948650428,
                -2.0067366946412353
            ]
        },
        'frame1': {
            'points': {'x': [[1.1, 180.1]], 'y': [[0.9, 1]]},
            'text': [['page', '2']],
            'slope': [0.81845546168861394]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [1184.890380859375, 1171.0015869140625, 1171.0015869140625],
                    [778.6455078125, 1330.7218017578125, 1618.91259765625],
                    [778.6455078125, 1098.0859375, 1389.748779296875, 1664.0509033203125],
                    [990.4483642578125, 1011.281494140625, 997.3927001953125],
                    [841.1447143554688, 1052.9476318359375, 1292.52783203125, 1660.5787353515625],
                    [827.2560424804688, 851.561279296875, 851.561279296875],
                    [761.28466796875, 1275.1669921875, 1625.85693359375],
                    [778.6455078125, 1358.499267578125]
                ],
                'y': [
                    [1257.507080078125, 722.7916870117188, 278.3529052734375],
                    [1014.4546508789062, 656.8202514648438, 413.767822265625],
                    [795.7073364257812, 764.4578247070312, 764.4578247070312, 757.5134887695312],
                    [1226.25732421875, 740.1525268554688, 517.9331665039062],
                    [1139.452880859375, 990.1493530273438, 854.7344360351562, 622.0984497070312],
                    [1267.923583984375, 879.0396118164062, 504.04449462890625],
                    [938.0667114257812, 934.5945434570312, 931.1223754882812],
                    [1101.259033203125, 1108.203369140625]
                ]
            },
            'text': [
                ['the', 'vertical', 'direction'],
                ['Finally,', 'this', 'phrase'],
                ['This', 'is', 'A', 'test'],
                ['phrase', 'is', 'in'],
                ['is', 'at', 'an', 'angle'],
                ['And', 'this', 'test'],
                ['phrase', 'that', 'is'],
                ['going', 'horizontal']
            ],
            'slope': [
                -91.051186978121308,
                -35.21990024826794,
                -2.2619714405899383,
                -86.768966756841976,
                -31.989667740964151,
                -87.585344318301594,
                -0.45479488421022657,
                0.68614217577777903
            ]
        },
        'frame1': {
            'points': {'x': [[1.05, 179.9]], 'y': [[0.8, 0.9]]},
            'text': [['page', '2']],
            'slope': [0.83637532542241544]
        }
    }
]

processed_data = {
    'frame0': {
        'x': [
            [775.17333984375, 1105.0302734375, 1358.499267578125, 1719.605712890625],
            [782.1177368164062, 1282.111328125, 1605.0238037109375],
            [782.1177368164062, 1313.3609619140625],
            [809.8951416015625, 855.033447265625, 837.6725463867188],
            [1004.3370361328125, 1025.170166015625, 1007.809326171875],
            [1174.4737548828125, 1153.6407470703125, 1139.7520751953125],
            [882.8109130859375, 1302.9443359375, 1594.6072998046875],
            [848.089111328125, 1063.3641357421875, 1330.7218017578125, 1670.9952392578125],
            [841.1447143554688, 872.3943481445312, 855.033447265625],
            [802.9508056640625, 1302.9443359375, 1608.4959716796875],
            [761.28466796875, 1282.111328125],
            [806.4229736328125, 1087.6693115234375, 1375.860107421875, 1747.3831787109375],
            [743.9237670898438, 1236.9730224609375, 1608.4959716796875],
            [1174.4737548828125, 1164.0572509765625, 1184.890380859375],
            [980.0318603515625, 1004.3370361328125, 997.3927001953125],
            [882.8109130859375, 1070.3084716796875, 1341.1383056640625, 1650.162109375],
            [768.22900390625, 1164.0572509765625, 1396.693115234375, 1750.8553466796875],
            [809.8951416015625, 1087.6693115234375, 1334.1939697265625, 1702.244873046875],
            [736.9794311523438, 1257.8060302734375, 1611.9681396484375],
            [1184.890380859375, 1171.0015869140625, 1171.0015869140625],
            [778.6455078125, 1330.7218017578125, 1618.91259765625],
            [778.6455078125, 1098.0859375, 1389.748779296875, 1664.0509033203125],
            [990.4483642578125, 1011.281494140625, 997.3927001953125],
            [841.1447143554688, 1052.9476318359375, 1292.52783203125, 1660.5787353515625],
            [827.2560424804688, 851.561279296875, 851.561279296875],
            [761.28466796875, 1275.1669921875, 1625.85693359375],
            [778.6455078125, 1358.499267578125]
        ],
        'y': [
            [754.0413208007812, 754.0413208007812, 760.9856567382812, 747.0968627929688],
            [955.4275512695312, 945.0110473632812, 931.1223754882812],
            [1108.203369140625, 1104.731201171875],
            [1250.562744140625, 872.0952758789062, 517.9331665039062],
            [1222.78515625, 712.3751831054688, 458.90618896484375],
            [1243.618408203125, 823.4848022460938, 267.9364013671875],
            [917.2335815429688, 639.4594116210938, 438.07305908203125],
            [1160.2861328125, 979.7328491210938, 823.4848022460938, 601.2654418945312],
            [1243.618408203125, 892.9284057617188, 504.04449462890625],
            [979.7328491210938, 646.4037475585938, 410.295654296875],
            [1111.675537109375, 1111.675537109375],
            [771.4021606445312, 760.9856567382812, 747.0968627929688, 760.9856567382812],
            [976.2606811523438, 951.9553833007812, 924.1779174804688],
            [1240.146240234375, 840.8457641601562, 288.76947021484375],
            [1278.340087890625, 736.6803588867188, 479.73919677734375],
            [1149.86962890625, 997.0936889648438, 854.7344360351562, 632.5150756835938],
            [754.0413208007812, 764.4578247070312, 743.6246948242188, 743.6246948242188],
            [1177.64697265625, 983.2050170898438, 833.9013061523438, 604.7376098632812],
            [958.8997192382812, 945.0110473632812, 927.6502075195312],
            [1257.507080078125, 722.7916870117188, 278.3529052734375],
            [1014.4546508789062, 656.8202514648438, 413.767822265625],
            [795.7073364257812, 764.4578247070312, 764.4578247070312, 757.5134887695312],
            [1226.25732421875, 740.1525268554688, 517.9331665039062],
            [1139.452880859375, 990.1493530273438, 854.7344360351562, 622.0984497070312],
            [1267.923583984375, 879.0396118164062, 504.04449462890625],
            [938.0667114257812, 934.5945434570312, 931.1223754882812],
            [1101.259033203125, 1108.203369140625]
        ],
        'text': [
            ['This', 'is', 'A', 'test'],
            ['phrase', 'that', 'is'],
            ['going', 'horizontal'],
            ['And', 'this', 'test'],
            ['phrase', 'is', 'in'],
            ['the', 'vertical', 'direction'],
            ['Finally', 'this', 'phrase'],
            ['is', 'at', 'an', 'angle'],
            ['And', 'this', 'test'],
            ['Finally', 'this', 'phrase'],
            ['going', 'horizontal'],
            ['This', 'is', 'A', 'test'],
            ['phrase', 'that', 'is'],
            ['the', 'vertical', 'direction'],
            ['phrase', 'is', 'in'],
            ['is', 'at', 'an', 'angle'],
            ['This', 'is', 'A', 'test'],
            ['is', 'at', 'an', 'angle'],
            ['phrase', 'that', 'is'],
            ['the', 'vertical', 'direction'],
            ['Finally,', 'this', 'phrase'],
            ['This', 'is', 'A', 'test'],
            ['phrase', 'is', 'in'],
            ['is', 'at', 'an', 'angle'],
            ['And', 'this', 'test'],
            ['phrase', 'that', 'is'],
            ['going', 'horizontal']
        ],
        'slope': [
            -0.3003687513450744,
            -1.6490187347355578,
            -0.37447581115123063,
            -84.322199370481954,
            -85.191381677072215,
            -92.084552300929801,
            -33.913994334734355,
            -33.694706994247483,
            -84.199673504615362,
            -35.105493581327558,
            0.0,
            -0.74857785202443772,
            -3.4142190235833518,
            -87.838924383831099,
            -87.866765532833455,
            -33.296892364919216,
            -0.83450919465025142,
            -32.547529948650428,
            -2.0067366946412353,
            -91.051186978121308,
            -35.21990024826794,
            -2.2619714405899383,
            -86.768966756841976,
            -31.989667740964151,
            -87.585344318301594,
            -0.45479488421022657,
            0.68614217577777903
        ]
    },
    'frame1': {
        'x': [
            [1, 180],
            [1.1, 180.1],
            [1.05, 179.9]
        ],
        'y': [
            [1, 1.1],
            [0.9, 1],
            [0.8, 0.9]
        ],
        'text': [
            ['page', '2'],
            ['page', '2'],
            ['page', '2']
        ],
        'slope': [
            0.81845546168862027,
            0.81845546168861394,
            0.83637532542241544
        ]
    }
}

reduced_data = {
    'frame0': [
        {
            'clusters_x': [
                782.11770629882812,
                1113.710693359375,
                1380.2003173828125,
                1720.4737854003906
            ],
            'clusters_y': [
                768.79803466796875,
                760.98565673828125,
                754.041259765625,
                752.30517578125
            ],
            'clusters_text': [
                ['This', 'This', 'This', 'This'],
                ['is', 'is', 'is', 'is'],
                ['A', 'A', 'A', 'A'],
                ['test', 'test', 'test', 'test']
            ],
            'line_slope': -1.0325936555594113
        },
        {
            'clusters_x': [
                756.07640075683594,
                1263.0143432617188,
                1612.8362121582031
            ],
            'clusters_y': [
                957.16366577148438,
                944.14300537109375,
                928.51821899414062
            ],
            'clusters_text': [
                ['phrase', 'phrase', 'phrase', 'phrase'],
                ['that', 'that', 'that', 'that'],
                ['is', 'is', 'is', 'is']
            ],
            'line_slope': -1.0325936555594113
        },
        {
            'clusters_x': [
                774.01597086588538,
                1317.9905192057292
            ],
            'clusters_y': [
                1107.0459798177083,
                1108.203369140625
            ],
            'clusters_text': [
                ['going', 'going', 'going'],
                ['horizontal', 'horizontal', 'horizontal']
            ],
            'line_slope': -1.0325936555594113
        },
        {
            'clusters_x': [
                826.0986328125,
                859.66302490234375,
                848.08909098307288
            ],
            'clusters_y': [
                1254.034912109375,
                881.35443115234375,
                508.67405192057294
            ],
            'clusters_text': [
                ['And', 'And', 'And'],
                ['this', 'this', 'this'],
                ['test', 'test', 'test']
            ],
            'line_slope': -87.434332758114309
        },
        {
            'clusters_x': [
                991.60575358072913,
                1013.5962320963541,
                1000.8649088541666
            ],
            'clusters_y': [
                1242.4608561197917,
                729.73602294921875,
                485.52618408203125
            ],
            'clusters_text': [
                ['phrase', 'phrase', 'phrase'],
                ['is', 'is', 'is'],
                ['in', 'in', 'in']
            ],
            'line_slope': -87.434332758114309
        },
        {
            'clusters_x': [
                1177.9459635416667,
                1162.8998616536458,
                1165.2146809895833
            ],
            'clusters_y': [
                1247.090576171875,
                795.70741780598962,
                278.35292561848956
            ],
            'clusters_text': [
                ['the', 'the', 'the'],
                ['vertical', 'vertical', 'vertical'],
                ['direction', 'direction', 'direction']
            ],
            'line_slope': -87.434332758114309
        },
        {
            'clusters_x': [
                821.46907552083337,
                1312.2034912109375,
                1607.338623046875
            ],
            'clusters_y': [
                970.47369384765625,
                647.56113688151038,
                420.71217854817706
            ],
            'clusters_text': [
                ['Finally', 'Finally', 'Finally,'],
                ['this', 'this', 'this'],
                ['phrase', 'phrase', 'phrase']
            ],
            'line_slope': -33.681169316158737
        },
        {
            'clusters_x': [
                845.48497009277344,
                1068.5723876953125,
                1324.6454772949219,
                1670.9952392578125
            ],
            'clusters_y': [
                1156.8139038085938,
                987.54522705078125,
                841.7137451171875,
                615.15414428710938
            ],
            'clusters_text': [
                ['is', 'is', 'is', 'is'],
                ['at', 'at', 'at', 'at'],
                ['an', 'an', 'an', 'an'],
                ['angle', 'angle', 'angle', 'angle']
            ],
            'line_slope': -33.681169316158737
        }
    ],
    'frame1': [
        {
            'clusters_x': [
                1.05,
                180.0
            ],
            'clusters_y': [
                0.90000000000000002,
                1.0
            ],
            'clusters_text': [
                ['page', 'page', 'page'],
                ['2', '2', '2']
            ],
            'line_slope': 0.82442874959988321
        }
    ]
}


class TestClusterLines(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.kwargs = {
            'eps_slope': 25,
            'eps_line': 50,
            'eps_word': 110,
            'min_samples': 1
        }

    def test_process_data(self):
        result = process_data(extracted_data)
        self.assertDictEqual(result, processed_data)

    def test_cluster_lines(self):
        result = poly_line_text_reducer._original(processed_data, metric='euclidean', **self.kwargs)
        self.assertDictEqual(result, reduced_data)

    def test_poly_line_text_reducer(self):
        result = poly_line_text_reducer(extracted_data, **self.kwargs)
        self.assertDictEqual(result, reduced_data)

    def test_poly_line_text_reducer_request(self):
        app = flask.Flask(__name__)
        request_kwargs = {
            'data': json.dumps(extract_in_data(extracted_data)),
            'content_type': 'application/json'
        }
        url_params = '?{0}'.format(urllib.parse.urlencode(self.kwargs))
        with app.test_request_context(url_params, **request_kwargs):
            result = poly_line_text_reducer(flask.request)
            self.assertDictEqual(result, reduced_data)


if __name__ == '__main__':
    unittest.main()
