[Generative AI](https://developers.google.com/machine-learning/glossary#generative-ai) is a class of models that creates content from user input. For example, generative AI can create unique images, music compositions, and jokes; it can summarize articles, explain how to perform a task, or edit a photo.

Generative AI can take a variety of inputs and create a variety of outputs, like text, images, audio, and video. It can also take and create combinations of these. For example, a model can take an image as input and create an image and text as output, or take an image and text as input and create a video as output.

We can discuss generative models by their inputs and outputs, typically written as "type of input"-to-"type of output." For example, the following is a partial list of some inputs and outputs for generative models:

- Text-to-text
- Text-to-image
- Text-to-video
- Text-to-code
- Text-to-speech
- Image and text-to-image

The following table contains examples of generative models, their input, and their possible output:

|Model|Input|Example output|
|---|---|---|
|Text-to-text|Who invented the Le Mans race?|The 24 Hours of Le Mans was founded by the Automobile Club de l'Ouest (ACO), a motoring organization founded in 1906. The first race was held on 26 and 27 May 1923 on the Sarthe Circuit, a 13.426-kilometre (8.345-mile) road circuit located near the town of Le Mans in France. The race was originally conceived as a way to promote the ACO and the Sarthe region.  <br>Source: [Bard](https://bard.google.com/)|
|Text-to-image|An alien octopus floats through a portal while reading a newspaper.|![Image of a cartoon octopus.](https://developers.google.com/static/machine-learning/intro-to-ml/images/octopus.png)  <br>Source: [Imagen](https://imagen.research.google/)|
|Text-to-video|A photorealistic teddy bear is swimming in the ocean at San Francisco. The teddy bear goes under water. The teddy bear keeps swimming under the water with colorful fishes. A panda bear is swimming under water.|![Video of a teddy bear swimming underwater.](https://developers.google.com/static/machine-learning/intro-to-ml/images/teddy_bear.gif)  <br>Source: [Phenaki](https://phenaki.video/)|
|Text-to-code|Write a Python loop that loops over a list of numbers and prints the prime numbers.|for number in numbers:<br>  # Check if the number is prime.<br>  is_prime = True<br>  for i in range(2, number):<br>    if number % i == 0:<br>        is_prime = False<br>        break<br>  # If the number is prime, print it.<br>  if is_prime:<br>    print(number)<br><br>  <br>Source: [Bard](https://bard.google.com/)|
|Image-to-text|![Image of a flamingo.](https://developers.google.com/static/machine-learning/intro-to-ml/images/flamingo.png)|This is a flamingo. They are found in the Caribbean.  <br>Source: [Google DeepMind](https://www.deepmind.com/blog/tackling-multiple-tasks-with-a-single-visual-language-model)|

How does generative AI work? At a high-level, generative models learn patterns in data with the goal to produce new but similar data. Generative models are like the following:

- Comedians who learn to imitate others by observing people's behaviors and style of speaking
- Artists who learn to paint in a particular style by studying lots of paintings in that style
- Cover bands that learn to sound like a specific music group by listening to lots of music by that group

To produce unique and creative outputs, generative models are initially trained using an unsupervised approach, where the model learns to mimic the data it's trained on. The model is sometimes trained further using supervised or reinforcement learning on specific data related to tasks the model might be asked to perform, for example, summarize an article or edit a photo.

Generative AI is a quickly evolving technology with new use cases constantly being discovered. For example, generative models are helping businesses refine their ecommerce product images by automatically removing distracting backgrounds or improving the quality of low-resolution images.