import os
import requests
from bs4 import BeautifulSoup

# URL which contains the pictures of all Pokemon
url = "https://pokemondb.net/pokedex/national"

def fetch_and_save_images(gen_number, image_url, image_name):
    """
    Fetches the image from the given URL and saves it in a folder named after the generation number.

    :param gen_number: The generation number of the Pokemon
    :param image_url: The URL of the image
    :param image_name: The name of the Pokemon
    """
    folder_name = f"./data/Generation_{gen_number}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    image_data = requests.get(image_url).content
    image_path = os.path.join(folder_name, f"{image_name}.jpg")

    with open(image_path, 'wb') as file:
        file.write(image_data)
    print(f"Saved {image_name} in {folder_name}")

# Fetch the HTML content of the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
i = 0

# Find all h2 tags which contain the generations numbers
for generation in soup.find_all("h2"):
    gen_id = generation.get("id")
    if gen_id and gen_id.startswith("gen-"):
        gen_number = gen_id.split("-")[1]

        # Find the next div tag with the class "infocard-list"
        infocard_list = generation.find_next("div", class_="infocard-list")

        if infocard_list:
            infocards = infocard_list.find_all("div", class_="infocard")
            for infocard in infocards:
                # Find the img tag which contains the image URL and the name of the Pokemon
                image_tag = infocard.find("img", class_="img-fixed img-sprite")
                image_url = image_tag["src"]
                image_name = image_tag["alt"]

                # Fetch and save the image
                fetch_and_save_images(gen_number, image_url, image_name)
                i += 1

print(f"Succefully fetched {i} images!")
