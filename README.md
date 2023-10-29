# torch_hub_test
This is a test github repository created to show how to use Torch Hub to Load and Save Models

### To Load model from Torch Hub
```>>> import torch
>>> model = torch.hub.load('atifadib/torch_hub_test', 'model', pretrained=True, trust_repo=True)
Downloading: "https://github.com/atifadib/torch_hub_test/zipball/main" to /Users/atifadib/.cache/torch/hub/main.zip
Downloading: "https://github.com/atifadib/torch_hub_test/raw/main/model_resources/model_v1.pth" to /Users/atifadib/.cache/torch/hub/checkpoints/model_v1.pth
100.0%
>>>``` 
