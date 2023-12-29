# Movie Recommendation app using cosine similarity
* Dataset used: https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k
* Uses streamlit

# General steps:

## 1) Data Preprocessing:
* Ensure that your dataset is clean and handle any missing values if necessary.

## 2) Feature Engineering:
* Use CountVectorizer on the "genre" and "overview" columns to convert them into numerical representations.

## 3) Creating a Feature Matrix:
* Concatenate the numerical representations obtained from CountVectorizer with other relevant numerical features to create a feature matrix.

## 4)  Cosine Similarity:
* Calculate the cosine similarity between movies based on their feature matrix. This can be done using the cosine similarity function from scikit-learn or other libraries.
  
## 5) Recommendation Generation:
* Identify top 5 movies with the highest cosine similarity to the user's movie selection as top recommendations.

## Streamlit-app:
![image](https://github.com/ongaunjie1/movie-recommendation-app/assets/118142884/8b44a087-c905-4a84-92c3-1621f8bea108)
