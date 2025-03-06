import numpy as np
import tensorflow as tf
from transformers import BertTokenizer, BertModel
import torch
from collections import Counter
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
tf.config.set_visible_devices([], 'GPU')


# Configuración inicial: modelo BERT y cargamos el modelo clasificador guardado
model_name = "bert-base-multilingual-cased"  # O 'bert-base-multilingual-cased' para español
tokenizer = BertTokenizer.from_pretrained(model_name)
bert_model = BertModel.from_pretrained(model_name)

# Seleccionar dispositivo: usar MPS si está disponible, sino CPU
device = torch.device("cpu")
bert_model.to(device)

# Cargar el modelo clasificador (Keras)
modelo = tf.keras.models.load_model("modelo_clasificador.keras")

# Diccionario de clases (modifícalo según corresponda)
topic_to_label = {
    "Medicina": 0,
    "Economia": 1,
    "Motor": 2,
    "Deportes": 3,
    "Religion": 4,
    "Militar": 5,
    "Politica": 6,
    "Ocio": 7,
    "Moda": 8,
    "Informatica": 9,
    "Astronomia": 10,
    "Alimentacion": 11
}
# Invertir el diccionario para obtener nombres a partir del índice
label_to_topic = {v: k for k, v in topic_to_label.items()}

def get_bert_embedding(text, max_length=512):
    """
    Toma un texto y devuelve el embedding del token [CLS] de BERT,
    utilizando MPS si está disponible.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
    # Mover todos los tensores al dispositivo seleccionado (MPS o CPU)
    inputs = {key: value.to(device) for key, value in inputs.items()}
    outputs = bert_model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :]
    # Regresamos el embedding en CPU como numpy array
    return cls_embedding.detach().cpu().numpy()  # Forma: (1, 768)

def predict_class(text):
    """
    Dado un texto, obtiene su embedding y usa el modelo para predecir la clase.
    Retorna el índice de la clase y el nombre correspondiente.
    """
    embedding = get_bert_embedding(text)  # (1, 768)
    pred_probs = modelo.predict(embedding)
    pred_class = int(np.argmax(pred_probs, axis=1)[0])
    return pred_class, label_to_topic.get(pred_class, "Desconocido")
def retorn_class(text):
    clase_idx, clase_nombre = predict_class(text)
    return clase_nombre
