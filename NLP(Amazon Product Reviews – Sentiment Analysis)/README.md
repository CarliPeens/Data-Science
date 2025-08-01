# 📦 Amazon Product Reviews – Sentiment Analysis

This project performs sentiment analysis on Amazon product reviews using the `spaCy` NLP library and the `spacytextblob` extension. The goal is to classify the sentiment polarity of reviews as positive, negative, or neutral, and to derive insights from the review data.

---

## 📑 Project Structure

```
📁 sentiment-analysis/
│
├── sentiment_analysis.ipynb   # Main Jupyter notebook for sentiment analysis
├── Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv   # Review dataset
└── README.md                  # Project documentation
```

---

## 📚 Dataset Description

- **Source**: Kaggle – Datafiniti’s Amazon Consumer Reviews
- **File**: `Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv`
- **Size**: ~23,000 reviews
- **Features**:
  - `reviews.text`: The content of the review
  - `reviews.rating`: Star rating (1–5)
  - `brand`, `manufacturer`, and other metadata

---

## 🔍 Project Objectives

1. Load and clean Amazon product review data
2. Perform sentiment analysis using `spaCy` and `spacytextblob`
3. Visualize sentiment distribution and review polarity
4. Provide insights about product perception based on reviews

---

## 🛠️ Tools and Libraries Used

- `pandas` – data handling
- `spaCy` – core NLP processing
- `spacytextblob` – sentiment polarity analysis
- `matplotlib`, `seaborn` – data visualization
- `re` – text preprocessing

---

## ⚙️ Setup Instructions

1. **Clone the repository or download the notebook**
2. **Install required libraries**:

```bash
pip install pandas matplotlib seaborn spacy spacytextblob
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

3. **Enable `spacytextblob` in spaCy pipeline**:

```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
```

---

## 🔄 Preprocessing Steps

- Removed missing or null reviews
- Normalized text: lowercase, removed special characters
- Tokenized and lemmatized text (optional for further improvement)
- Extracted sentiment polarity and subjectivity for each review

---

## 📊 Results Summary

- Reviews with higher star ratings mostly exhibit positive sentiment polarity
- Negative reviews are more prominent in 1–2 star ratings
- Neutral sentiment occurs in factual or short reviews

---

## 🔍 Insights

- Most products have overwhelmingly positive reviews
- Some brands receive mixed sentiment regardless of rating
- Reviews can show sentiment discrepancies with actual ratings (e.g., positive tone with low rating due to delivery issues)

---

## 🚧 Limitations and Improvements

### Limitations
- `spacytextblob` provides basic polarity classification
- Subtle or sarcastic language may be misclassified
- No deep learning or contextual language modeling

### Possible Improvements
- Use transformer-based models (e.g., BERT or RoBERTa)
- Add sentiment explanation or keyword attribution
- Train a custom sentiment classifier on labeled data

---

## 📈 Sample Visualization

The notebook includes:
- Polarity distribution histogram
- Sentiment vs. Rating scatterplot
- Word clouds for positive and negative reviews

---

## 📌 License

This project is for educational purposes only.  
Dataset © Datafiniti (via Kaggle)
