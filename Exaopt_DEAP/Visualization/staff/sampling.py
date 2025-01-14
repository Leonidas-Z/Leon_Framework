from abc import abstractmethod

from Visualization.staff.population import Population


class Sampling:

    def __init__(self) -> None:
        """
        This abstract class represents any sampling strategy that can be used to create an initial population or
        an initial search point.
        """
        super().__init__()

    def do(self, problem, n_samples, pop=Population(), **kwargs):
        """
        Sample new points with problem information if necessary.

        Parameters
        ----------

        problem : :class:`~pymoo.core.problem.Problem`
            The problem to which points should be sampled. (lower and upper bounds, discrete, binary, ...)

        n_samples : int
            Number of samples

        pop : :class:`~pymoo.core.population.Population`
            The sampling results are stored in a population. The template of the population can be changed.
            If 'none' simply a numpy array is returned.

        Returns
        -------
        X : numpy.array
            Samples points in a two dimensional array

        """
        val = self._do(problem, n_samples, **kwargs)

        if pop is None:
            return val

        return Population.new("X", val)

    @abstractmethod
    def _do(self, problem, n_samples, **kwargs):
        pass



