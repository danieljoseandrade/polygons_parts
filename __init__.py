def classFactory(iface):
    from .polygon_explode import PolygonExplodePlugin
    return PolygonExplodePlugin(iface)