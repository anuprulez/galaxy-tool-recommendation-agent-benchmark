from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F


# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[
        0
    ]  # First element of model_output contains all token embeddings
    input_mask_expanded = (
        attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    )
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
        input_mask_expanded.sum(1), min=1e-9
    )


def get_sentence_embeddings(sentences):
    pred_embed = list()
    # Load model from HuggingFace Hub
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

    # Tokenize sentences
    for sentence in sentences:
        encoded_input = tokenizer(
            sentence, padding=True, truncation=True, return_tensors="pt"
        )
        with torch.no_grad():
            model_output = model(**encoded_input)
        sentence_embeddings = mean_pooling(
            model_output, encoded_input["attention_mask"]
        )
        sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)
        pred_embed.append(sentence_embeddings[0].tolist())
    return pred_embed
