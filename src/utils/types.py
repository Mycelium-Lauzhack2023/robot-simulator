import jaxtyping
import numpy as np

OccupancyGrid = jaxtyping.UInt8[np.ndarray, "height width"]
