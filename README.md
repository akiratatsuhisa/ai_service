# AI Service

## Prerequisite

- Python version 3.1x.x or higher
- Windows operating system

## Installation Steps

1. Create a Virtual Environment

Run the following command to create a virtual environment:

```bash
python -m venv .venv
```

2. Install Dependencies

Activate the virtual environment and install the dependencies from requirements.txt:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Install PyTorch:

Install PyTorch with the required CUDA version:

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```

4. Create config.json File

In the root folder of the project, create a config.json file with the following content:

```json
{
  "HF_HOME": "C:\\path\\to\\your\\cache",
  "PORT": "8080",
  "MODEL_NAME": "deepseek-ai/deepseek-coder-1.3b-instruct"
}
```

## Configuration Fields

| Field        | Purpose                          | Example Value                              |
| ------------ | -------------------------------- | ------------------------------------------ |
| `HF_HOME`    | Directory for Hugging Face cache | `C:\\path\\to\\your\\cache`                |
| `PORT`       | Port number for the service      | `8080`                                     |
| `MODEL_NAME` | Name of the model to be used     | `deepseek-ai/deepseek-coder-1.3b-instruct` |

## Running the Service

- To run the service (for non-developers):
  Execute the run.sh script:

```bash
./run.sh serve
```

- To debug via VSCode

Open the project in VSCode and use the built-in debugger to run the service.

## License

This project is licensed under the AGPL-3.0. For more details, refer to the LICENSE file.
