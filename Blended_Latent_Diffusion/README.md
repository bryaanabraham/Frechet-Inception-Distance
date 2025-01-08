
# Blended Latent Diffusion

# Installation
Install the conda virtual environment:
```bash
$ conda env create -f environment.yaml
$ conda activate ldm
```

# Usage

## New - Stable Diffusion Implementation
You can use the newer Stable Diffusion implementation based on [Diffusers](https://github.com/huggingface/diffusers) library.
For that, you need to install PyTorch 2.1 and Diffusers via the following commands:
```bash
$ conda install pytorch==2.1.0 torchvision==0.16.0  pytorch-cuda=11.8 -c pytorch -c nvidia
$ pip install -r pip_requirements.txt
```

* For using Stable Diffusion XL (requires a stronger GPU), use the following script:

```bash
$ python scripts/text_editing_SDXL.py --prompt "a stone" --init_image "inputs/img.png" --mask "inputs/mask.png"
```
You can use smaller `--batch_size` in order to save GPU memory.

* For using Stable Diffusion v2.1, use the following script:
```bash
$ python scripts/text_editing_SD2.py --prompt "a stone" --init_image "inputs/img.png" --mask "inputs/mask.png"
```

## Old - Latent Diffusion Model Implementation
For using the old implementation, based on the Latent Diffusion Model (LDM), you need first to download the pre-trained weights (5.7GB):
```bash
$ mkdir -p models/ldm/text2img-large/
$ wget -O models/ldm/text2img-large/model.ckpt https://ommer-lab.com/files/latent-diffusion/nitro/txt2img-f8-large/model.ckpt
```

Alternatively use: [link](https://huggingface.co/omriav/blended-latent-diffusion-ldm/resolve/main/model.ckpt?download=true).

Then, editing the image may require two steps:
### Step 1 - Generate initial predictions
```bash
$ python scripts/text_editing_LDM.py --prompt "a pink yarn ball" --init_image "inputs/img.png" --mask "inputs/mask.png"
```

The predictions will be saved in `outputs/edit_results/samples`.

You can use a larger batch size by specifying `--n_samples` to the maximum number that saturates your GPU.

### Step 2 (optional) - Reconstruct the original background
If you want to reconstruct the original image background, you can run the following:
```bash
$ python scripts/reconstruct.py --init_image "inputs/img.png" --mask "inputs/mask.png" --selected_indices 0 1
```

You can choose the specific image indices that you want to reconstruct. The results will be saved in `outputs/edit_results/samples/reconstructed_optimization`.


# Acknowledgements
This code is based on [Latent Diffusion Models](https://github.com/CompVis/latent-diffusion) and is cloned from [blended-latent-diffusion (omriav)](https://github.com/omriav/blended-latent-diffusion.git).
