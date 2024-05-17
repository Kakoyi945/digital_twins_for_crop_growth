import torch
import torch.nn as nn

class maize_gru_model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.encoder = nn.GRU(7,16,1,batch_first=True)
        self.decoder = nn.GRU(6,16,1,batch_first=True)
        self.out = nn.Sequential(
            nn.ReLU(),
            nn.Linear(16, 6)
        )

    def forward(self,inputs,inputs_):
        h0 = torch.randn(1,inputs.shape[0],16)
        _,h1 = self.encoder(inputs,h0)
        # h1 = torch.randn(2,inputs.shape[0],6)
        outputs,_ =  self.decoder(inputs_,h1)
        outputs = self.out(outputs)
        return outputs

class maize_lstm_model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.encoder = nn.LSTM(7,28,1,batch_first=True)
        self.decoder = nn.LSTM(6,28,1,batch_first=True)
        self.out = nn.Sequential(
            nn.ReLU(),
            nn.Linear(28, 6)
        )

    def forward(self,inputs, inputs_):
        h0 = torch.randn(1,inputs.shape[0],28)
        c0 = torch.randn(1,inputs.shape[0],28)
        _,(h1,c1) = self.encoder(inputs,(h0,c0))
        # outputs = self.out(hidden)
        # h1 = torch.zeros(1,inputs.shape[0],28)
        # c1 = torch.randn(1,inputs.shape[0],28)
        outputs,_ =  self.decoder(inputs_,(h1,c1))
        outputs = self.out(outputs)
        return outputs
    
class wheat_gru_model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.encoder = nn.GRU(7,8,1,batch_first=True)
        self.decoder = nn.GRU(6,8,1,batch_first=True)
        self.out = nn.Sequential(
            nn.ReLU(),
            nn.Linear(8, 6)
        )

    def forward(self,inputs,inputs_):
        h0 = torch.randn(1,inputs.shape[0],8)
        _,h1 = self.encoder(inputs,h0)
        # h1 = torch.randn(2,inputs.shape[0],6)
        outputs,_ =  self.decoder(inputs_,h1)
        outputs = self.out(outputs)
        return outputs

class wheat_lstm_model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.encoder = nn.LSTM(7,7,1,batch_first=True)
        self.decoder = nn.LSTM(6,7,1,batch_first=True)
        self.out = nn.Sequential(
            nn.ReLU(),
            nn.Linear(7, 6)
        )

    def forward(self,inputs, inputs_):
        h0 = torch.randn(1,inputs.shape[0],7)
        c0 = torch.randn(1,inputs.shape[0],7)
        _,(h1,c1) = self.encoder(inputs,(h0,c0))
        # outputs = self.out(hidden)
        # h1 = torch.zeros(1,inputs.shape[0],28)
        # c1 = torch.randn(1,inputs.shape[0],28)
        outputs,_ =  self.decoder(inputs_,(h1,c1))
        outputs = self.out(outputs)
        return outputs