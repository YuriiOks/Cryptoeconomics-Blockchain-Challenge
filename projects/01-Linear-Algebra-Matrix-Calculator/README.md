# 🧮 01-Linear-Algebra-Matrix-Calculator

This project is part of the 30-day Cryptoeconomics & Blockchain Technology Challenge, focusing on foundational linear algebra concepts. The goal is to implement and explore various matrix operations, determinants, and their applications in cryptography. This project serves as an introduction to the mathematical tools used in game theory, economics, and blockchain technology.

## 📚 Learning Objectives

By completing this project, you will:

1. Understand fundamental linear algebra operations, including vector and matrix manipulations.
2. Implement mathematical operations such as matrix addition, multiplication, and transposition using Python.
3. Learn about special matrices (inverse, symmetric, orthogonal) and their properties.
4. Compute and analyze determinants and matrix inverses.
5. Explore eigenvalues and eigenvectors with practical examples.
6. Apply linear algebra concepts to cryptographic algorithms like the Hill Cipher.

## 🚀 Project Structure

The project is divided into five Jupyter notebooks, each focusing on a specific topic, along with supporting Python scripts for reusable functions:

```bash
/01-Linear-Algebra-Matrix-Calculator/
├── notebooks/
│   ├── 01-Scalars-Vectors-Matrices.ipynb       # Notebook 1: Scalars, Vectors, and Matrices Concepts
│   ├── 02-Matrix-Operations.ipynb              # Notebook 2: Matrix Operations (Addition, Multiplication, Transpose)
│   ├── 03-Determinants-Inverses.ipynb          # Notebook 3: Determinants and Inverses
│   ├── 04-Eigenvalues-Eigenvectors.ipynb       # Notebook 4: Eigenvalues and Eigenvectors
│   ├── 05-Cryptography-Applications.ipynb      # Notebook 5: Applications in Cryptography
├── scripts/                                    # Python scripts for major functions
│   ├── matrix_operations.py                    # Code for matrix addition, multiplication, etc.
│   ├── eigenvalues.py                          # Code for computing eigenvalues
│   ├── hill_cipher.py                          # Code for Hill Cipher implementation
│   └── parity_check.py                         # Code for error-correcting code exercises
├── data/                                       # Optional: If any data sets are required
│   └── example_data.csv
├── assets/                                     # Store any external graphics, logos, or other media
│   └── images/
│       ├── matrix_addition_example.png
│       └── eigenvalue_visualization.png
├── README.md                                   # Project documentation
└── environment.yml                             # Environment file for dependencies
```

## 🛠️ Setup Instructions

To get started with this project, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/YuriiOks/Cryptoeconomics-Blockchain-Challenge.git
   cd Cryptoeconomics-Blockchain-Challenge/projects/01-Linear-Algebra-Matrix-Calculator
   ```

2. **Set Up the Python Environment**:
   You can use `conda` to create the environment defined in `environment.yml`:

   ```bash
   conda env create -f environment.yml
   conda activate linear-algebra
   ```

3. **Install Jupyter and Dependencies**:
   If you’re not using `conda`, install the dependencies with `pip`:

   ```bash
   pip install numpy pandas matplotlib jupyter sympy seaborn
   ```

4. **Run Jupyter Notebooks**:
   Start Jupyter Lab or Jupyter Notebook to interact with the notebooks:

   ```bash
   jupyter lab
   ```

5. **Open the First Notebook**:
   Navigate to the `notebooks/` folder and open `01-Scalars-Vectors-Matrices.ipynb` to start with the basics.

## 📁 Directory Details

- **notebooks/**: Contains five Jupyter notebooks covering different linear algebra topics.
- **scripts/**: Contains standalone Python scripts implementing core algorithms for each section.
- **data/**: Optional folder to store data files used in matrix operations and cryptography exercises.
- **assets/images/**: Visual elements and images referenced in the notebooks.
- **environment.yml**: Specifies the Python version and dependencies required for the project.

## ✨ Key Concepts and Exercises

### 1. Scalars, Vectors, and Matrices

- Learn basic operations and types of matrices.
- Practice vector addition, dot product, and scalar multiplication.
- **Exercise**: Implement vector addition and visualize the results using `matplotlib`.

### 2. Matrix Operations

- Implement matrix addition, multiplication, and transpose.
- Explore the properties of matrix operations using step-by-step visualizations.
- **Exercise**: Use matrix multiplication to perform a geometric transformation on a 2D object.

### 3. Determinants and Inverses

- Calculate determinants for 2x2 and 3x3 matrices.
- Learn about matrix inversion and its applications.
- **Exercise**: Use determinants to determine matrix invertibility and compute inverses.

### 4. Eigenvalues and Eigenvectors

- Define eigenvalues and eigenvectors and understand their geometric interpretation.
- Solve the characteristic equation for basic matrices.
- **Exercise**: Use Python to diagonalize a matrix and interpret the results visually.

### 5. Applications in Cryptography

- Implement the Hill Cipher for message encoding and decoding.
- Learn about matrix transformations in cryptography.
- **Exercise**: Create a Python-based encryption/decryption system using the Hill Cipher.

## 💡 Tips and Recommendations

- Follow the notebooks sequentially, as each builds on the concepts introduced in the previous one.
- Use the interactive visualizations to gain deeper insights into matrix transformations.
- For a more challenging experience, try modifying the Hill Cipher implementation to handle larger matrices.

## 📧 Questions or Issues?

If you encounter any issues or have questions, feel free to reach out through the issue tracker in this repository. You can also contribute by submitting pull requests with improvements or new features.

## 📜 License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.
