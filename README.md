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




### Telemetry
Tonic Ragas Logger collects minimal telemetry to help us figure out what users want and how they're using the product. We do not use any existing telemetry framework and instead created our own privacy focused setup. Only the following information is tracked

* What metrics were used for a run
* Number of questions in a run
* SDK Version
* Is being run on a CI machine

We do **NOT** track things such as the contents of the questions / answers, your scores, or any other sensitive information. For detecting CI/CD, we only check for common environment variables in different CI/CD environments. We do not log the values of these environment variables.

We also generate a random UUID to help us figure out how many users are using the product. This UUID is linked to your Tonic Validate account only to help track who is using the SDK and UI at once and to get user counts. If you want to see how we implemented telemetry, you can do so in the `tonic_ragas_logger/utils/telemetry.py` file

If you wish to opt out of telemetry, you only need to set the `TONIC_RAGAS_DO_NOT_TRACK` environment variable to `True`.


<p align="right">(<a href="#readme-top">back to top</a>)</p>