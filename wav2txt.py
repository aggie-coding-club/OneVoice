import IPython
import torch
import torchaudio

def transcript(file_location):
    class GreedyCTCDecoder(torch.nn.Module):
        def __init__(self, labels, blank=0):
            super().__init__()
            self.labels = labels
            self.blank = blank

        def forward(self, emission: torch.Tensor) -> str:
            """Given a sequence emission over labels, get the best path string
            Args:
            emission (Tensor): Logit tensors. Shape `[num_seq, num_label]`.

            Returns:
            str: The resulting transcript
            """
            indices = torch.argmax(emission, dim=-1)  # [num_seq,]
            indices = torch.unique_consecutive(indices, dim=-1)
            indices = [i for i in indices if i != self.blank]
            return "".join([self.labels[i] for i in indices])

    torch.random.manual_seed(0)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    #print(torch.__version__)
    #print(torchaudio.__version__)
    #print(device)

    SPEECH_FILE = file_location


    bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H

    #print("Sample Rate:", bundle.sample_rate)

    #print("Labels:", bundle.get_labels())

    model = bundle.get_model().to(device)

    #print(model.__class__)


    IPython.display.Audio(SPEECH_FILE)

    waveform, sample_rate = torchaudio.load(SPEECH_FILE)

    waveform = waveform.to(device)

    if sample_rate != bundle.sample_rate:
        waveform = torchaudio.functional.resample(
            waveform, sample_rate, bundle.sample_rate)

    with torch.inference_mode():
        features, _ = model.extract_features(waveform)
        emission, _ = model(waveform)

    decoder = GreedyCTCDecoder(labels=bundle.get_labels())
    return str(decoder(emission[0])).replace("|", " ")
