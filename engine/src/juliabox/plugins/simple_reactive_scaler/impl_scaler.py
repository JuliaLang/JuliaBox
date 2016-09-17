from juliabox.cloud import JBPluginCloud
from juliabox.jbox_util import JBoxCfg

class SimpleReactiveScaler(JBPluginCloud):
    provides = [JBPluginCloud.JBP_SCALER, JBPluginCloud.JBP_SCALER_SIMPLE_REACTIVE]

    NAME = 'Simple Reactive Scaler'
    LOAD_TABLE = {80: 1}     # Default scaling logic

    @staticmethod
    def configure():
        SimpleReactiveScaler.LOAD_TABLE = JBoxCfg.get('cloud_host.scaler_config',
                                                      SimpleReactiveScaler.LOAD_TABLE)

    @staticmethod
    def get_name():
        return SimpleReactiveScaler.NAME

    @staticmethod
    def machines_to_add(avg_load):
        threshold = None
        keys = SimpleReactiveScaler.LOAD_TABLE.keys()
        keys.sort()
        for k in keys:
            if avg_load >= k:
                threshold = k
            else:
                break
        return SimpleReactiveScaler.LOAD_TABLE[threshold] if threshold else 0
