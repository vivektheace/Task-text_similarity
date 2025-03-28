import gradio as gr
from utils import predict_similarity

interface = gr.Interface(
    fn=predict_similarity,
    inputs=["text", "text"],
    outputs="number",
    title="Semantic Similarity Predictor",
    description="Enter two paragraphs to get a similarity score between 0 and 1 using SBERT."
)

if __name__ == "__main__":
    interface.launch()
