# Install required libraries
!pip install diffusers transformers accelerate -q

from diffusers import StableDiffusionPipeline
import torch

# Load the model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda")

# Your prompt
prompt = "brown color cat is sitting on mango tree, realistic, detailed fur, sunny day, high quality"

# Generate image
image = pipe(
    prompt,
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]

# Show and save the image
image.save("cat_on_mango_tree.png")
image