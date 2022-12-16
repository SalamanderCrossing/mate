<h1 style="color:green"><span style="color:green">Maté 🧉</span></h1>


Maté is a comprehensive framework for deep learning projects that aims to streamline the development process and make it easier for developers to create high-quality projects. It includes features such as a training manager to help you set up, run, and monitor your models, as well as a package manager to manage dependencies and share code with others.


Maté also includes a [MateHub](https://salamanderxing.github.io/mate/), a store of all available modules that can be easily accessed and incorporated into a project. With support for multiple deep learning frameworks including PyTorch, TensorFlow, and Jax, Maté is flexible and can be used with the tools you already know and love.


Maté standardizes project structure to make it easy to understand and work with, while still allowing for flexibility and customization. And with its intuitive design, Maté is easy to learn and use, saving you time and effort in the development process. Make your deep learning projects more efficient and effective with Maté.

<p align="center">
  <img src="./imgs/mate_summary.png" alt="Your Image" style="width: 60%; margin-left:10px; border-radius:50%;">
</p>

## Installation 🔌
At the moment Maté is only supported on MacOS and Linux, but soon also windows.

```bash
git clone https://github.com/SalamanderXing/mate
cd mate
pip install -e .
```

## Examples



## Quick Start ⚡

**Train a model**

```bash
mate train my_experiment
```

**Evaluate a model**

```bash
mate test my_experiment
```

**Run a model**

```bash
mate run feature_extraction my_experiment
```

**Clone a model**

```bash
mate clone resnet my_resnet
```

More features coming soon!

## Comparison to familiar tools

- *Weights & Biases* wandb is a logger and allows model weights sharing as well
- *Tensorboard* This is a logger and can be integrated into mate
- *[Monai](https://github.com/Project-MONAI/MONAI)*
- *[Ivy](https://github.com/unifyai/ivy)*
- *[THINGSvision](https://github.com/ViCCo-Group/thingsvision)*





## For Coders
Dear coders, we try our best to not get in your way and in fact, you do not have to integrate or import any mate class to your projects. Mate simply parses the configuration. To make your project mate compatible, you need to move a few files and make a Bombilla configuration file. 


**More tutorials and examples will be added soon!!**



## FAQ
**Q: Does Maté work with colab?**

**A**: Yes! Maté works with colab as any Maté project is exportable to a juypter notebook.

## Contact 🤝 

For questions please contact:

g.zani(at)uva.nl
