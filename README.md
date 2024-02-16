# movie-recommender
Hi everyone, this is my side project which is basically a movie-recommendation webapp I made using django framework.
[https://moviehome.co.in](url)

# overview
You can search any movie(before 2017) on search bar and if you find your movie in search results then you can simply click on it and here you are at the webpage which contains 40 movies that you will find most similar to your searched movie 
# Dataset
The dataset is of 13000 movies whose columns are :
'Release Year'
'Title'
'Cast'
'Wiki Page'
'Plot'
'plot_length'
'text'
'embeddings'
'Poster'
[https://huggingface.co/datasets/vishnupriyavr/wiki-movie-plots-with-summaries-faiss-embeddings](url)

# working
I took inspiration of this project from Andrej Karpathy's project awesome-movie.life which is just the same except his movie dataset is new. So here is how this works 
1. The similar movies are sorted on the basis of vector embeddings which are created using openai embedding api , if you don't know the embeddings this is a vector of around ~ 800 dimensions which is kind of representation of the movie summery but in numbers so that computer can easily find similar movies
2. Each 13000 movie in dataset has it's unique vector embeddings and based on that we can easily find similar movies using a method called cosine similaritis which is available in scikit-learn.
3. The cosine similarity matrix is a matrix of dimensions (13000*13000) here each row is 13000 dimension vector and it signifies the most similar movie index in decreasing order . for example the 1st row's 1st element is the 1st movie of the dataset because it is the most similar movie the itself and likewise the 2nd element is the movie which is most similar to it after that and so on
4. so now it's pretty easy I used first 40 similar movie indices from the cosine matrix and used them to list on my website hence it shows the 40 top similar movie to the given movie


