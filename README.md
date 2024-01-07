# Ai_Projects___Topic_and_Code_Explained

* This `Public Template` repository consists of all of [@sanskarGupta551](https://github.com/sanskarGupta551)'s Projects since `Year 2022`.

* All Projects will have -
    1. A `Jupyter Notebook` Explaining the Topic and the Code Implementation, `and`
    2. `End Results` in the form of Python Scripts, Apps, Images or Video Links `if possible`.

## A. Computer Vision 

* This section consists of Projects built with the purpose of `Learning and Understanding` Applications of `Computer Vision` to solve Real World Problems.

1. [Face_Mask_Detection_with_VGG16](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Computer_Vision___Face_Mask_Detection_with_VGG16/Face_Mask_Detection_with_VGG16.ipynb)

* `Face Mask Detection` is a system that uses `Computer Vision` and Deep Learning to determine whether a person is wearing a `mask` or not.
* Here, we Build a `Face Mask Detection` model using `CNNs`(Convolutional Neural Networks) and a [VGG16](https://www.tensorflow.org/api_docs/python/tf/keras/applications/vgg16/VGG16) base, then Train it using `Transfer Learning` on our Dataset.
* At last, we load the `Best Model` saved using our pre-defined `Callback` and `Test` our model on `Unseen Data`.
* `Dataset` - [Face Mask Detection ~12K Images Dataset](https://www.kaggle.com/datasets/ashishjangra27/face-mask-12k-images-dataset) from Kaggle.

![Image](https://www.intertecsystems.com/wp-content/uploads/2020/05/face-mask-detection-software-e1591538656411.png)

2. [Facial_Emotion_Recognition_with_VGG16](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Computer_Vision___Facial_Emotion_Recognition_with_VGG16/Facial_Emotion_Recognition_with_VGG16.ipynb)

* `Facial Emotion Recognition` (FER) is a subfield of Facial Recognition that involves `identifying` and categorizing `Human Emotions` based on Facial expressions.
* Here, we Build a `Facial Emotion Recognition` model by loading the [VGG16](https://www.tensorflow.org/api_docs/python/tf/keras/applications/vgg16/VGG16) base trained on `Imagenet` without thr Top layer, `Adapt` it to our current problem, and Train it using `Transfer Learning` on our Dataset. 
* Then, we load the `Best Model` saved using our pre-defined `Callback` and `Test` our model on a few `Images`.
* At last, we test our Model on `Videos` with added complexity of [Haar Cascade](https://docs.opencv.org/3.4/d2/d99/tutorial_js_face_detection.html) to improve `Model Accuracy`.
* `Dataset` - [FER2013 Dataset](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data) from Kaggle.

![Image](https://i.pinimg.com/originals/b0/bb/1d/b0bb1d0b86bdca1de8ead928064d09d8.png)

3. [Fashion_MNIST_with_CNN(s)](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Computer_Vision___Fashion_MNIST_with_CNN(s)/Fashion_MNIST_with_CNN(s).ipynb)

* [Fashion MNIST](https://keras.io/api/datasets/fashion_mnist/) is a `Image Classification` dataset with `28x28` grayscale images of `10` Fashion categories.
* This is a classic `Computer Vision` problem, often one of the first projects built by any `Computer Vision` enthusiast.
* Here, we will build a` Deep Learning model` using `Convolutional Neural Networks (CNNs)` to solve this Image Classification problem.
* `Dataset` - [Fashion MNIST](https://keras.io/api/datasets/fashion_mnist/) from Keras.

![Image](https://thiagolcmelo.github.io/assets/img/fashion-mnist.png)

4. [Green_Screening_Images_and_Videos_with_OpenCV](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Computer_Vision___Green_Screening_Images_and_Videos_with_OpenCV/Green_Screening_Images_and_Videos_with_OpenCV.ipynb)

* `Green Screening` is a technique that allows you to place any `Background` picture you want `behind` the performers or the `Foreground`.
* Here, we first `Understand` how `Green Screening` works with the help of a `Computer Vision` library [OpenCV](https://opencv.org/) using different `Images` as Foreground and Background.
* Then, we will perform `Green Screening` of a `Video` of `Steve Dancing` with a few different `Videos` sewed together as Background. 
* `Dataset` - `None`.

![Image](https://i.ytimg.com/vi/JfyzwWgZT4M/maxresdefault.jpg)

5. [Image_Captioning_with_Flickr30k](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Computer_Vision___Image_Captioning_with_Flickr30k/Image_Captioning_with_Flickr30k.ipynb)

* `Image Captioning` is the task of `describing` the content of an `Image` in words.
* Here, we build an `Encoder Model` using `LSTM` (Long-Short Term Memory), which is a type of `RNN` (Recurrent Neural Network), and `Train` it on our pre-processed Dataset.
* At last, we `Test` this Model on a few `Unseen Images`.
* `Dataset` - [Flickr30k](https://www.kaggle.com/datasets/eeshawn/flickr30k/data)

![Image](https://petapixel.com/assets/uploads/2016/09/Caption1-800x450.jpg)

6. [Image_Deblurring_with_VGG16](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Computer_Vision___Image_Deblurring_with_VGG16/Image_Deblurring_with_VGG16.ipynb)

* `Image Deblurring` is a process of `restoring` a sharp image from a `blurred` input `Image`.
* Here, we first `Build` a Mixed Blur `Dataset` from `Scratch`.
* Then we build a Model using [VGG16](https://www.tensorflow.org/api_docs/python/tf/keras/applications/vgg16/VGG16) and `Train` it on our Dataset.
* At last, we will `Evaluate Accuracy` of our Model and `Test` it on a few `Images`.
* `Dataset` - `Built from Scratch`.

![Image](https://th.bing.com/th/id/R.1c95a17451c44bb937d2275bc6ae14d9?rik=FClK479meeWRPA&riu=http%3a%2f%2fwww.ece.northwestern.edu%2flocal-apps%2fmatlabhelp%2ftoolbox%2fimages%2fdeblu10a.gif&ehk=VTBAkwI%2bK%2b2lqG5JtdUoByh24GOJfmcoo8RGX8xAyiY%3d&risl=&pid=ImgRaw&r=0)

## B. Natural Language Processing

* This section consists of Projects built with the purpose of `Learning and Understanding` Applications of `Natural Language Processing` to solve Real World Problems.

1. [GenZ_Tweets_Data_Pipeline_for_Sentiment_Analysis](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/NLP___GenZ_Tweets_Data_Pipeline_for_Sentiment_Analysis/GenZ_Tweets_Data_Pipeline_for_Sentiment_Analysis.ipynb)

* 
* `Dataset` - `None`.

![Image](https://i.pinimg.com/originals/e1/d0/33/e1d0330eb3bfd698f6c332e0d61f6d11.png)

2. [Next_Word_Prediction_with_Bidirectional_LSTM](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/NLP___Next_Word_Prediction_with_Bidirectional_LSTM/Next_Word_Prediction_with_Bidirectional_LSTM.ipynb)

* 

3. [Prompt_to_Synopsis_Generator_(using_Transfer_Learning)](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/NLP___Prompt_to_Plot_Summary_Generator/Prompt_to_Synopsis_Generator_(using_Transfer_Learning).ipynb)

* 

4. [Tweets_Sentiment_Analysis_with_3_Neural_Network](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/NLP___Tweets_Sentiment_Ananlysis_with_3_Neural_Networks/Tweets_Sentiment_Analysis_with_3_Neural_Network.ipynb)

* 

## C. Theory Notebooks

* 

1. [Ai_Imagining_Stories_from_Images](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Theory_Notebooks/Ai_Imagining_Stories_from_Images.ipynb)

* 

2. [Ai_Long_form_Story_Generator_with_Varied_Context](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Theory_Notebooks/Ai_Long_form_Story_Generator_with_Varied_Context.ipynb)

* 

3. [AutoML___A_Brief_Introduction](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/blob/main/Theory_Notebooks/AutoML___A_Brief_Introduction.ipynb)

* 

## D. Upcoming Projects

* 

1. [(Building)Portfolio_Project___Authentic_Audience](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/tree/main/(Building)Portfolio_Project___Authentic_Audience)

* 

## E. Future Projects


1. [Computer_Vision___Ingredient_to_Recipe_Search_Engine](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/tree/main/Upcoming_Projects/Computer_Vision___Ingredient_to_Recipe_Search_Engine)

* 

2. [Computer_Vision___Ai_Multi_media_Generator](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/tree/main/Upcoming_Projects/Computer_Vision___Ai_Multi_media_Generator)

* 

3. [Computer_Vision___Face_Swapper](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/tree/main/Upcoming_Projects/Computer_Vision___Face_Swapper)

* 

4. [NLP___Long_form_Story_Generator_using_Deep_Learning](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/tree/main/Upcoming_Projects/NLP___Long_form_Story_Generator_using_Deep_Learning)

* 

5. [Computer_Vision___Ai_Comic_Generator](https://github.com/sanskarGupta551/Ai_Projects___Topic_and_Code_Explained/tree/main/Upcoming_Projects/Computer_Vision___Ai_Comic_Generator)

* 

