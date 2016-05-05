from IPython.lib.backgroundjobs import BackgroundJobManager
from IPython.core.magic import register_line_magic
from IPython import get_ipython
from ipywidgets import IntProgress
from IPython.display import display

def log_progress(sequence, every=1):
    progress = IntProgress(min=0, max=len(sequence), value=0)
    display(progress)
    
    for index, record in enumerate(sequence):
        if index % every == 0:
            progress.value = index
        yield record
    progress.value = index+1

def jobs_manager():
    jobs = BackgroundJobManager()

    @register_line_magic
    def job(line):
        ip = get_ipython()
        jobs.new(line, ip.user_global_ns)

    return jobs

jobs = jobs_manager()