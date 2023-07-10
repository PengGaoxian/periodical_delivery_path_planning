import openpyxl
from AdaptiveGA import calIndividualFitness
from extract_parameter import getEncodeNumBoundary, getVehicleCommutingTime, getLogisticsTaskInfo, getRelayPoint

commuting_time_1d_array = getVehicleCommutingTime('dataSet/commuting_route.xlsx', 'commuting_route_grid')
logisticsTaskInfo_list = getLogisticsTaskInfo('dataSet/logistics_task.xlsx', 'WGS84_logistics_task_10')

comp_3d_array = [
    [['C55', 1081, 1026, 971, 916, 915, 860]],
    [['C14', 947, 948, 949, 950, 951, 952, 1007, 1008, 1009, 1010, 955, 956, 957, 958, 959, 960, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1076, 1077, 1078, 1079]],
    [['C95', 1555, 1500, 1445, 1390, 1335, 1280, 1225, 1226, 1171, 1116, 1061, 1006, 951, 950, 949, 948, 947, 946]],
    [['C45', 1548, 1603, 1658, 1713, 1714, 1715, 1716]],
    [['C100', 353, 352, 351, 350, 349, 348, 347, 346, 345, 344, 343, 398, 453, 452, 451, 506, 561, 616, 671, 726, 781, 836, 835, 834, 833, 888, 887, 942, 997, 1052, 1107]],
    [['C22', 864, 865, 866, 867, 812, 757, 702, 701, 646, 591, 536, 535, 480, 425, 370]],
    [['C33', 803, 858, 913, 968, 1023]],
    [['C36', 1171, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1296, 1297, 1298, 1299, 1300, 1301]],
    [['C36', 1364, 1363, 1362, 1361, 1306, 1305, 1304, 1303, 1302, 1301, 1300, 1299, 1298, 1297, 1296, 1241, 1240, 1239, 1238, 1237, 1236, 1235, 1234, 1233, 1232, 1231, 1230, 1229, 1228, 1227, 1226, 1171]],
    [['C39', 860, 861, 862, 863, 864, 865, 866, 867, 922, 977, 1032, 1033, 1088, 1089, 1144]]
]

relay_points_2d_array = getRelayPoint('dataSet/trans_points.xlsx', '100%', comp_3d_array)

print(commuting_time_1d_array)
print(logisticsTaskInfo_list)
print(relay_points_2d_array)

comp_result = calIndividualFitness(comp_3d_array, commuting_time_1d_array, logisticsTaskInfo_list, relay_points_2d_array)
print(comp_result.gene)
print(comp_result.compCost)
print(comp_result.singleTaskCost_1d_array)
print(comp_result.IsinTimeLimit)
print(comp_result.IsinWeightLimit)