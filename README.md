<h1 style="color:green"><span style="color:green">Maté 🧉</span></h1>

Mate is a tool designed to improve reproducibility and facilitate development in deep learning. It is a command line tool that offers a variety of features to help you manage your project, including:

- Validating the structure of your project
- Visualizing/summarizing your project
- Summarizing your results
- Running/testing your experiments.

In addition, any project developed with Mate on a public repository gets automatically listed on [MateHub](https://salamanderxing.github.io/mate/). This website is a browser for finding and reusing components created by others (or yourself).

Mate is compatible is any python deep learning framework (such as JAX, PyTorch, and TensorFlow) since it leverages Python features.


<p align="center">
  <img src="./imgs/mate_summary.svg" alt="Your Image" style="width: 60%; margin-left:10px; border-radius:50%;">
</p>

## Installation 🔌
At the moment Maté is only supported on MacOS and Linux, but soon also windows.

```bash
git clone https://github.com/SalamanderXing/mate
cd mate
pip install -e .
```

## [Documentation](./docs.md)

## Examples

### PyTorch Lightning

- [MNIST Classifier](https://github.com/SalamanderXing/pytorch-lightning-mnist)

### JAX (with Flax)
[JAX](https://github.com/google/jax) is the (relatively) new framework by Google. That uses just-in-time-compilation to improve performance of your neural network.
These projects are based on this [amazing repo](https://github.com/phlippe/uvadlc_notebooks/tree/master/docs/tutorial_notebooks/JAX).

- [CIFAR10 Autoecoder](https://github.com/SalamanderXing/jax-ae)
- [Graph Neural Networks](https://github.com/SalamanderXing/jax-gnn)
- [Normalizing Flow](https://github.com/SalamanderXing/jax-normalizing-flow)
- [Inception, ResNet, DenseNet](https://github.com/SalamanderXing/jax-inception-resnet-densenet)
- [Autoregressive Image Modeling](https://github.com/SalamanderXing/jax-autoregressive-image-modeling)
- [Transformers for text classification](https://github.com/SalamanderXing/jax-transformers)
- [Transformers for anomaly detection](https://github.com/SalamanderXing/jax-anomaly-detection)


## Quick Start ⚡
This example will walk you through training and showing results of your model on a Pytorch-Lithtning example. 
> For this project in particular, you need PyTorch and Pytorch-Lithtning installed.

First let's clone the project, for example: 
```bash
git clone https://github.com/SalamanderXing/pytorch-lightning-mnist
```
Then go to the project directory:
```bash
cd mnist_classifier
```
Then run:
```
mate summary
```
This will give you an overview of your projec and your componens. It also tells you where your components have issues. In this case, (hopefully) you will see something like this:
<p align="center" style="margin:0; padding:0;">
  <img src="./imgs/lightning_summary.svg" alt="Your Image" style="width: 30%; height:200; object-fit:cover; margin-left:10px; margin-top:0, border-radius:50%;">
</p>
then we can train our experiment:

```bash
mate train simple
```


You should see all the training logs.
If you now do again:
```bash
mate summary
```
You should notice a 💪 next to the experiment. That means that the training was successful:
<p align="center" style="margin:0; padding:0;">
  <img src="./imgs/lightning_summary_after_training.svg" alt="Your Image" style="width: 30%; height:200; object-fit:cover; margin-left:10px; margin-top:0, border-radius:50%;">
</p>

Finally, to visualize our results:

```bash
mate results
```
<p align="center" style="margin:0; padding:0;">
  <img src="./imgs/lightning_results.svg" alt="Your Image" style="width: 50%; height:200; margin-left:10px; margin-top:0, border-radius:50%;">
</p>
Mate has inferred the dataset and will group our experiments according to that and put them in the same table.

## MateHub

[MateHub](https://salamanderxing.github.io/mate/). Before creating a new module (trainer, data_loader, model) you might want to head over to this site and look if there is anything that either fits your need or allows you to not start from scratch. 

### How it works
All mate projects on public github repo (published by anyone) will be automatically listed on MateHub. It works by using the GitHub rest API.


## Comparison to familiar tools

- *Weights & Biases*, *Tensorboard*  is a logger and allows model weights sharing as well. Mate does not attempt to replace logger's functionalities. Use the logger your like best :) That would happend probably inside your trainer module. 
- *[Monai](https://github.com/Project-MONAI/MONAI)*: Focuses on medical imaging and provides pretrained models as well as preprocessing pipelines
- *[Ivy](https://github.com/unifyai/ivy)*: Provides a unified tensor type that work with all backends (frameworks). Works with mate!
- *[THINGSvision](https://github.com/ViCCo-Group/thingsvision)*: Provides a set pretrained models for analysis of their activation. In particular to compare them with brain activations.


## FAQ
**Q: Does Maté work with colab?**

**A**: Yes! Maté works with colab as any Maté project is exportable to a juypter notebook.

## Contact 🤝 

For questions please contact:

g.zani(at)uva.nl
