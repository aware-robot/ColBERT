from setuptools import setup, Extension
import os
import torch.utils

with open('README.md', 'r') as f:
    long_description = f.read()

# Define the extension module
torch_path = os.path.join(torch.__path__[0], 'include/')
torch_api_path = os.path.join(torch_path, 'torch/csrc/api/include/')
segmented_maxsim_module = Extension(
    'colbert.modeling.segmented_maxsim',
    sources=['colbert/modeling/segmented_maxsim.cpp'],
    include_dirs=[torch_path, torch_api_path]
)

setup(
    name='ColBERT',
    version='0.2.0',
    author='Omar Khattab',
    author_email='okhattab@stanford.edu',
    description="Efficient and Effective Passage Search via Contextualized Late Interaction over BERT",
    ext_modules=[segmented_maxsim_module],
    install_requires=open('requirements.txt').read().splitlines(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/stanford-futuredata/ColBERT',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
