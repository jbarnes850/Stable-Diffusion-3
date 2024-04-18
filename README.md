# Stable Diffusion 3 Text-to-Image Generator

This is a Python application that utilizes the Stable Diffusion 3 model to generate images from textual prompts. It provides a user-friendly interface built with Gradio, allowing users to enter a prompt, select a model, and choose an aspect ratio to generate an image.

## Requirements

To run this application, you need to have the following dependencies installed:

- requests
- requests-toolbelt
- gradio

You can install these dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using the command mentioned above.
3. Replace the `api_key` variable in the `SD3.py` file with your actual Stability AI API key.
4. Run the `SD3.py` script using the following command:

```bash
python SD3.py
```

5. The application will launch in your default web browser.
6. Enter a text prompt describing the image you want to generate.
7. Select the desired model (either "sd3" or "sd3-turbo").
8. Choose the aspect ratio for the generated image.
9. Click the "Submit" button to generate the image.
10. The generated image will be displayed on the screen.

## About Stable Diffusion 3

Stable Diffusion 3 is a state-of-the-art text-to-image generation model developed by Stability AI. It is capable of generating high-quality images from textual descriptions, allowing users to create visual content based on their imagination.

The model has been trained on a vast dataset of image-text pairs, enabling it to understand and generate images across a wide range of domains and styles. It uses a diffusion-based approach to iteratively refine the generated image, resulting in highly detailed and coherent visual outputs.

Stable Diffusion 3 offers two variants: "sd3" and "sd3-turbo". The "sd3" model is the standard version, while "sd3-turbo" is a more powerful and computationally intensive variant that can generate even higher-quality images.

## Acknowledgements

This application is built using the Stability AI API and the Gradio library. We would like to thank the developers and contributors of these projects for their excellent work.

## License

This project is licensed under the [MIT License](LICENSE).
