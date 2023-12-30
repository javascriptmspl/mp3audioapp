import time
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

class TimingMixin:
    """
    A mixin that logs the time taken to execute a view.
    """

    @method_decorator(sensitive_post_parameters())  # Optional decorator for added sensitivity
    def dispatch(self, request, *args, **kwargs):
        start_time = time.time()

        # Call the actual view
        response = super().dispatch(request, *args, **kwargs)

        end_time = time.time()
        elapsed_time = end_time - start_time

        self.log_timing(request, elapsed_time)

        return response

    def log_timing(self, request, elapsed_time):
        """
        Placeholder for logging timing information.
        Override this method in your views to customize logging.
        """
        print(f"View '{self.__class__.__name__}' took {elapsed_time:.6f} seconds to execute.")
        return (f"View '{self.__class__.__name__}' took {elapsed_time:.6f} seconds to execute.")
