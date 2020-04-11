import snoop
import cheap_repr
import snoop.configuration

def register(verbose=False, torch_formatter=None, numpy_formatter=None):
    try:
        import numpy
        from snoop_tensor.numpy import NumpyFormatter
        numpy_formatter = numpy_formatter or NumpyFormatter()
        cheap_repr.register_repr(numpy.ndarray)(lambda x, _: numpy_formatter(x))
    except ImportError:
        pass

    try:
        import torch
        from snoop_tensor.torch import TensorFormatter
        torch_formatter = torch_formatter or TensorFormatter()
        cheap_repr.register_repr(torch.Tensor)(lambda x, _: torch_formatter(x))
    except ImportError:
        pass

    unwanted = {
        snoop.configuration.len_shape_watch,
        snoop.configuration.dtype_watch,
    }
    snoop.config.watch_extras = tuple(x for x in snoop.config.watch_extras if x not in unwanted)
