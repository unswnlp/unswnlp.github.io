# Fine-tune with Unsloth

[Unsloth](https://unsloth.ai) speeds up LoRA and QLoRA fine-tuning. On the Spark machines it comes as the
`unsloth/26.11` module: Unsloth 2026.11.6 in a container built on NVIDIA's PyTorch 25.11, with
its own transformers 5.17, TRL 1.15, PEFT, xformers and bitsandbytes. You run your script with
`unsloth-python` instead of `python`, inside a Slurm job.

For plain PEFT/TRL without Unsloth, the `train/26.11` module is simpler.

## A training job

```python title="finetune.py"
import os
import torch
from unsloth import FastLanguageModel
from datasets import Dataset
from trl import SFTConfig, SFTTrainer

model, tok = FastLanguageModel.from_pretrained(
    "/models/Qwen/Qwen3-1.7B", max_seq_length=2048, dtype=torch.bfloat16, load_in_4bit=False)
model = FastLanguageModel.get_peft_model(
    model, r=16, lora_alpha=16, target_modules=["q_proj", "k_proj", "v_proj", "o_proj"])

data = Dataset.from_dict({"text": ["Q: what is 2 plus 2? A: 4."] * 64})   # your data here
out = f"/scratch/{os.environ['USER']}/runs/qwen3-lora"
trainer = SFTTrainer(model=model, processing_class=tok, train_dataset=data,
                     args=SFTConfig(output_dir=out, max_steps=100, per_device_train_batch_size=4,
                                    logging_steps=10, report_to="none"))
trainer.train()
```

```bash title="finetune.sbatch"
#!/bin/bash -l
#SBATCH -J finetune
#SBATCH -p batch
#SBATCH --gres=shard:2
#SBATCH -c 8
#SBATCH --mem=48G
#SBATCH -t 08:00:00
#SBATCH -o /scratch/%u/finetune.%j.log

module load unsloth/26.11
cd /scratch/$USER        # Unsloth writes a compiled cache in the current folder
unsloth-python finetune.py
```

For a quick try, an interactive job works too:

```bash
module load unsloth/26.11
cd /scratch/$USER
srun -p interactive -c 4 --mem=24G --gres=shard:1 -t 30 unsloth-python finetune.py
```

## Sizing

- **LoRA in BF16** needs the model's weights (2 GB per billion parameters) plus activations and
  optimizer state for the adapters. A 1.7B model fits easily in `--mem=24G`; a 27-31B model needs
  most of the machine (`--gres=gpu:1 --mem=105G`).
- **QLoRA** (`load_in_4bit=True`) cuts the weights to about a quarter, for models that don't fit
  in BF16. bitsandbytes works on the GB10.

## Extra packages

`unsloth-python` runs the container's Python, so the `core`/`hf` modules and your own virtual
environments don't apply inside it. If your script needs a package the container doesn't have,
ask the maintainer. To see what's included:

```bash
apptainer exec /apps/containers/unsloth/26.11/unsloth.sif pip list
```

## Messages you can ignore

- `Not an error, but Unsloth cannot patch MLP layers…`: normal when your LoRA doesn't cover the
  MLP layers (as in the example above), or the model has bias terms.
- `Ignoring an unusable torchao…`: only matters for torchao quantization, which LoRA and QLoRA
  don't use.
