arr = [20459440, 20458987, 20458733, 20458586, 20458284, 20458202, 20457860, 20457611, 20456391, 20455888, 20455269,
       20454830, 20454212, 20454184, 20454146, 20453922, 20452542, 20450716, 20447814, 20438557, 20424174, 20419436,
       20409217, 20394189, 20378130, 20356098, 20352091, 20343586, 20338069, 20337799, 20333280, 20318024, 20275819,
       20269554, 20262684, 20258563, 20219905, 20142943, 20133957, 20121781, 20085324, 19987253, 19969031, 19942288,
       19844122, 19804714, 19789399, 19770693, 19700226, 19576007, 19483542, 19425997, 19042165, 19000064, 18909725,
       18904145, 18669822, 18565022, 18389987, 18259359, 18208953, 17988689, 17884456, 17790401, 17621170, 17553892,
       17473537, 17466361, 17365278, 17328129, 17185953, 17152062, 17049913, 17002217, 16957514, 16924540, 16911050,
       16644262, 16390849, 16120793, 15767106, 15712028, 15687846, 15649054, 15620747, 15559984, 15540739, 15525037,
       15274479, 15188702, 15088029, 15005839, 14904846, 14711057, 14570473, 14493796, 14440953, 14434577, 14377384,
       14222650, 14216684, 14164919, 14111535, 14089191, 13819282, 13717991, 13467012, 13272225, 13155286, 2904628,
       2708180, 2495704, 2060841, 2025011, 2023169, 2007456, 1851034, 1338200, 1325433, 898261, 440324,440324,898261]


def test_same():
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                print(f'相同的数字：{arr[i]}')
