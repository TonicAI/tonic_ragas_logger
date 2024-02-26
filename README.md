# Tonic Validate Ragas Logger
 
The Tonic Validate Ragas Logger is a tool to upload your results from Ragas to the Tonic Validate UI for visualization. The UI is completely free to use.

<picture>
  <img src="https://raw.githubusercontent.com/TonicAI/tonic_validate/main/readme_images/TonicValidate-Graph.png" width="800">
</picture>

To get started, install the `validate-ragas-logger` library.


```bash
pip install tonic-ragas-logger
```

After the library is installed, you can start uploading your Ragas results. Here is an example of how to upload Ragas results.

```python
from ragas import evaluate
from datasets import Dataset
from tonic_ragas_logger import RagasValidateApi

dataset = Dataset.from_dict({
    'question': [
        'What is the capital of France?'
    ],
    'contexts': [
        ['Paris is the capital of France.']
    ],
    'answer': ['Paris'],
    'ground_truths': [['Paris']]
})

results = evaluate(dataset)

# Upload results to the Tonic Validate UI
validate_api = RagasValidateApi("your-api-key")
validate_api.upload_results("your-project-id", results)
```

To get an API key for Tonic Validate, sign up for an account on [our website](https://validate.tonic.ai/). When you sign up, you can create an API key on the sidebar.

<picture>
  <img src="https://raw.githubusercontent.com/TonicAI/tonic_ragas_logger/main/readme_images/api_key.png" width="800">
</picture>

Once you have an API key, you can either set it in the `TONIC_VALIDATE_API_KEY` environment variable or you can input it into the `RagasValidateApi` constructor like so

```python
validate_api = RagasValidateApi("your-api-key")
```

After you have created an API key, you can create a project which allows you to upload your results to the UI. To do so, click on the create a project button on the homepage of Tonic Validate.

<picture>
  <img src="https://raw.githubusercontent.com/TonicAI/tonic_ragas_logger/main/readme_images/validate_create_project.png" width="800">
</picture>

After creating your project, you will be provided a project id which you can copy into `upload_results`.

```python
validate_api.upload_results("your-project-id", results)
```

After you execute `upload_results`, your results should be visible in the UI.

<picture>
  <img src="https://raw.githubusercontent.com/TonicAI/tonic_validate/main/readme_images/TonicValidate-Graph.png" width="800">
</picture>

Congratulations, now you have uploaded your Ragas results to Tonic Validate!