# Tensor Amplification and Spectral Transfer for Sidorenko-Type Inequalities

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-2607.02260v1-B31B1B.svg)](https://arxiv.org/pdf/2607.02260v1)

This repository contains a Python implementation of the concepts and algorithms described in the research paper **"Tensor Amplification and Spectral Transfer for Sidorenko-Type Inequalities"** by Yuqi Zhao. The implementation provides computational tools to explore and verify the tensor-amplification framework for Sidorenko-type inequalities in graphon classes.

---

## 📜 Overview of the Paper

The paper introduces a **tensor-amplification framework** to study Sidorenko-type inequalities in graphon classes. These inequalities are crucial in extremal graph theory and combinatorics, as they provide insights into graph homomorphism densities and their relationships with structural properties of graphs.

### Key Contributions:
1. **Admissible Classes**: The framework applies to any admissible class of graphons, defined as classes that are:
   - Closed under **tensor powers**.
   - Closed under **normalized principal restrictions**.
   
2. **Transfer Principles**:
   - **Regularization of Equality Cases**: For any non-matching graph \( H \) that is \( \mathcal{C} \)-Sidorenko, equality cases \( t(H, W) = p(W)^{e(H)} \) with \( W \in \mathcal{C} \) are shown to regularize optimally.
   - **Spectral Transfer**: Establishes equivalence between ordinary \( \mathcal{C} \)-Sidorenko and a spectral inequality for \( H \) in the range \( v(H) \leq e(H) \), using a Perron-biased tensor regularization theorem.

3. **Applications**:
   - The framework is applied to **doubly nonnegative graphons** and **bounded doubly nonnegative kernels**, yielding spectral equivalences for Sidorenko-good graphs and identifying Sidorenko-good forcing with regular-KNRS forcing.

---

## ⚙️ How It Works

The implementation in this repository provides a computational framework to:
1. **Model Graphons**:
   - Represent graphons as mathematical objects, including doubly nonnegative graphons and bounded kernels.
   
2. **Tensor Amplification**:
   - Compute tensor powers of graphons and analyze their properties under the admissible class constraints.

3. **Verify Sidorenko-Type Inequalities**:
   - Test if a given graph \( H \) satisfies the \( \mathcal{C} \)-Sidorenko property within a specified graphon class.
   
4. **Spectral Transfer**:
   - Compute and verify the spectral inequality \( t(H, W) \geq \rho(W)^{2e(H)-v(H)}p(W)^{v(H)-e(H)} \) for non-zero \( W \in \mathcal{C} \).

5. **Regularization Analysis**:
   - Analyze the regularity of equality cases \( t(H, W) = p(W)^{e(H)} \) for \( W \in \mathcal{C} \).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Required Python libraries:
  - `numpy`
  - `scipy`
  - `matplotlib`

Install dependencies using:
```bash
pip install -r requirements.txt
```

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/tensor-amplification.git
cd tensor-amplification
```

---

## 🛠️ Usage

The main implementation is provided in the `implementation.py` script. Below are the steps to use it:

### 1. Define a Graphon
Graphons can be defined as functions or matrices. For example:
```python
from implementation import Graphon

# Define a simple graphon as a matrix
W = Graphon.from_matrix([
    [0.5, 0.2],
    [0.2, 0.7]
])
```

### 2. Tensor Amplification
Compute the tensor power of a graphon:
```python
# Compute the 2nd tensor power of W
tensor_power = W.tensor_power(2)
print(tensor_power)
```

### 3. Verify Sidorenko-Type Inequalities
Check if a graph \( H \) satisfies the Sidorenko property for a given graphon class:
```python
from implementation import is_sidorenko

# Define a simple graph H (e.g., a triangle)
H = {
    "nodes": 3,
    "edges": [(0, 1), (1, 2), (2, 0)]
}

# Check Sidorenko property
result = is_sidorenko(H, W)
print(f"Is H Sidorenko? {result}")
```

### 4. Spectral Transfer
Compute and verify the spectral inequality:
```python
from implementation import spectral_transfer

# Verify spectral inequality for H and W
spectral_result = spectral_transfer(H, W)
print(f"Spectral Inequality Satisfied? {spectral_result}")
```

### 5. Regularization Analysis
Analyze the regularity of equality cases:
```python
from implementation import analyze_regularization

# Analyze regularization for equality cases
regularization_result = analyze_regularization(H, W)
print(f"Regularization Result: {regularization_result}")
```

---

## 📊 Examples and Visualizations

The repository includes a `notebooks/` directory with Jupyter notebooks demonstrating:
- Tensor amplification for various graphons.
- Visualization of graphon tensor powers.
- Verification of Sidorenko-type inequalities.
- Spectral transfer principles.

To run the notebooks:
```bash
jupyter notebook notebooks/
```

---

## 🧪 Testing

Unit tests are provided to ensure correctness. Run the tests using:
```bash
pytest tests/
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💡 Acknowledgments

This implementation is based on the research paper **"Tensor Amplification and Spectral Transfer for Sidorenko-Type Inequalities"** by Yuqi Zhao. You can find the original paper on [arXiv](https://arxiv.org/pdf/2607.02260v1).

If you use this implementation in your research, please consider citing the original paper:
```
@article{zhao2023tensor,
  title={Tensor Amplification and Spectral Transfer for Sidorenko-Type Inequalities},
  author={Yuqi Zhao},
  journal={arXiv preprint arXiv:2607.02260v1},
  year={2023}
}
```

---

## 🤝 Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

For questions or feedback, please feel free to reach out to [Yuqi Zhao](https://arxiv.org/pdf/2607.02260v1) or open an issue in this repository.