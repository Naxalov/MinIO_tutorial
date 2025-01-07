# MinIO Tutorial

This tutorial guides you through setting up a local environment for using the [MinIO Python client](https://docs.min.io/docs/python-client-quickstart-guide.html). By the end of this tutorial, you will have a functional MinIO environment and be able to confirm successful installation of the MinIO Python client.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
3. [Installing the MinIO Python Client](#installing-the-minio-python-client)
4. [Verifying Installation](#verifying-installation)

---

## Prerequisites

- Python 3.x installed on your system  
- [pip](https://pip.pypa.io/en/stable/installing/) for package management (usually comes by default with Python 3.x)

---

## Setting Up a Virtual Environment

1. **Create a virtual environment**  

```bash
   python -m venv venv
```

2. **Activate the virtual environment**  

```bash
   source venv/bin/activate
```

---

## Installing the MinIO Python Client

1. **Install the MinIO Python client**  

```bash
   pip install minio
```

## Verifying Installation

1. **Use the pip show command to verify the installation**  

```bash
   pip show minio
```

2. **Use the Python shell to verify the installation**  

```
python -c "import minio; print(minio.__version__)"
```

3. **Use the Python script below to verify the installation**  

```python
   from minio import Minio

   # print the MinIO Python client version
    print(Minio.__version__)
```


