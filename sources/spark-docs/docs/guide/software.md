# Software

Software is provided as **modules**, as on Gadi and Katana. The big Python packages (PyTorch,
transformers, …) are installed once, centrally, so they don't use up your file quota, and every
module in a release has been tested together.

## Modules

```bash
module avail                 # what's available
module load hf/26.11         # load one (it loads what it needs too)
module list                  # what you have loaded
module unload hf             # unload
module spider vllm           # details about a module
```

A small `base` module is loaded at login and stays loaded; it sets up the cache locations and a
few safety settings. You don't need to touch it.

## Python bundles (release 26.11)

The Python stack comes as bundles that build on each other. Each does one job:

| Module | What's in it | Loads first |
|---|---|---|
| `core/26.11` | Python 3.12, PyTorch 2.14 (CUDA 13.0), torchvision, torchaudio, NumPy, SciPy, pandas, PyArrow, scikit-learn, Matplotlib, seaborn, tqdm, Weights & Biases, TensorBoard | |
| `hf/26.11` | transformers 5.23, tokenizers, safetensors, huggingface_hub, accelerate, datasets, sentence-transformers, bitsandbytes, torchao, sentencepiece, tiktoken | `core` |
| `train/26.11` | PEFT 0.21, TRL 1.18 | `hf` |
| `eval/26.11` | lm-eval 0.4.13, evaluate, sacreBLEU, rouge-score | `hf` |
| `jupyter/26.11` | JupyterLab, ipykernel, ipywidgets | `core` |

For example, `module load train/26.11` gives you everything for LoRA fine-tuning with PEFT and
TRL. To see exact versions: `python -m pip list`.

The release number is the year and month (`26.11` = November 2026). A new release doesn't change
an old one, so a project can stay on `26.11` while others move on.

## Adding your own packages

Make a virtual environment **on top of** the modules. It sees everything in the modules you have
loaded, and holds only what you add:

```bash
module load hf/26.11
python3 -m venv --system-site-packages --without-pip /scratch/$USER/envs/myproject
source /scratch/$USER/envs/myproject/bin/activate
python -m pip install some-package
```

- Keep environments in scratch, not home.
- Use **`python -m pip`**, not `uv pip`: uv can't see the bundle packages and would download
  second copies of transformers and friends.
- pip won't replace PyTorch, NumPy or the CUDA libraries: the modules pin those, so your
  environment stays compatible. Other packages you install take priority over the bundle's.
- `pip install` outside a virtual environment is refused on purpose, so nothing lands in
  `~/.local`.

Next time: `module load hf/26.11` and `source …/activate` again (also inside job scripts).

## Containers

Two tools ship as containers, because they need their own builds of PyTorch. You use them
through a command, and they only run inside Slurm jobs.

| Module | Command | What it is |
|---|---|---|
| `vllm/26.09` | `vllm` | vLLM 0.29 for serving models, from NVIDIA's NGC build. See [Serve a model with vLLM](../howto/vllm.md) |
| `unsloth/26.11` | `unsloth-python` | Unsloth 2026.11.6 for fast fine-tuning, on NVIDIA's PyTorch 25.11. See [Fine-tune with Unsloth](../howto/unsloth.md) |

You can also run your own containers with **Apptainer** inside a job (`apptainer exec --nv
my.sif …`). Docker isn't available to users.

## GB10 specifics

- **Arm, not x86.** Packages need `aarch64` builds. Most of PyPI has them; if pip starts compiling
  something big from source, ask before letting it run for an hour.
- **flash-attn doesn't build for this GPU.** Use PyTorch's built-in attention instead:
  `attn_implementation="sdpa"` in transformers. It's the default in most models anyway.
- **Precision:** BF16 is the safe default for training and inference. FP8 works well for
  inference (for example `--quantization fp8` in vLLM). FP4 is still experimental.
