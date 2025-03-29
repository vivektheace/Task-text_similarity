**GRADIO LIVE ENDPOINT - https://huggingface.co/spaces/vivekdace/semantic-similarity-app
FASTAPI LIVE ENDPOINT - https://text-similarity-model-uwpv.onrender.com/docs
**
# Assignment **Report: Semantic Similarity Model & Deployment**

## Part A: Core Modeling Approach

The task required building an algorithm that can determine the semantic similarity between two given paragraphs and output a score between **0 and 1**, where 1 denotes high semantic similarity.

To address this, we utilized the **Sentence-BERT (SBERT)** model, specifically the `'all-MiniLM-L6-v2'` variant from the `sentence-transformers` library. SBERT extends the capabilities of BERT by enabling direct and efficient comparison between sentence embeddings using cosine similarity.

### Why SBERT?

- **Context-aware embeddings**: Unlike traditional techniques (e.g., TF-IDF or Bag-of-Words), SBERT captures the **meaning** of a sentence, not just keyword overlap.
- **Optimized for similarity tasks**: SBERT is specifically fine-tuned for semantic textual similarity, outperforming vanilla BERT in this use case.
- **No need for labeled data**: Since the provided dataset had no labels, we used SBERT in an **unsupervised** setting, leveraging cosine similarity between encoded embeddings.
- **Speed and efficiency**: The `MiniLM` variant offers a strong trade-off between performance and inference speed, which is ideal for API deployment.

### Functionality

We created a `predict_similarity(text1, text2)` function that:

1. Cleans and lowercases both inputs.
2. Generates embeddings using SBERT.
3. Computes the cosine similarity between them.
4. Returns a float score between 0 and 1.

## Part B: API Deployment Approach

The final model was deployed in two formats to demonstrate both frontend and backend readiness:

### Gradio UI (via Hugging Face Spaces)

- A web-based interactive interface was built using **Gradio** and hosted on **Hugging Face Spaces**.
- This allows users to input two paragraphs and instantly get a similarity score.
- URL: [https://vivekdace-semantic-similarity-app.hf.space](https://vivekdace-semantic-similarity-app.hf.space/)

### FastAPI Endpoint (Optional Extension)

- For backend integration, the same core logic was packaged into a FastAPI app.
- This enables programmatic access via HTTP POST requests with JSON input/output.
- The modular design allows the same model logic (`utils.py`) to be reused by both interfaces.

## Conclusion

The SBERT-based solution offered a robust, production-ready approach to semantic similarity without the need for supervised training. Both deployment options (Gradio and FastAPI) demonstrate the model's flexibility and ease of integration in real-world systems.
