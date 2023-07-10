## 数据集说明
### EasyPoI程序导出的PoI位置数据
使用EasyPoI百度版，查找区域为长沙市，关键词为公司、住宅小区、仓库，导出的数据如下：
1. [EasyPoI_company.xlsx](dataSet/EasyPoI_company.xlsx)（公司位置坐标）
2. [EasyPoI_home.xlsx](dataSet/EasyPoI_home.xlsx)（住宅小区位置坐标）
3. [EasyPoI_warehouse.xlsx](dataSet/EasyPoI_warehouse.xlsx)（仓库位置坐标）

### PoI位置数据转换坐标系，导入ArcGIS Pro
EasyPoI导出的PoI位置坐标系为BD09，需要转换成WGS84坐标系的数据。虽然EasyPoI也能导出WGS84坐标，但是导出来的数据不准确，所以不建议直接从EasyPoI直接导出WGS84坐标系的数据。坐标系的转换需要使用[transfer.py](transfer.py)脚本。EasyPoI百度地图版导出来的数据为BD09坐标系，需要转换成WGS84坐标系的数据才能在ArcGIS Pro中使用。
1. [ArcGIS_company.xlsx](dataSet/ArcGIS_company.xlsx)（长沙市内的公司位置的WGS84坐标）
    - WGS84表
        - lng：WGS84坐标系下，长沙市区内的公司位置的经度
        - lat：WGS84坐标系下，长沙市区内的公司位置的纬度
        - name：公司名称
    - GCJ02表
        - lng：GCJ02坐标系下，长沙市区内的公司位置的经度
        - lat：GCJ02坐标系下，长沙市区内的公司位置的纬度
        - name：公司名称
    - BD09表
        - lng：BD09坐标系下，长沙市区内的公司位置的经度
        - lat：BD09坐标系下，长沙市区内的公司位置的纬度
        - name：公司名称
2. [ArcGIS_home.xlsx](dataSet/ArcGIS_home.xlsx)（长沙市内的住宅小区位置的WGS84坐标）
    - WGS84表
        - lng：WGS84坐标系下，长沙市区内的住宅小区位置的经度
        - lat：WGS84坐标系下，长沙市区内的住宅小区位置的纬度
        - name：住宅小区名称
    - GCJ02表
        - lng：GCJ02坐标系下，长沙市区内的住宅小区位置的经度
        - lat：GCJ02坐标系下，长沙市区内的住宅小区位置的纬度
        - name：住宅小区名称
    - BD09表
        - lng：BD09坐标系下，长沙市区内的住宅小区位置的经度
        - lat：BD09坐标系下，长沙市区内的住宅小区位置的纬度
        - name：住宅小区名称
3. [ArcGIS_warehouse.xlsx](dataSet/ArcGIS_warehouse.xlsx)（长沙市内的仓库位置的WGS84坐标）
    - WGS84表
        - lng：WGS84坐标系下，长沙市区内的仓库位置的经度
        - lat：WGS84坐标系下，长沙市区内的仓库位置的纬度
        - name：仓库名称
    - GCJ02表
        - lng：GCJ02坐标系下，长沙市区内的仓库位置的经度
        - lat：GCJ02坐标系下，长沙市区内的仓库位置的纬度
        - name：仓库名称
    - BD09表
        - lng：BD09坐标系下，长沙市区内的仓库位置的经度
        - lat：BD09坐标系下，长沙市区内的仓库位置的纬度
        - name：仓库名称
### 划出研究区域内的PoI数据。
为了限定研究范围，我们划定了长沙市区内一个矩形区域作为研究区域，该研究区域内的PoI数据如下：   
1. [ArcGIS_border.xlsx](dataSet/ArcGIS_border.xlsx)（划定的矩形研究区域的边界）
    - WGS84表
        - lng：WGS84坐标系下研究区域边界点的经度
        - lat：WGS84坐标系下研究区域边界点的纬度
2. [inborder_ArcGIS_company.xlsx](dataSet/inborder_ArcGIS_company.xlsx)（研究区域边界内的公司位置坐标）
    - WGS84表
        - lng：WGS84坐标系下，长沙市区内的公司位置的经度
        - lat：WGS84坐标系下，长沙市区内的公司位置的纬度
        - name：长沙市区内的公司名称
    - WGS84_in_border表
        - lng：WGS84坐标系下，研究区域内的公司位置的经度
        - lat：WGS84坐标系下，研究区域内的公司位置的纬度
        - name：研究区域内的公司名称
    - WGS84_inborder_filter表
        - lng：WGS84坐标系下，研究区域内经过随机过滤后，剩下的公司位置经度
        - lat：WGS84坐标系下，研究区域内经过随机过滤后，剩下的公司位置纬度
        - name：研究区域内经过随机过滤后，剩下的公司名称
    - GCJ02_inborder_filter表
        由于需要使用高德地图API计算从company到home的导航路径，所以需要将WGS84坐标系下的经纬度转换为GCJ02坐标系下的经纬度
        - lng：GCJ02坐标系下，研究区域内经过随机过滤后，剩下的公司位置经度
        - lat：GCJ02坐标系下，研究区域内经过随机过滤后，剩下的公司位置纬度
        - name：研究区域内经过随机过滤后，剩下的公司名称
3. [inborder_ArcGIS_home.xlsx](dataSet/inborder_ArcGIS_home.xlsx)（研究区域边界内的住宅小区位置坐标）
    - WGS84表
        - lng：WGS84坐标系下，长沙市区内的住宅小区位置的经度
        - lat：WGS84坐标系下，长沙市区内的住宅小区司位置的纬度
        - name：长沙市区内的住宅小区名称
    - WGS84_in_border表
        - lng：WGS84坐标系下，研究区域内的住宅小区位置的经度
        - lat：WGS84坐标系下，研究区域内的住宅小区位置的纬度
        - name：研究区域内的住宅小区名称
    - WGS84_inborder_filter表
        - lng：WGS84坐标系下，研究区域内经过随机过滤后，剩下的住宅小区位置经度
        - lat：WGS84坐标系下，研究区域内经过随机过滤后，剩下的住宅小区位置纬度
        - name：研究区域内经过随机过滤后，剩下的住宅小区名称
    - GCJ02_inborder_filter表
        由于需要使用高德地图API计算从company到home的导航路径，所以需要将WGS84坐标系下的经纬度转换为GCJ02坐标系下的经纬度
        - lng：GCJ02坐标系下，研究区域内经过随机过滤后，剩下的住宅小区位置经度
        - lat：GCJ02坐标系下，研究区域内经过随机过滤后，剩下的住宅小区位置纬度
        - name：研究区域内经过随机过滤后，剩下的住宅小区名称
4. [inborder_ArcGIS_warehouse.xlsx](dataSet/inborder_ArcGIS_warehouse.xlsx)（研究区域边界内的仓库位置坐标）
    - WGS84表
        - lng：WGS84坐标系下，长沙市区内的仓库位置的经度
        - lat：WGS84坐标系下，长沙市区内的仓库位置的纬度
        - name：长沙市区内的仓库名称
    - WGS84_in_border表
        - lng：WGS84坐标系下，研究区域内的仓库位置的经度
        - lat：WGS84坐标系下，研究区域内的仓库位置的纬度
        - name：研究区域内的仓库名称
    - WGS84_in_border_filter表
        - lng：WGS84坐标系下，研究区域内经过随机过滤后，剩下的仓库位置经度
        - lat：WGS84坐标系下，研究区域内经过随机过滤后，剩下的仓库位置纬度
        - name：研究区域内经过随机过滤后，剩下的仓库名称
    - GCJ02_in_border_filter表
        由于需要使用高德地图API计算从company到home的导航路径，所以需要将WGS84坐标系下的经纬度转换为GCJ02坐标系下的经纬度
        - lng：GCJ02坐标系下，研究区域内经过随机过滤后，剩下的仓库位置经度
        - lat：GCJ02坐标系下，研究区域内经过随机过滤后，剩下的仓库位置纬度
        - name：研究区域内经过随机过滤后，剩下的仓库名称
### 通勤车辆起止点及其路径数据
1. [commuting_route.xlsx](dataSet/commuting_route.xlsx)（车辆通勤的起止点）
    - GCJ02_origin_destination表
        该表通过[Routes.py](Routes.py)文件中的getCommuteRoutes()函数生成，该函数通过高德地图API计算从公司到住宅小区的导航路径，然后将导航路径上的点作为起止点数据。
        - lng_company：GCJ02坐标系下，公司位置经度
        - lat_company：GCJ02坐标系下，公司位置纬度
        - name_company：公司名称
        - lng_home：GCJ02坐标系下，住宅小区位置经度
        - lat_home：GCJ02坐标系下，住宅小区位置纬度
        - name_home：住宅小区名称
        - origin_fumula：起点坐标的excel公式表示
        - destination_fumula：终点坐标的excel公式表示
        - orign：起点坐标的文本表示
        - destination：终点坐标的文本表示
    - GCJ02_route_points表
        - lng：GCJ02坐标系下，公司到住宅小区导航路径上的点的经度
        - lat：GCJ02坐标系下，公司到住宅小区导航路径上的点的纬度
        - ID：公司到住宅小区导航路径的序号，公司到住宅小区的只记录最优的导航路径。
        - distance：导航路径的实际长度
        - duration：导航路径的预计行驶时间
    - WGS84_route_points表
        该表通过[transfer.py](transfer.py)文件中的transfer()函数生成，该函数通过高德地图API将GCJ02坐标系下的经纬度转换为WGS84坐标系下的经纬度。然后导入ArcGIS Pro中，使用点集转线工具生成通勤路径。
        - lng：WGS84坐标系下，公司到住宅小区导航路径上的点的经度
        - lat：WGS84坐标系下，公司到住宅小区导航路径上的点的纬度
        - ID：公司到住宅小区导航路径的序号，公司到住宅小区的只记录最优的导航路径。
        - distance：导航路径的实际长度
        - duration：导航路径的预计行驶时间
### 区域网格数据
1. [area_grid_seqtable.xlsx](area_grid_seqtable.xlsx)
    - area_grid_seq表
        该表需要用到ArcGIS Pro的线转点工具，将通勤路径转换为点，点的间隔距离为30m。
        - OBJECTID：通勤路径转点后的点序号（ArcGIS Pro自动生成）
        - Route_Flag：通勤路径经过点的标志（1：经过；0：未经过）
        - grid_uid：网格序号
        - FID_routes_Points_30m：线转点的30m间隔距离的点的序号
        - route_ID：通勤路径的序号
    - area_grid_seq_deduplicate表
        该表通过[neighbor_weight.py](neighbor_weight.py)中的area_grid_seq_deduplicate()函数，根据area_grid_seq表中route_ID和grid_uid字段去重，得到每条通勤路径依次经过的网格序号。
        - route_ID：通勤路径的序号
        - grid_uid：网格序号
    - neighbor_weight表
        该表通过[neighbor_weight.py](neighbor_weight.py)中的area_grid_seq_weight()函数，根据area_grid_seq_deduplicate表中route_ID和grid_uid字段，计算每条通勤路径经过的网格的邻域网格转移权重。
        - route_ID：通勤路径的序号
        - grid_uid_prev：通勤路径经过的上一个网格序号
        - grid_uid：通勤路径经过的当前网格序号
        - node_count：通勤路径经过的当前网格的邻域网格转移权重
2. [area_grid_Neighbors.xlsx](area_grid_Neighbors.xlsx)（网格邻域数据）
    - area_grid_Neighbors表
        该表通过ArcGIS Pro的Spatial Statistics Tools工具箱中的Generate Network Spatial Weights工具生成，该工具生成的网格邻域数据包含了网格的邻域网格ID、网格边界长度、邻域网格转移权重等信息。
        - OBJECTID：通勤路径经过的网格序号（ArcGIS Pro自动生成）
        - src_uid：自定义的网格序号
        - nbr_uid：邻域网格序号
        - src_Route_Flag：通勤路径经过的网格标志（1：经过；0：未经过）
        - nbr_Route_Flag：通勤路径经过的邻域网格标志（1：经过；0：未经过）
        - LENGTH：网格边界长度
        - NODE_COUNT：邻域网格转移权重
    - area_grid_Neighbors_route表
        该表通过[neighbor_weight.py](neighbor_weight.py)中的update_neighbor_weight()函数，按照路径经过的网格序号计算相邻网格的，与area_grid_Neighbors表不同，如果路径A按顺时针方向依次经过最小的田子网格1、2、3、4，area_grid_Neighbors表将认为网格1的邻域网格为2、4。而area_grid_Neighbors_route表将认为网格1的邻域网格只有网格2。
        - OBJECTID：通勤路径经过的网格序号（ArcGIS Pro自动生成）
        - src_uid：自定义的网格序号
        - nbr_uid：邻域网格序号
        - src_Route_Flag：通勤路径经过的网格标志（1：经过；0：未经过）
        - nbr_Route_Flag：通勤路径经过的邻域网格标志（1：经过；0：未经过）
        - LENGTH：网格边界长度
        - NODE_COUNT：邻域网格转移权重
### 物流任务数据
1. [logistics_task.xlsx](dataSet/logistics_task.xlsx)物流任务的起止点坐标和货物重量
    - WGS84_logistics_task_10表
        包含10个物流任务的任务集
        - task_id：任务序号
        - lng_origin_warehouse：WGS84坐标系下，起点仓库位置经度
        - lat_origin_warehouse：WGS84坐标系下，起点仓库位置纬度
        - name_origin_warehouse：起点仓库名称
        - lng_destination_warehouse：WGS84坐标系下，终点仓库位置经度
        - lat_destination_warehouse：WGS84坐标系下，终点仓库位置纬度
        - name_destination_warehouse：终点仓库名称
        - cargo_weight：货物重量
        - origin_grid：起点所在网格序号
            将起点坐标导入ArcGIS Pro，使用Spatial Join工具，将起点坐标与area_grid_seq_deduplicate表中的网格序号进行空间连接，得到起点所在网格序号
        - destication_grid：终点所在网格序号
            将终点坐标导入ArcGIS Pro，使用Spatial Join工具，将终点坐标与area_grid_seq_deduplicate表中的网格序号进行空间连接，得到终点所在网格序号
        - nearest_origin_grid_uid：起点所在网格序号的最近邻网格序号
        - nearest_destication_grid_uid：终点所在网格序号的最近邻网格序号
    - WGS84_logistics_task_20表
        包含20个物流任务的任务集
        - task_id：任务序号
        - lng_origin_warehouse：WGS84坐标系下，起点仓库位置经度
        - lat_origin_warehouse：WGS84坐标系下，起点仓库位置纬度
        - name_origin_warehouse：起点仓库名称
        - lng_destination_warehouse：WGS84坐标系下，终点仓库位置经度
        - lat_destination_warehouse：WGS84坐标系下，终点仓库位置纬度
        - name_destination_warehouse：终点仓库名称
        - cargo_weight：货物重量
        - origin_grid：起点所在网格序号
            将起点坐标导入ArcGIS Pro，使用Spatial Join工具，将起点坐标与area_grid_seq_deduplicate表中的网格序号进行空间连接，得到起点所在网格序号
        - destication_grid：终点所在网格序号
            将终点坐标导入ArcGIS Pro，使用Spatial Join工具，将终点坐标与area_grid_seq_deduplicate表中的网格序号进行空间连接，得到终点所在网格序号
        - nearest_origin_grid_uid：起点所在网格序号的最近邻网格序号
        - nearest_destication_grid_uid：终点所在网格序号的最近邻网格序号
2. [logistics_task_route.xlsx](dataSet/logistics_task_route.xlsx)物流任务的配送路径
    - logistics_task_10_route表
        包含10个物流任务的物流路径
        - task_id：任务序号
        - cargo_weight：货物重量
        - origin_grid_uid：起点所在网格序号
        - destication_grid_uid：终点所在网格序号
        - nearest_origin_grid_uid：起点所在网格序号的最近邻网格序号
        - nearest_destication_grid_uid：终点所在网格序号的最近邻网格序号
        - route：物流路径
    - logistics_task_20_route表
        包含20个物流任务的物流路径
        - task_id：任务序号
        - cargo_weight：货物重量
        - origin_grid_uid：起点所在网格序号
        - destication_grid_uid：终点所在网格序号
        - nearest_origin_grid_uid：起点所在网格序号的最近邻网格序号
        - nearest_destication_grid_uid：终点所在网格序号的最近邻网格序号
        - route：物流路径
3. 物流任务路径上的车辆序列