# GAN Powered Pokémon Generation

This project is part of **Lernziel 3** from the 6th Semester course **Deep Reinforcement Learning und Generative Verfahren**. The goal is to create a Generative Adversarial Network (GAN) trained on self-crawled images of Pokémon to explore the feasibility of generating new, "artificial" Pokémon. The dataset used consists of images from the Pokédex up to and including Generation 8, which can be found at [Pokémon Database](https://pokemondb.net/pokedex/national).

## Project Structure

- **crawler/**

  - Contains the crawler for scraping Pokémon images from the Pokémon Database.
  - **crawler.py**: The main script used to crawl images.

- **data/**

  - Contains the images crawled from the Pokémon Database.
  - **image_mover.py**: This script copies all images into a single directory, preparing them for GAN training.

- **lab/**

  - Contains notebooks for data analysis and GAN training.
  - **data_analysis.ipynb**: A Jupyter notebook that analyzes the dataset to prepare for network architecture design and checks the input size of the images.
  - **gan_powered_pokemon_generation.ipynb**: The main Jupyter notebook containing the GAN training code and the network structure, which is based on the paper:
    - _Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks_ by Alec Radford, Luke Metz (indico Research), and Soumith Chintala (Facebook AI Research).

- **time_lapse_creator.py**
  - A Python script that generates a timelapse of the samples created every 10 epochs, providing an overview of the training process.

## Setting up the project

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Jupyter Notebook
- TensorFlow or PyTorch (keep your specific CUDA version in mind if you want to retrain the model)
- Other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/GAN-powered-pokemon-generation.git
   cd GAN-powered-pokemon-generation
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## References

- **Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks** by Alec Radford, Luke Metz, and Soumith Chintala. Available [here](https://arxiv.org/abs/1511.06434).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
