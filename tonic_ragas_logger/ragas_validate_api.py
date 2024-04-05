from typing import Any, List, Optional, Dict

from tonic_ragas_logger.utils.telemetry import Telemetry
from tonic_validate import Run, RunData
from tonic_ragas_logger.config import Config

from tonic_ragas_logger.utils.http_client import HttpClient
from ragas.evaluation import Result


class RagasValidateApi:
    """Wrapper class for invoking the Tonic Validate UI.

    Parameters
    ----------
    api_key : str
        The access token for the Tonic Validate UI. The access token is obtained from
        the Tonic Validate UI.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
    ):
        self.config = Config()
        if api_key is None:
            api_key = self.config.TONIC_VALIDATE_API_KEY
            if api_key is None:
                exception_message = (
                    "No api key provided. Please provide an api key or set "
                    "TONIC_VALIDATE_API_KEY environment variable."
                )
                raise Exception(exception_message)
        self.client = HttpClient(self.config.TONIC_VALIDATE_BASE_URL, api_key)
        self.telemetry = Telemetry()

    def upload_results(
        self,
        project_id: str,
        results: Result,
        run_metadata: Dict[str, Any] = {},
        tags: List[str] = [],
    ) -> str:
        """Uploads results to a Tonic Validate project.

        Parameters
        ----------
        project_id : str
            The ID of the project to upload the run to.
        results : Result
            The result to upload.
        run_metadata : Dict[str, str]
            Metadata to attach to the run. If the values are not strings, then they are
            converted to strings before making the request.
        """
        run = self.__convert_to_run(results)
        run_response = self.client.http_post(
            f"/projects/{project_id}/runs/with_data",
            data={
                "run_metadata": run_metadata,
                "tags": tags,
                "data": [run_data.to_dict() for run_data in run.run_data],
            },
        )

        try:
            self.telemetry.log_run(
                len(run.run_data), list(run.overall_scores.keys())
            )
        except Exception as _:
            pass

        return run_response["id"]

    def __convert_to_run(self, results: Result) -> Run:
        """Converts a Result to a Run.

        Parameters
        ----------
        results : Result
            The result to convert.
        """
        try:
            overall_scores = {
                str(score): 0 if value is None else float(value)
                for score, value in results.items()
            }
        except ValueError:
            raise ValueError(
                "The scores in the results are in the format of {score: value} where score is a string and value is a float."
            )

        if not results.dataset:
            raise ValueError(
                "The ragas results do not have a dataset provided. Can not upload results without a dataset."
            )

        if len(results.scores) != len(results.dataset):
            raise ValueError(
                "The length of results.scores and results.dataset are not the same"
            )

        run_data = []
        for i in range(len(results.scores)):
            try:
                scores: Dict[str, float | None] = {
                    str(score): 0 if value is None else float(value)
                    for score, value in results.scores[i].items()
                }
            except ValueError:
                raise ValueError(
                    "The scores in the results are in the format of {score: value} where score is a string and value is a float."
                )
            run_data.append(
                RunData(
                    scores=scores,
                    reference_question=results.dataset["question"][i],
                    reference_answer=results.dataset["ground_truth"][i],
                    llm_answer=results.dataset["answer"][i],
                    llm_context=results.dataset["contexts"][i],
                )
            )

        return Run(
            overall_scores=overall_scores,
            run_data=run_data,
            id=None,
        )
