# 🔍 Quote Search Engine

This project is a simple web application that functions like a search engine. It allows users to input a query, processes the input using **TF-IDF** and **cosine similarity**, and returns the most relevant results from a dataset.

## 🌟 Features

- **Search Engine Functionality**: Users can enter queries, and the app retrieves relevant results based on similarity scoring.
- **TF-IDF Vectorization**: The app computes the importance of words in the dataset using TF-IDF (Term Frequency-Inverse Document Frequency).
- **Cosine Similarity**: The app ranks search results by calculating cosine similarity between the query and dataset entries.
- **Frontend**: A simple, user-friendly interface built with HTML, CSS, and JavaScript.
- **Backend**: Python scripts handle data processing and similarity computations.

## 🚀 How It Works

1. **Dataset Processing**  
   - The dataset is processed using `process_data.py` to generate TF-IDF vectors.  
   - These vectors are saved in `processed_quotes.pkl` for efficient querying.

2. **Search Query**  
   - Users enter a search query in the frontend.  
   - The query is sent to the backend (`main.py`), where it is processed.  
   - Cosine similarity is computed between the query vector and dataset vectors.  
   - Results are ranked by relevance and displayed on the frontend.

## 🌐 Deployment

### Frontend
The frontend (`index.html`, `style.css`, `script.js`) can be deployed using [Vercel](https://vercel.com/).

### Backend
The backend (`main.py` and `processed_quotes.pkl`) requires a Python runtime and can be deployed using:
- [Render](https://render.com/)
- [Heroku](https://www.heroku.com/)
- [AWS Lambda](https://aws.amazon.com/lambda/) + API Gateway

---

## 📝 Example Queries

- **Query**: "machine learning"  
  **Results**: Displays dataset entries related to machine learning.  
- **Query**: "artificial intelligence"  
  **Results**: Returns relevant entries ranked by similarity.

---

## 🤔 Future Enhancements

- **Pagination**: Add pagination for long result lists.  
- **Better UI**: Improve the design and user experience of the frontend.  
- **Dataset Upload**: Allow users to upload their own datasets for custom searches.  
- **Cloud Deployment**: Integrate with cloud platforms for real-time performance.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes.

---


## 💬 Contact

If you have any questions or feedback, feel free to open an issue or reach out.
