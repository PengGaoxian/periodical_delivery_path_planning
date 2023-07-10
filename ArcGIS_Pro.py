import arcpy

# 指定线要素图层名称
route_layer_name = "routes"
# 指定面要素图层名称
area_grid_layer_name = "area_grid"
# 指定导出表的输出路径和名称
output_table = r"output_table.dbf"

# 获取当前地图文档
aprx = arcpy.mp.ArcGISProject("C:/Users/Administrator/Documents/ArcGIS/Projects/长沙/长沙.aprx")

# 获取地图文档中的地图
map = aprx.listMaps()[0]

# 获取线要素图层
route_layer = map.listLayers(route_layer_name)[0]

# 获取面要素图层
area_grid_layer = map.listLayers(area_grid_layer_name)[0]

# 获取第一条线要素的几何形状
with arcpy.da.SearchCursor(route_layer, "SHAPE@") as cursor:
    first_line_shape = next(cursor)[0]

# 创建空间查询对象
# spatial_query = arcpy.SpatialReference(route_layer.spatialReference)
spatial_query = "{} INTERSECT".format(route_layer_name)

# 创建空间查询游标
with arcpy.da.SearchCursor(area_grid_layer, ["OID@", "SHAPE@"], spatial_query) as cursor:
    # 创建输出表
    arcpy.CreateTable_management(arcpy.env.workspace, arcpy.ValidateTableName(output_table))
    # 添加字段
    arcpy.AddField_management(output_table, "OID", "LONG")
    arcpy.AddField_management(output_table, "SHAPE", "GEOMETRY")
    # 创建插入游标
    with arcpy.da.InsertCursor(output_table, ["OID", "SHAPE"]) as insert_cursor:
        # 遍历相交的面要素并插入到输出表中
        for row in cursor:
            oid = row[0]
            shape = row[1]
            if shape.intersect(first_line_shape):
                insert_cursor.insertRow((oid, shape))
