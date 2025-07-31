# Capstone Project: Slogan Classifier and Generator

## 📌 Project Overview

This project consists of two deep learning models trained on business slogans:

1. **Slogan Generator**:  
   A text-generation model using LSTM to create new, industry-specific slogans based on a given industry name.

2. **Slogan Classifier**:  
   A classification model that predicts the industry category of a business based on its slogan.

Both models were built using TensorFlow and trained on a cleaned dataset of real-world business slogans.

---

## 🧾 Dataset Description

- Source: A CSV file containing business slogans and their respective industries.
- Features:
  - `industry`: The sector or category of the business.
  - `output`: The slogan text.
- Preprocessing:
  - Removed null entries.
  - Filtered out industries with fewer than 2 slogans.
  - Used spaCy for text normalization and tokenization.
  - Added an industry prefix to each slogan for contextual slogan generation.

---

## 🛠️ Technologies Used

- Python 3.x  
- [TensorFlow 2.x](https://www.tensorflow.org/)  
- [spaCy](https://spacy.io/) (with `en_core_web_sm`)  
- NumPy, pandas  
- scikit-learn  

---

## 🧪 Methodology

### Preprocessing

- Text was lowercased and punctuation removed.
- Created a `processed_slogan` column.
- Prepended industry names to slogans to create `modified_slogan`.

### Slogan Generator

- Tokenized `modified_slogan` column into sequences.
- Created n-gram style inputs with progressively longer sequences.
- Padded all input sequences to uniform length.
- Built a Sequential LSTM model:
  - Embedding Layer
  - Two LSTM layers (150 + 100 units)
  - Dense output layer with softmax activation
- Trained for 50 epochs.

### Slogan Classifier

- Used `processed_slogan` column with complete padded sequences.
- One-hot encoded target industries.
- Built a similar Sequential LSTM model:
  - Embedding Layer
  - Two LSTM layers
  - Dense output layer predicting industry
- Trained and evaluated model performance on test data (20% split).

---

## 📈 Results & Evaluation

- **Slogan Generator**: Successfully generated industry-themed slogans. Some outputs were noisy due to dataset inconsistency.
- **Slogan Classifier**: Achieved ~19% accuracy — above random guess but with room for improvement.

### 🔍 Suggestions for Improvement

- Clean up noisy or inconsistent slogans in the dataset.
- Add dropout layers to reduce overfitting.
- Train longer or with more complex architectures.
- Use pre-trained word embeddings (e.g., GloVe).
- Apply temperature sampling or beam search for generation.

---

## 🧪 Example Usage

### Generate a Slogan

```python
industry = "internet"
generated_slogan = generate_slogan(industry)
print(generated_slogan)
