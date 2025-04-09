from pathlib import Path

def get_project_root() -> Path:
    """
    Used to obtain the root directory of the project.
    """
    return Path(__file__).parent.resolve()

def get_plot_output_dir() -> Path:
    """
    Used to creat a directory to save relevant plots
    """
    path = get_project_root() / "output_plots"
    path.mkdir(exist_ok=True)
    return path

def get_model_dir() -> Path:
    """
    Used to creat a directory to save trained model
    """
    path = get_project_root() / "models"
    path.mkdir(exist_ok = True)
    return path

def get_logs_dir() -> Path:
    """
    Used to creat a directory to save model registry logs.
    """
    path = get_project_root() / "logs"
    path.mkdir(exist_ok = True)
    return path
