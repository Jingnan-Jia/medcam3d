# A library that generates the 3D CAM attention maps for 3D networks for 3D medical images




| Method              | What it does                                                                                                                |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------|
| GradCAM             | Weight the 3D activations by the average gradient                                                                           |



# Chosing the Target Layer
You need to choose the target layer to compute CAM for.
Some common choices are:
- FasterRCNN: model.backbone
- Resnet18 and 50: model.layer4[-1]
- VGG and densenet161: model.features[-1]
- mnasnet1_0: model.layers[-1]
- ViT: model.blocks[-1].norm1
- SwinT: model.layers[-1].blocks[-1].norm1

If you pass **a list with several layers**, the CAM will be **averaged** accross them.
This can be useful if you're not sure what layer will perform best.
However, it may be not wise to select multiple layers at once because the CAMs's values of shallow layers may be way smaller than the deeper layers (e.g. 1/10). So the shallower layers' CAM would be ignored.

----------

If this repository helps you in anyway, show your love ❤️ by putting a ⭐ on this project. 


