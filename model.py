import torch.nn as nn
from torch.hub import load_state_dict_from_url

model_urls = {
	'model': ""
}

class MyModel(nn.Module):
	def __init__(self):
		super(MyModel, self).__init__()
		self.fc1 = nn.Linear(2, 2)
		self.fc2 = nn.Linear(2, 1)

	def forward(self, x):
		x = nn.functional.relu(self.fc1(x))
		x = nn.functional.sigmoid(self.fc2(x))
		return x

def load_model(pretrained=True, progress=True, **kwargs):
	model = MyModel(**kwargs)
	if pretrained:
		state_dict = load_state_dict_from_url(model_urls['model'], progress=progress)
		model.load_state_dict(state_dict)
	return model

