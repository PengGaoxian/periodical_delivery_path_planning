# 计算车辆绕行取货路径经过的距离（单程）
from A_star import calculate_heuristic
def calDetourGridnum4Vehicle(pickup_grid, dropdown_grid, commuting_route_1d_array):
    min_detour_grid_num = 0 # 绕行取货路径经过的网格数
    # 如果pickup_grid不在commuting_route_1d_array中，则计算pickup_grid到commuting_route_1d_array中每一个网格的距离，取最小值
    if pickup_grid not in commuting_route_1d_array:
        min_detour_grid_num1 = 100000
        for grid in commuting_route_1d_array[1:]:
            grid_num = calculate_heuristic(grid, pickup_grid)
            if grid_num < min_detour_grid_num1:
                min_detour_grid_num1 = grid_num
        min_detour_grid_num += min_detour_grid_num1
    # 如果dropdown_grid不在commuting_route_1d_array中，则计算dropdown_grid到commuting_route_1d_array中每一个网格的距离，取最小值
    if dropdown_grid not in commuting_route_1d_array:
        min_detour_grid_num2 = 100000
        for grid in commuting_route_1d_array[1:]:
            grid_num = calculate_heuristic(grid, pickup_grid)
            if grid_num < min_detour_grid_num2:
                min_detour_grid_num2 = grid_num
        min_detour_grid_num += min_detour_grid_num2

    return min_detour_grid_num

# 计算车辆的绕行成本，即绕行取货路径或送货返回经过的距离，此时货物并不在车上（单程）
def calDetourCost4Vehicle(pickup_grid, dropdown_grid, commuting_route_1d_array):
    min_detour_grid_num = calDetourGridnum4Vehicle(pickup_grid, dropdown_grid, commuting_route_1d_array)
    detour_distance = min_detour_grid_num * 300 / 1000 # 每个网格的边长为300m
    detour_cost = detour_distance * 0.8 # 绕行成本为每公里0.8元
    return detour_cost


# 计算单个物流任务的绕行成本（单程）
def calDetourCost4SingleTask(logistics_start_grid, logistics_end_grid, relay_point_1d_array, vehicleSeq4SingleTask_2d_array):
    detourCost4VehicleSeq = 0 # 车辆序列绕行成本
    if relay_point_1d_array == []:
        detourCost4VehicleSeq = calDetourCost4Vehicle(logistics_start_grid, logistics_end_grid, vehicleSeq4SingleTask_2d_array[0])
    else:
        # 遍历车辆序列中的每一辆车
        for index, vehicleGrid_1d_array in enumerate(vehicleSeq4SingleTask_2d_array):
            # 计算车辆序列中的第一辆车绕行成本
            if index == 0:
                detourCost4firstVehicle = calDetourCost4Vehicle(logistics_start_grid, relay_point_1d_array[0], vehicleGrid_1d_array)
                detourCost4VehicleSeq += detourCost4firstVehicle
            # 计算车辆序列中的最后一辆车绕行成本
            elif index == len(vehicleSeq4SingleTask_2d_array) - 1:
                detourCost4lastVehicle = calDetourCost4Vehicle(relay_point_1d_array[-1], logistics_end_grid, vehicleGrid_1d_array)
                detourCost4VehicleSeq += detourCost4lastVehicle
            # 计算车辆序列中除第一辆车和最后一辆车之外的车辆绕行成本
            else:
                detourCost4middleVehicle = calDetourCost4Vehicle(relay_point_1d_array[index - 1], relay_point_1d_array[index], vehicleGrid_1d_array)
                detourCost4VehicleSeq += detourCost4middleVehicle
            # 计算车辆序列中的第一辆车绕行到物流路径起点的时间

    return detourCost4VehicleSeq


# 计算车辆的运输成本
def calTransportCost4Vehicle(pickup_grid, dropdown_grid, common_route_1d_array):
    min_detour_grid_num = calDetourGridnum4Vehicle(pickup_grid, dropdown_grid, common_route_1d_array)
    common_grid_num = len(common_route_1d_array)
    # 运输路径经过的网格数 = 运输路径经过的网格数 + 绕行路径经过的网格数（单程，此时车辆是载货状态）
    total_transport_grid_num = min_detour_grid_num + common_grid_num
    transport_distance = total_transport_grid_num * 300 / 1000 # 每个网格的边长为300m
    transport_cost = transport_distance * 1.2 # 运输成本为每公里0.8元
    return transport_cost


# 计算所有单个任务的运输成本
def calTransportCost4SingleTask(logistics_start_grid, logistics_end_grid, relay_point_1d_array, vehicleSeq4SingleTask_2d_array):
    transportCost4VehicleSeq = 0 # 车辆序列运输成本
    if relay_point_1d_array == []:
        transportCost4VehicleSeq = calTransportCost4Vehicle(logistics_start_grid, logistics_end_grid, vehicleSeq4SingleTask_2d_array[0])
    else:
        # 遍历车辆序列中的每一辆车
        for index, common_route_1d_array in enumerate(vehicleSeq4SingleTask_2d_array):
            # 计算车辆序列中的第一辆车运输成本
            if index == 0:
                transportCost4firstVehicle = calTransportCost4Vehicle(logistics_start_grid, relay_point_1d_array[0], common_route_1d_array)
                transportCost4VehicleSeq += transportCost4firstVehicle
            # 计算车辆序列中的最后一辆车运输成本
            elif index == len(vehicleSeq4SingleTask_2d_array) - 1:
                transportCost4lastVehicle = calTransportCost4Vehicle(relay_point_1d_array[-1], logistics_end_grid, common_route_1d_array)
                transportCost4VehicleSeq += transportCost4lastVehicle
            # 计算车辆序列中除第一辆车和最后一辆车之外的车辆运输成本
            else:
                transportCost4middleVehicle = calTransportCost4Vehicle(relay_point_1d_array[index - 1], relay_point_1d_array[index], common_route_1d_array)
                transportCost4VehicleSeq += transportCost4middleVehicle

    return transportCost4VehicleSeq


# 计算车辆在取送货绕行过程和接力过程额外消耗的时间
def calDetourRelayTime4Vehicle(pickup_grid, dropdown_grid, common_route_1d_array):
    min_detour_grid_num = calDetourGridnum4Vehicle(pickup_grid, dropdown_grid, common_route_1d_array)
    # min_detour_grid_num是单程绕行网格数，双程绕行网格数为min_detour_grid_num * 2，每个网格的边长为300m，车辆速度为10m/s
    detour_time = min_detour_grid_num * 2 * 300 / 10 / 60  # 绕行时间，单位为分钟
    relay_time = 2 # 车辆在取货点和送货点停留的时间，单位为分钟
    # 总时间，单位为分钟
    detour_relay_time = detour_time + relay_time * 2 # 取货一次，送货一次

    return detour_relay_time

# 计算车辆组合是否满足时间限制，任何一辆车的通勤+取送货时间超过60分钟，则违反时间限制
"""
vehicleSeqCompo_3d_array = [
    [['C1',1,2,3,4], ['C2',5,6,7,8], ['C3',9,10,11,12]], # 能完成第一个物流任务的车辆序列
    [['C1',1,2,3,4], ['C2',5,6,7,8], ['C3',9,10,11,12]]  # 能完成第二个物流任务的车辆序列
]
start_1d_array = [1,5,9] # 车辆的起始网格
end_1d_array = [4,8,12] # 车辆的终止网格
relay_point_2d_array = [[0,1,2,3,4],[0,5,6,7,8],[0,9,10,11,12]] # 车辆的通勤路径
"""
def isMeetTimeLimit4VehicleSeqComp(vehicleSeqCompo_3d_array, commuting_time_1d_array, logistics_task_2d_array, relay_point_2d_array):
    # 定义一个字典类型的变量，用于存储车辆的名称和通勤和取送货过程消耗的总时间
    vehicle_total_time = {}
    # 遍历车辆序列组合中的每组车辆序列（用于完成一个物流任务的车辆序列）
    for i, vehicleSeq_2d_array in enumerate(vehicleSeqCompo_3d_array):
        # 遍历车辆序列中的每辆车
        for j, vehicleGrid_1d_array in enumerate(vehicleSeq_2d_array):
            common_route_1d_array = vehicleGrid_1d_array[1:] # 车辆的通勤路径
            vehicle_name = vehicleGrid_1d_array[0] # 车辆名称
            # 提取vehicle_name中的数字，即车辆的序号，vehicle_name的格式为C1、C2、C3、C4、C5、C6、C7、C8、C9、C10
            vehicle_index = int(vehicle_name[1:])
            commuting_time = commuting_time_1d_array[vehicle_index-1] # 车辆的通勤时间

            start_end_grid = logistics_task_2d_array[i]
            # 如果relay_point_2d_array[i]为空
            if len(relay_point_2d_array[i]) == 0:
                pickup_grid = start_end_grid[0]
                dropdown_grid = start_end_grid[1]
            else:
                # 计算车辆的取货点和送货点
                if j == 0:
                    pickup_grid = start_end_grid[0]
                    dropdown_grid = relay_point_2d_array[i][0]
                elif j == len(vehicleSeq_2d_array)-1:
                    pickup_grid = relay_point_2d_array[i][-1]
                    dropdown_grid = start_end_grid[1]
                else:
                    pickup_grid = relay_point_2d_array[i][j-1]
                    dropdown_grid = relay_point_2d_array[i][j]

            # 如果车辆名称不在vehicle_total_time中，则将车辆名称和通勤+取送货过程消耗的总时间存入vehicle_total_time中
            if vehicle_name not in vehicle_total_time:
                # 计算车辆的绕行时间和接力时间
                detour_relay_time = calDetourRelayTime4Vehicle(pickup_grid, dropdown_grid, common_route_1d_array)
                # 存储车辆消耗的总时间
                vehicle_total_time[vehicle_name] = detour_relay_time + commuting_time
                if vehicle_total_time[vehicle_name] > 60:
                    print("overtime: " + vehicle_name)
                    return False
            else:
                # 计算车辆的绕行时间和接力时间
                detour_relay_time = calDetourRelayTime4Vehicle(pickup_grid, dropdown_grid, common_route_1d_array)
                # 更新车辆消耗的总时间
                vehicle_total_time[vehicle_name] += detour_relay_time
                if vehicle_total_time[vehicle_name] > 60:
                    print("overtime: " + vehicle_name)
                    return False
    return True


# 计算车辆最大的载货总重量
"""
vehicleSeqCompo_3d_array = [
    [['C1',1,2,3,4], ['C2',5,6,7,8], ['C3',9,10,11,12]], # 能完成第一个物流任务的车辆序列
    [['C1',1,2,3,4], ['C2',5,6,7,8], ['C3',9,10,11,12]]  # 能完成第二个物流任务的车辆序列
]
"""
def isMeetWeightLimit4VehicleSeqComp(vehicleSeqCompo_3d_array, logistics_task_weight_1d_array):
    class Vehicle:
        def __init__(self, name, task_weight, route_grid):
            self.name = name
            self.task_weight_1d_array = [task_weight]
            self.route_grid_2d_array = [route_grid]

        def update(self, task_weight, route_grid):
            self.task_weight_1d_array.append(task_weight)
            self.route_grid_2d_array.append(route_grid)

    # 遍历vehicleSeqCompo_3d_array中的每组车辆序列
    vehicle_list = []
    # i为第i个物流任务，vehicleSeq_2d_array为能完成第i个物流任务的车辆序列
    for i, vehicleSeq_2d_array in enumerate(vehicleSeqCompo_3d_array):
        # vehicleGrid_1d_array为车辆序列中的某一辆车在配送过程中的路径网格
        for j, vehicleGrid_1d_array in enumerate(vehicleSeq_2d_array):
            vehicle_name = vehicleGrid_1d_array[0]
            # 取出vehicle_list中的车辆名称，存入name_list中
            name_list = [vehicle.name for vehicle in vehicle_list]
            # 如果vehicle_name不在name_list中，则创建一个新的车辆对象，并将其存入vehicle_list中
            if vehicle_name not in name_list:
                task_weight = logistics_task_weight_1d_array[i] # 获取车辆配送任务的重量
                route_grid = vehicleGrid_1d_array[1:] # 获取车辆的配送路径
                # 创建一个新的车辆对象
                vehicle = Vehicle(vehicle_name, task_weight, route_grid)
                # 将车辆对象存入vehicle_list中
                vehicle_list.append(vehicle)
            # 如果vehicle_name在name_list中，则更新vehicle_list
            else:
                # 获取vehicle_list中的车辆对象
                vehicle = vehicle_list[name_list.index(vehicle_name)]
                new_task_weight = logistics_task_weight_1d_array[i] # 获取车辆配送任务的重量
                new_route_grid = vehicleGrid_1d_array[1:] # 获取车辆的配送路径
                '''
                [['C1',1,2,3,4], ['C2',5,6,7,8], ['C3',9,10,11,12]], # 能完成第一个物流任务的车辆序列
                [['C1',1,2,3,4], ['C2',5,6,7,8], ['C3',9,10,11,12]]  # 能完成第二个物流任务的车辆序列
                vehicle = {
                    vehicle_name = 'C1'
                    task_weight_1d_array = [10,20]
                    route_grid_2d_array = [[1,2,3,4], [1,2,3,4]]
                }
                '''
                sum_weight = new_task_weight
                # 遍历vehicle.route_grid_2d_array中的每个route_grid
                for k, route_grid in enumerate(vehicle.route_grid_2d_array):
                    # 如果vehicle_route_grid与route_grid有交集，则累加task_weight到sum_weight中
                    set_route_grid = set(route_grid)
                    set_new_route_grid = set(new_route_grid)
                    if set_route_grid.intersection(set_new_route_grid):
                        sum_weight += vehicle.task_weight_1d_array[k]
                        if sum_weight > 80:
                            print("overload:" + vehicle_name)
                            return False

                # 更新车辆对象的属性
                vehicle.update(new_task_weight, new_route_grid)
    return True 
