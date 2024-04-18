import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import gradio as gr

def generate_image(prompt, aspect_ratio='1:1', model='sd3', seed=0, output_format='png'):
    api_url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    api_key = "sk-lr4V2rv0uFv2dmgD34TPrURw9ppaFgcZs67rNW7zKqJqiHEb"  # Replace this with your actual API key

    m = MultipartEncoder(
        fields={
            'prompt': prompt,
            'aspect_ratio': aspect_ratio,
            'model': model,
            'seed': str(seed),
            'output_format': output_format,
            'mode': 'text-to-image'  # Default mode
        }
    )

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': m.content_type,
        'Accept': 'image/*'  # To receive the image directly
    }

    response = requests.post(api_url, data=m, headers=headers)
    print(response.status_code, response.content)
    
    if response.status_code == 200:
        # Assuming the response content is the image in binary format
        output_path = 'generated_image.png'
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return output_path  # Return the path for Gradio to display the image
    else:
        return f"Error: {response.text}"

def wrap_generate_image(prompt, model, aspect_ratio):
    return generate_image(prompt, aspect_ratio, model)

iface = gr.Interface(
    fn=wrap_generate_image,
    inputs=[
        gr.Textbox(lines=2, label="Prompt", placeholder="Enter a description for the image..."),
        gr.Radio(choices=['sd3', 'sd3-turbo'], label="Model", value='sd3'),
        gr.Dropdown(choices=['1:1', '16:9', '21:9', '2:3', '3:2', '4:5', '5:4', '9:16', '9:21'], label="Aspect Ratio", value='1:1')
    ],
    outputs=gr.Image(),
    title="Stable Diffusion 3 Text-to-Image Generator",
    description="Select a model, aspect ratio, and enter a prompt to generate an image using Stable Diffusion 3."
)

iface.launch(share=True)
