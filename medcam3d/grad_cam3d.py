import numpy as np
from medcam3d.base_cam import BaseCAM


class GradCAM(BaseCAM):
    def __init__(self, model, target_layers, use_cuda=False,
                 reshape_transform=None):
        super(
            GradCAM,
            self).__init__(
            model,
            target_layers,
            use_cuda,
            reshape_transform)

    def get_cam_weights(self,
                        input_tensor,
                        target_layer,
                        target_category,
                        activations,
                        grads):
        # shape of grads: n, c, z, y, x
        if len(grads.shape) == 5:  # 3d
            return np.mean(grads, axis=(2, 3, 4))  # shape: n, c
        else:  # 2d
            return np.mean(grads, axis=(2, 3))  # shape: n, c