### How to start

```bash
cd flaskbook_api
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```
If you fail to install torch search appropriate version at [official site](https://pytorch.org/) and use it.

### Load model
```python
import torch
import torchvision
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
torch.save(model, "model.pt")
quit()
```

### Environment
* Ubuntu 18.04
* CPU only
* WSL2

### Usage
```bash
flask run
```