import json
import os
import inspect


class Mate:
    """
    Class containing all the information about the current run. You usually want to import it into your experiment like this:

    ```python
    from mate import mate  # instance of Mate, containing all the information about the current run
    ```

    You can use this to:
    - Get the current CLI command
    - Save the run to a json file
    - Get the current save directory
    - Get the current checkpoint path

    **Example**

    ```python
    from mate import mate

    if mate.command == "train":
        # do training
    elif mate.command == "test":
        # do testing
    ```
    """

    @staticmethod
    def load():
        get_top_level_cmd = "git rev-parse --show-toplevel"
        top_level = os.popen(get_top_level_cmd).read().strip()
        stack = [al.filename for al in inspect.stack()][-3].split(os.sep)
        if len(stack) > 1:
            cur = stack[-3]
            runtime_filename = os.path.join(top_level, ".mate", cur, "runtime.json")
            if os.path.exists(runtime_filename):
                with open(runtime_filename, "r") as f:
                    runtime = json.load(f)
            else:
                runtime = {"command": "", "save_dir": "", "checkpoint_path": ""}
        else:
            runtime = {"command": "", "save_dir": "", "checkpoint_path": ""}
        return Mate(**runtime)

    def save(self, location: str):
        with open(location, "w") as f:
            json.dump(self.to_dict(), f)

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }

    def __repr__(self):
        return str(self.to_dict())

    def __str__(self):
        return self.__repr__()

    @property
    def is_train(self) -> bool:
        return self.command == "train"

    @property
    def is_test(self) -> bool:
        return self.command == "test"

    def result(self, values: dict):
        """
        Save the results of the current run.

        **Example**
        ```python
        from mate import mate

        mate.result({"loss": 0.5})
        ```

        This is not meant to replace a proper logging framework,
        but rather to provide a simple way to save the results of an experiment.
        This is especially useful when you want to compare multiple experiments (see `mate.results()`).

        **Pytorch Lightning Example**

        If you want, with pytorch lightning, you can directly pass the `logged_metrics` dictionary to this function.

        ```python
        from mate import mate
        from pytorch_lightning import LightningModule
        from pytorch_lightning import Trainer

        pl_module = # initialize your pytorch lightning module
        trainer = Trainer()

        if mate.is_train:
            trainer.fit(pl_module)
            mate.result(pl_module.logged_metrics)

        ```


        """
        values = {
            k: (v if isinstance(v, (int, float)) else v.item())
            for k, v in values.items()
        }
        result_path = os.path.join(self.save_dir, "result.json")
        result = {}
        if os.path.exists(result_path):
            with open(result_path, "r") as f:
                result = json.load(f)
        result = result | values
        with open(result_path, "w") as f:
            json.dump(result, f)

    def results(self) -> dict[str, dict[str, float]]:
        pass

    def __init__(
        self,
        command: str,
        save_dir: str,
        checkpoint_path: str,
    ):
        self.command: str = command
        self.checkpoint_path: str = ""
        self.save_dir = save_dir
        self.checkpoint_path = os.path.join(checkpoint_path, "checkpoint.ckpt")
