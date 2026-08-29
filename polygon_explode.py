from qgis.core import QgsApplication

from .processing_provider.provider import PolygonExplodeProvider


class PolygonExplodePlugin:

    def __init__(self, iface):
        self.iface = iface
        self.provider = None

    def initGui(self):
        self.provider = PolygonExplodeProvider()

        QgsApplication.processingRegistry().addProvider(
            self.provider
        )

    def unload(self):
        if self.provider is not None:

            QgsApplication.processingRegistry().removeProvider(
                self.provider
            )

            self.provider = None