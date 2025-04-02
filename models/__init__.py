from models.efficientnet import EfficientNetV2
from models.multiview_efficientnet import MultiviewEfficientNetV2

def get_model(config, **kwargs):
    name = config['model']
    if name == "efficientnet":
        return EfficientNetV2(**kwargs)
    elif name == "multiview_efficientnet":
        return MultiviewEfficientNetV2(**kwargs)
    else:
        raise ValueError(f"Unknown model name: {name}")