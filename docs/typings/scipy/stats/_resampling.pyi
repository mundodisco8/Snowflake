"""
This type stub file was generated by pyright.
"""

__all__ = ['bootstrap', 'monte_carlo_test', 'permutation_test']
fields = ...
BootstrapResult = ...
def bootstrap(data, statistic, *, n_resamples=..., batch=..., vectorized=..., paired=..., axis=..., confidence_level=..., method=..., random_state=...): # -> Any:
    r"""
    Compute a two-sided bootstrap confidence interval of a statistic.

    When `method` is ``'percentile'``, a bootstrap confidence interval is
    computed according to the following procedure.

    1. Resample the data: for each sample in `data` and for each of
       `n_resamples`, take a random sample of the original sample
       (with replacement) of the same size as the original sample.

    2. Compute the bootstrap distribution of the statistic: for each set of
       resamples, compute the test statistic.

    3. Determine the confidence interval: find the interval of the bootstrap
       distribution that is

       - symmetric about the median and
       - contains `confidence_level` of the resampled statistic values.

    While the ``'percentile'`` method is the most intuitive, it is rarely
    used in practice. Two more common methods are available, ``'basic'``
    ('reverse percentile') and ``'BCa'`` ('bias-corrected and accelerated');
    they differ in how step 3 is performed.

    If the samples in `data` are  taken at random from their respective
    distributions :math:`n` times, the confidence interval returned by
    `bootstrap` will contain the true value of the statistic for those
    distributions approximately `confidence_level`:math:`\, \times \, n` times.

    Parameters
    ----------
    data : sequence of array-like
         Each element of data is a sample from an underlying distribution.
    statistic : callable
        Statistic for which the confidence interval is to be calculated.
        `statistic` must be a callable that accepts ``len(data)`` samples
        as separate arguments and returns the resulting statistic.
        If `vectorized` is set ``True``,
        `statistic` must also accept a keyword argument `axis` and be
        vectorized to compute the statistic along the provided `axis`.
    n_resamples : int, default: ``9999``
        The number of resamples performed to form the bootstrap distribution
        of the statistic.
    batch : int, optional
        The number of resamples to process in each vectorized call to
        `statistic`. Memory usage is O(`batch`*``n``), where ``n`` is the
        sample size. Default is ``None``, in which case ``batch = n_resamples``
        (or ``batch = max(n_resamples, n)`` for ``method='BCa'``).
    vectorized : bool, default: ``True``
        If `vectorized` is set ``False``, `statistic` will not be passed
        keyword argument `axis`, and is assumed to calculate the statistic
        only for 1D samples.
    paired : bool, default: ``False``
        Whether the statistic treats corresponding elements of the samples
        in `data` as paired.
    axis : int, default: ``0``
        The axis of the samples in `data` along which the `statistic` is
        calculated.
    confidence_level : float, default: ``0.95``
        The confidence level of the confidence interval.
    method : {'percentile', 'basic', 'bca'}, default: ``'BCa'``
        Whether to return the 'percentile' bootstrap confidence interval
        (``'percentile'``), the 'reverse' or the bias-corrected and accelerated
        bootstrap confidence interval (``'BCa'``).
        Note that only ``'percentile'`` and ``'basic'`` support multi-sample
        statistics at this time.
    random_state : {None, int, `numpy.random.Generator`,
                    `numpy.random.RandomState`}, optional

        Pseudorandom number generator state used to generate resamples.

        If `random_state` is ``None`` (or `np.random`), the
        `numpy.random.RandomState` singleton is used.
        If `random_state` is an int, a new ``RandomState`` instance is used,
        seeded with `random_state`.
        If `random_state` is already a ``Generator`` or ``RandomState``
        instance then that instance is used.

    Returns
    -------
    res : BootstrapResult
        An object with attributes:

        confidence_interval : ConfidenceInterval
            The bootstrap confidence interval as an instance of
            `collections.namedtuple` with attributes `low` and `high`.
        standard_error : float or ndarray
            The bootstrap standard error, that is, the sample standard
            deviation of the bootstrap distribution

    Warns
    -----
    `~scipy.stats.DegenerateDataWarning`
        Generated when ``method='BCa'`` and the bootstrap distribution is
        degenerate (e.g. all elements are identical).

    Notes
    -----
    Elements of the confidence interval may be NaN for ``method='BCa'`` if
    the bootstrap distribution is degenerate (e.g. all elements are identical).
    In this case, consider using another `method` or inspecting `data` for
    indications that other analysis may be more appropriate (e.g. all
    observations are identical).

    References
    ----------
    .. [1] B. Efron and R. J. Tibshirani, An Introduction to the Bootstrap,
       Chapman & Hall/CRC, Boca Raton, FL, USA (1993)
    .. [2] Nathaniel E. Helwig, "Bootstrap Confidence Intervals",
       http://users.stat.umn.edu/~helwig/notes/bootci-Notes.pdf
    .. [3] Bootstrapping (statistics), Wikipedia,
       https://en.wikipedia.org/wiki/Bootstrapping_%28statistics%29

    Examples
    --------
    Suppose we have sampled data from an unknown distribution.

    >>> import numpy as np
    >>> rng = np.random.default_rng()
    >>> from scipy.stats import norm
    >>> dist = norm(loc=2, scale=4)  # our "unknown" distribution
    >>> data = dist.rvs(size=100, random_state=rng)

    We are interested int the standard deviation of the distribution.

    >>> std_true = dist.std()      # the true value of the statistic
    >>> print(std_true)
    4.0
    >>> std_sample = np.std(data)  # the sample statistic
    >>> print(std_sample)
    3.9460644295563863

    We can calculate a 90% confidence interval of the statistic using
    `bootstrap`.

    >>> from scipy.stats import bootstrap
    >>> data = (data,)  # samples must be in a sequence
    >>> res = bootstrap(data, np.std, confidence_level=0.9,
    ...                 random_state=rng)
    >>> print(res.confidence_interval)
    ConfidenceInterval(low=3.57655333533867, high=4.382043696342881)

    If we sample from the distribution 1000 times and form a bootstrap
    confidence interval for each sample, the confidence interval
    contains the true value of the statistic approximately 900 times.

    >>> n_trials = 1000
    >>> ci_contains_true_std = 0
    >>> for i in range(n_trials):
    ...    data = (dist.rvs(size=100, random_state=rng),)
    ...    ci = bootstrap(data, np.std, confidence_level=0.9, n_resamples=1000,
    ...                   random_state=rng).confidence_interval
    ...    if ci[0] < std_true < ci[1]:
    ...        ci_contains_true_std += 1
    >>> print(ci_contains_true_std)
    875

    Rather than writing a loop, we can also determine the confidence intervals
    for all 1000 samples at once.

    >>> data = (dist.rvs(size=(n_trials, 100), random_state=rng),)
    >>> res = bootstrap(data, np.std, axis=-1, confidence_level=0.9,
    ...                 n_resamples=1000, random_state=rng)
    >>> ci_l, ci_u = res.confidence_interval

    Here, `ci_l` and `ci_u` contain the confidence interval for each of the
    ``n_trials = 1000`` samples.

    >>> print(ci_l[995:])
    [3.77729695 3.75090233 3.45829131 3.34078217 3.48072829]
    >>> print(ci_u[995:])
    [4.88316666 4.86924034 4.32032996 4.2822427  4.59360598]

    And again, approximately 90% contain the true value, ``std_true = 4``.

    >>> print(np.sum((ci_l < std_true) & (std_true < ci_u)))
    900

    `bootstrap` can also be used to estimate confidence intervals of
    multi-sample statistics, including those calculated by hypothesis
    tests. `scipy.stats.mood` perform's Mood's test for equal scale parameters,
    and it returns two outputs: a statistic, and a p-value. To get a
    confidence interval for the test statistic, we first wrap
    `scipy.stats.mood` in a function that accepts two sample arguments,
    accepts an `axis` keyword argument, and returns only the statistic.

    >>> from scipy.stats import mood
    >>> def my_statistic(sample1, sample2, axis):
    ...     statistic, _ = mood(sample1, sample2, axis=-1)
    ...     return statistic

    Here, we use the 'percentile' method with the default 95% confidence level.

    >>> sample1 = norm.rvs(scale=1, size=100, random_state=rng)
    >>> sample2 = norm.rvs(scale=2, size=100, random_state=rng)
    >>> data = (sample1, sample2)
    >>> res = bootstrap(data, my_statistic, method='basic', random_state=rng)
    >>> print(mood(sample1, sample2)[0])  # element 0 is the statistic
    -5.521109549096542
    >>> print(res.confidence_interval)
    ConfidenceInterval(low=-7.255994487314675, high=-4.016202624747605)

    The bootstrap estimate of the standard error is also available.

    >>> print(res.standard_error)
    0.8344963846318795

    Paired-sample statistics work, too. For example, consider the Pearson
    correlation coefficient.

    >>> from scipy.stats import pearsonr
    >>> n = 100
    >>> x = np.linspace(0, 10, n)
    >>> y = x + rng.uniform(size=n)
    >>> print(pearsonr(x, y)[0])  # element 0 is the statistic
    0.9962357936065914

    We wrap `pearsonr` so that it returns only the statistic.

    >>> def my_statistic(x, y):
    ...     return pearsonr(x, y)[0]

    We call `bootstrap` using ``paired=True``.
    Also, since ``my_statistic`` isn't vectorized to calculate the statistic
    along a given axis, we pass in ``vectorized=False``.

    >>> res = bootstrap((x, y), my_statistic, vectorized=False, paired=True,
    ...                 random_state=rng)
    >>> print(res.confidence_interval)
    ConfidenceInterval(low=0.9950085825848624, high=0.9971212407917498)

    """
    ...

fields = ...
MonteCarloTestResult = ...
def monte_carlo_test(sample, rvs, statistic, *, vectorized=..., n_resamples=..., batch=..., alternative=..., axis=...): # -> Any:
    r"""
    Monte Carlo test that a sample is drawn from a given distribution.

    The null hypothesis is that the provided `sample` was drawn at random from
    the distribution for which `rvs` generates random variates. The value of
    the `statistic` for the given sample is compared against a Monte Carlo null
    distribution: the value of the statistic for each of `n_resamples`
    samples generated by `rvs`. This gives the p-value, the probability of
    observing such an extreme value of the test statistic under the null
    hypothesis.

    Parameters
    ----------
    sample : array-like
        An array of observations.
    rvs : callable
        Generates random variates from the distribution against which `sample`
        will be tested. `rvs` must be a callable that accepts keyword argument
        ``size`` (e.g. ``rvs(size=(m, n))``) and returns an N-d array sample
        of that shape.
    statistic : callable
        Statistic for which the p-value of the hypothesis test is to be
        calculated. `statistic` must be a callable that accepts a sample
        (e.g. ``statistic(sample)``) and returns the resulting statistic.
        If `vectorized` is set ``True``, `statistic` must also accept a keyword
        argument `axis` and be vectorized to compute the statistic along the
        provided `axis` of the sample array.
    vectorized : bool, default: ``False``
        By default, `statistic` is assumed to calculate the statistic only for
        a 1D arrays `sample`. If `vectorized` is set ``True``, `statistic` must
        also accept a keyword argument `axis` and be vectorized to compute the
        statistic along the provided `axis` of an ND sample array. Use of a
        vectorized statistic can reduce computation time.
    n_resamples : int, default: 9999
        Number of random permutations used to approximate the Monte Carlo null
        distribution.
    batch : int, optional
        The number of permutations to process in each call to `statistic`.
        Memory usage is O(`batch`*``sample.size[axis]``). Default is
        ``None``, in which case `batch` equals `n_resamples`.
    alternative : {'two-sided', 'less', 'greater'}
        The alternative hypothesis for which the p-value is calculated.
        For each alternative, the p-value is defined as follows.

        - ``'greater'`` : the percentage of the null distribution that is
          greater than or equal to the observed value of the test statistic.
        - ``'less'`` : the percentage of the null distribution that is
          less than or equal to the observed value of the test statistic.
        - ``'two-sided'`` : twice the smaller of the p-values above.

    axis : int, default: 0
        The axis of `sample` over which to calculate the statistic.

    Returns
    -------
    statistic : float or ndarray
        The observed test statistic of the sample.
    pvalue : float or ndarray
        The p-value for the given alternative.
    null_distribution : ndarray
        The values of the test statistic generated under the null hypothesis.

    References
    ----------

    .. [1] B. Phipson and G. K. Smyth. "Permutation P-values Should Never Be
       Zero: Calculating Exact P-values When Permutations Are Randomly Drawn."
       Statistical Applications in Genetics and Molecular Biology 9.1 (2010).

    Examples
    --------

    Suppose we wish to test whether a small sample has been drawn from a normal
    distribution. We decide that we will use the skew of the sample as a
    test statistic, and we will consider a p-value of 0.05 to be statistically
    significant.

    >>> import numpy as np
    >>> from scipy import stats
    >>> def statistic(x, axis):
    ...     return stats.skew(x, axis)

    After collecting our data, we calculate the observed value of the test
    statistic.

    >>> rng = np.random.default_rng()
    >>> x = stats.skewnorm.rvs(a=1, size=50, random_state=rng)
    >>> statistic(x, axis=0)
    0.12457412450240658

    To determine the probability of observing such an extreme value of the
    skewness by chance if the sample were drawn from the normal distribution,
    we can perform a Monte Carlo hypothesis test. The test will draw many
    samples at random from their normal distribution, calculate the skewness
    of each sample, and compare our original skewness against this
    distribution to determine an approximate p-value.

    >>> from scipy.stats import monte_carlo_test
    >>> # because our statistic is vectorized, we pass `vectorized=True`
    >>> rvs = lambda size: stats.norm.rvs(size=size, random_state=rng)
    >>> res = monte_carlo_test(x, rvs, statistic, vectorized=True)
    >>> print(res.statistic)
    0.12457412450240658
    >>> print(res.pvalue)
    0.7012

    The probability of obtaining a test statistic less than or equal to the
    observed value under the null hypothesis is ~70%. This is greater than
    our chosen threshold of 5%, so we cannot consider this to to be significant
    evidence against the null hypothesis.

    Note that this p-value essentially matches that of
    `scipy.stats.skewtest`, which relies on an asymptotic distribution of a
    test statistic based on the sample skewness.

    >>> stats.skewtest(x).pvalue
    0.6892046027110614

    This asymptotic approximation is not valid for small sample sizes, but
    `monte_carlo_test` can be used with samples of any size.

    >>> x = stats.skewnorm.rvs(a=1, size=7, random_state=rng)
    >>> # stats.skewtest(x) would produce an error due to small sample
    >>> res = monte_carlo_test(x, rvs, statistic, vectorized=True)

    The Monte Carlo distribution of the test statistic is provided for
    further investigation.

    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> ax.hist(res.null_distribution, bins=50)
    >>> ax.set_title("Monte Carlo distribution of test statistic")
    >>> ax.set_xlabel("Value of Statistic")
    >>> ax.set_ylabel("Frequency")
    >>> plt.show()

    """
    ...

attributes = ...
PermutationTestResult = ...
def permutation_test(data, statistic, *, permutation_type=..., vectorized=..., n_resamples=..., batch=..., alternative=..., axis=..., random_state=...): # -> Any:
    r"""
    Performs a permutation test of a given statistic on provided data.

    For independent sample statistics, the null hypothesis is that the data are
    randomly sampled from the same distribution.
    For paired sample statistics, two null hypothesis can be tested:
    that the data are paired at random or that the data are assigned to samples
    at random.

    Parameters
    ----------
    data : iterable of array-like
        Contains the samples, each of which is an array of observations.
        Dimensions of sample arrays must be compatible for broadcasting except
        along `axis`.
    statistic : callable
        Statistic for which the p-value of the hypothesis test is to be
        calculated. `statistic` must be a callable that accepts samples
        as separate arguments (e.g. ``statistic(*data)``) and returns the
        resulting statistic.
        If `vectorized` is set ``True``, `statistic` must also accept a keyword
        argument `axis` and be vectorized to compute the statistic along the
        provided `axis` of the sample arrays.
    permutation_type : {'independent', 'samples', 'pairings'}, optional
        The type of permutations to be performed, in accordance with the
        null hypothesis. The first two permutation types are for paired sample
        statistics, in which all samples contain the same number of
        observations and observations with corresponding indices along `axis`
        are considered to be paired; the third is for independent sample
        statistics.

        - ``'samples'`` : observations are assigned to different samples
          but remain paired with the same observations from other samples.
          This permutation type is appropriate for paired sample hypothesis
          tests such as the Wilcoxon signed-rank test and the paired t-test.
        - ``'pairings'`` : observations are paired with different observations,
          but they remain within the same sample. This permutation type is
          appropriate for association/correlation tests with statistics such
          as Spearman's :math:`\rho`, Kendall's :math:`\tau`, and Pearson's
          :math:`r`.
        - ``'independent'`` (default) : observations are assigned to different
          samples. Samples may contain different numbers of observations. This
          permutation type is appropriate for independent sample hypothesis
          tests such as the Mann-Whitney :math:`U` test and the independent
          sample t-test.

          Please see the Notes section below for more detailed descriptions
          of the permutation types.

    vectorized : bool, default: ``False``
        By default, `statistic` is assumed to calculate the statistic only for
        1D arrays contained in `data`. If `vectorized` is set ``True``,
        `statistic` must also accept a keyword argument `axis` and be
        vectorized to compute the statistic along the provided `axis` of the ND
        arrays in `data`. Use of a vectorized statistic can reduce computation
        time.
    n_resamples : int or np.inf, default: 9999
        Number of random permutations (resamples) used to approximate the null
        distribution. If greater than or equal to the number of distinct
        permutations, the exact null distribution will be computed.
        Note that the number of distinct permutations grows very rapidly with
        the sizes of samples, so exact tests are feasible only for very small
        data sets.
    batch : int, optional
        The number of permutations to process in each call to `statistic`.
        Memory usage is O(`batch`*``n``), where ``n`` is the total size
        of all samples, regardless of the value of `vectorized`. Default is
        ``None``, in which case ``batch`` is the number of permutations.
    alternative : {'two-sided', 'less', 'greater'}, optional
        The alternative hypothesis for which the p-value is calculated.
        For each alternative, the p-value is defined for exact tests as
        follows.

        - ``'greater'`` : the percentage of the null distribution that is
          greater than or equal to the observed value of the test statistic.
        - ``'less'`` : the percentage of the null distribution that is
          less than or equal to the observed value of the test statistic.
        - ``'two-sided'`` (default) : twice the smaller of the p-values above.

        Note that p-values for randomized tests are calculated according to the
        conservative (over-estimated) approximation suggested in [2]_ and [3]_
        rather than the unbiased estimator suggested in [4]_. That is, when
        calculating the proportion of the randomized null distribution that is
        as extreme as the observed value of the test statistic, the values in
        the numerator and denominator are both increased by one. An
        interpretation of this adjustment is that the observed value of the
        test statistic is always included as an element of the randomized
        null distribution.
        The convention used for two-sided p-values is not universal;
        the observed test statistic and null distribution are returned in
        case a different definition is preferred.

    axis : int, default: 0
        The axis of the (broadcasted) samples over which to calculate the
        statistic. If samples have a different number of dimensions,
        singleton dimensions are prepended to samples with fewer dimensions
        before `axis` is considered.
    random_state : {None, int, `numpy.random.Generator`,
                    `numpy.random.RandomState`}, optional

        Pseudorandom number generator state used to generate permutations.

        If `random_state` is ``None`` (default), the
        `numpy.random.RandomState` singleton is used.
        If `random_state` is an int, a new ``RandomState`` instance is used,
        seeded with `random_state`.
        If `random_state` is already a ``Generator`` or ``RandomState``
        instance then that instance is used.

    Returns
    -------
    statistic : float or ndarray
        The observed test statistic of the data.
    pvalue : float or ndarray
        The p-value for the given alternative.
    null_distribution : ndarray
        The values of the test statistic generated under the null hypothesis.

    Notes
    -----

    The three types of permutation tests supported by this function are
    described below.

    **Unpaired statistics** (``permutation_type='independent'``):

    The null hypothesis associated with this permutation type is that all
    observations are sampled from the same underlying distribution and that
    they have been assigned to one of the samples at random.

    Suppose ``data`` contains two samples; e.g. ``a, b = data``.
    When ``1 < n_resamples < binom(n, k)``, where

    * ``k`` is the number of observations in ``a``,
    * ``n`` is the total number of observations in ``a`` and ``b``, and
    * ``binom(n, k)`` is the binomial coefficient (``n`` choose ``k``),

    the data are pooled (concatenated), randomly assigned to either the first
    or second sample, and the statistic is calculated. This process is
    performed repeatedly, `permutation` times, generating a distribution of the
    statistic under the null hypothesis. The statistic of the original
    data is compared to this distribution to determine the p-value.

    When ``n_resamples >= binom(n, k)``, an exact test is performed: the data
    are *partitioned* between the samples in each distinct way exactly once,
    and the exact null distribution is formed.
    Note that for a given partitioning of the data between the samples,
    only one ordering/permutation of the data *within* each sample is
    considered. For statistics that do not depend on the order of the data
    within samples, this dramatically reduces computational cost without
    affecting the shape of the null distribution (because the frequency/count
    of each value is affected by the same factor).

    For ``a = [a1, a2, a3, a4]`` and ``b = [b1, b2, b3]``, an example of this
    permutation type is ``x = [b3, a1, a2, b2]`` and ``y = [a4, b1, a3]``.
    Because only one ordering/permutation of the data *within* each sample
    is considered in an exact test, a resampling like ``x = [b3, a1, b2, a2]``
    and ``y = [a4, a3, b1]`` would *not* be considered distinct from the
    example above.

    ``permutation_type='independent'`` does not support one-sample statistics,
    but it can be applied to statistics with more than two samples. In this
    case, if ``n`` is an array of the number of observations within each
    sample, the number of distinct partitions is::

        np.product([binom(sum(n[i:]), sum(n[i+1:])) for i in range(len(n)-1)])

    **Paired statistics, permute pairings** (``permutation_type='pairings'``):

    The null hypothesis associated with this permutation type is that
    observations within each sample are drawn from the same underlying
    distribution and that pairings with elements of other samples are
    assigned at random.

    Suppose ``data`` contains only one sample; e.g. ``a, = data``, and we
    wish to consider all possible pairings of elements of ``a`` with elements
    of a second sample, ``b``. Let ``n`` be the number of observations in
    ``a``, which must also equal the number of observations in ``b``.

    When ``1 < n_resamples < factorial(n)``, the elements of ``a`` are
    randomly permuted. The user-supplied statistic accepts one data argument,
    say ``a_perm``, and calculates the statistic considering ``a_perm`` and
    ``b``. This process is performed repeatedly, `permutation` times,
    generating a distribution of the statistic under the null hypothesis.
    The statistic of the original data is compared to this distribution to
    determine the p-value.

    When ``n_resamples >= factorial(n)``, an exact test is performed:
    ``a`` is permuted in each distinct way exactly once. Therefore, the
    `statistic` is computed for each unique pairing of samples between ``a``
    and ``b`` exactly once.

    For ``a = [a1, a2, a3]`` and ``b = [b1, b2, b3]``, an example of this
    permutation type is ``a_perm = [a3, a1, a2]`` while ``b`` is left
    in its original order.

    ``permutation_type='pairings'`` supports ``data`` containing any number
    of samples, each of which must contain the same number of observations.
    All samples provided in ``data`` are permuted *independently*. Therefore,
    if ``m`` is the number of samples and ``n`` is the number of observations
    within each sample, then the number of permutations in an exact test is::

        factorial(n)**m

    Note that if a two-sample statistic, for example, does not inherently
    depend on the order in which observations are provided - only on the
    *pairings* of observations - then only one of the two samples should be
    provided in ``data``. This dramatically reduces computational cost without
    affecting the shape of the null distribution (because the frequency/count
    of each value is affected by the same factor).

    **Paired statistics, permute samples** (``permutation_type='samples'``):

    The null hypothesis associated with this permutation type is that
    observations within each pair are drawn from the same underlying
    distribution and that the sample to which they are assigned is random.

    Suppose ``data`` contains two samples; e.g. ``a, b = data``.
    Let ``n`` be the number of observations in ``a``, which must also equal
    the number of observations in ``b``.

    When ``1 < n_resamples < 2**n``, the elements of ``a`` are ``b`` are
    randomly swapped between samples (maintaining their pairings) and the
    statistic is calculated. This process is performed repeatedly,
    `permutation` times,  generating a distribution of the statistic under the
    null hypothesis. The statistic of the original data is compared to this
    distribution to determine the p-value.

    When ``n_resamples >= 2**n``, an exact test is performed: the observations
    are assigned to the two samples in each distinct way (while maintaining
    pairings) exactly once.

    For ``a = [a1, a2, a3]`` and ``b = [b1, b2, b3]``, an example of this
    permutation type is ``x = [b1, a2, b3]`` and ``y = [a1, b2, a3]``.

    ``permutation_type='samples'`` supports ``data`` containing any number
    of samples, each of which must contain the same number of observations.
    If ``data`` contains more than one sample, paired observations within
    ``data`` are exchanged between samples *independently*. Therefore, if ``m``
    is the number of samples and ``n`` is the number of observations within
    each sample, then the number of permutations in an exact test is::

        factorial(m)**n

    Several paired-sample statistical tests, such as the Wilcoxon signed rank
    test and paired-sample t-test, can be performed considering only the
    *difference* between two paired elements. Accordingly, if ``data`` contains
    only one sample, then the null distribution is formed by independently
    changing the *sign* of each observation.

    .. warning::
        The p-value is calculated by counting the elements of the null
        distribution that are as extreme or more extreme than the observed
        value of the statistic. Due to the use of finite precision arithmetic,
        some statistic functions return numerically distinct values when the
        theoretical values would be exactly equal. In some cases, this could
        lead to a large error in the calculated p-value. `permutation_test`
        guards against this by considering elements in the null distribution
        that are "close" (within a factor of ``1+1e-14``) to the observed
        value of the test statistic as equal to the observed value of the
        test statistic. However, the user is advised to inspect the null
        distribution to assess whether this method of comparison is
        appropriate, and if not, calculate the p-value manually. See example
        below.

    References
    ----------

    .. [1] R. A. Fisher. The Design of Experiments, 6th Ed (1951).
    .. [2] B. Phipson and G. K. Smyth. "Permutation P-values Should Never Be
       Zero: Calculating Exact P-values When Permutations Are Randomly Drawn."
       Statistical Applications in Genetics and Molecular Biology 9.1 (2010).
    .. [3] M. D. Ernst. "Permutation Methods: A Basis for Exact Inference".
       Statistical Science (2004).
    .. [4] B. Efron and R. J. Tibshirani. An Introduction to the Bootstrap
       (1993).

    Examples
    --------

    Suppose we wish to test whether two samples are drawn from the same
    distribution. Assume that the underlying distributions are unknown to us,
    and that before observing the data, we hypothesized that the mean of the
    first sample would be less than that of the second sample. We decide that
    we will use the difference between the sample means as a test statistic,
    and we will consider a p-value of 0.05 to be statistically significant.

    For efficiency, we write the function defining the test statistic in a
    vectorized fashion: the samples ``x`` and ``y`` can be ND arrays, and the
    statistic will be calculated for each axis-slice along `axis`.

    >>> def statistic(x, y, axis):
    ...     return np.mean(x, axis=axis) - np.mean(y, axis=axis)

    After collecting our data, we calculate the observed value of the test
    statistic.

    >>> from scipy.stats import norm
    >>> rng = np.random.default_rng()
    >>> x = norm.rvs(size=5, random_state=rng)
    >>> y = norm.rvs(size=6, loc = 3, random_state=rng)
    >>> statistic(x, y, 0)
    -3.5411688580987266

    Indeed, the test statistic is negative, suggesting that the true mean of
    the distribution underlying ``x`` is less than that of the distribution
    underlying ``y``. To determine the probability of this occuring by chance
    if the two samples were drawn from the same distribution, we perform
    a permutation test.

    >>> from scipy.stats import permutation_test
    >>> # because our statistic is vectorized, we pass `vectorized=True`
    >>> # `n_resamples=np.inf` indicates that an exact test is to be performed
    >>> res = permutation_test((x, y), statistic, vectorized=True,
    ...                        n_resamples=np.inf, alternative='less')
    >>> print(res.statistic)
    -3.5411688580987266
    >>> print(res.pvalue)
    0.004329004329004329

    The probability of obtaining a test statistic less than or equal to the
    observed value under the null hypothesis is 0.4329%. This is less than our
    chosen threshold of 5%, so we consider this to to be significant evidence
    against the null hypothesis in favor of the alternative.

    Because the size of the samples above was small, `permutation_test` could
    perform an exact test. For larger samples, we resort to a randomized
    permutation test.

    >>> x = norm.rvs(size=100, random_state=rng)
    >>> y = norm.rvs(size=120, loc=0.3, random_state=rng)
    >>> res = permutation_test((x, y), statistic, n_resamples=100000,
    ...                        vectorized=True, alternative='less',
    ...                        random_state=rng)
    >>> print(res.statistic)
    -0.5230459671240913
    >>> print(res.pvalue)
    0.00016999830001699983

    The approximate probability of obtaining a test statistic less than or
    equal to the observed value under the null hypothesis is 0.0225%. This is
    again less than our chosen threshold of 5%, so again we have significant
    evidence to reject the null hypothesis in favor of the alternative.

    For large samples and number of permutations, the result is comparable to
    that of the corresponding asymptotic test, the independent sample t-test.

    >>> from scipy.stats import ttest_ind
    >>> res_asymptotic = ttest_ind(x, y, alternative='less')
    >>> print(res_asymptotic.pvalue)
    0.00012688101537979522

    The permutation distribution of the test statistic is provided for
    further investigation.

    >>> import matplotlib.pyplot as plt
    >>> plt.hist(res.null_distribution, bins=50)
    >>> plt.title("Permutation distribution of test statistic")
    >>> plt.xlabel("Value of Statistic")
    >>> plt.ylabel("Frequency")
    >>> plt.show()

    Inspection of the null distribution is essential if the statistic suffers
    from inaccuracy due to limited machine precision. Consider the following
    case:

    >>> from scipy.stats import pearsonr
    >>> x = [1, 2, 4, 3]
    >>> y = [2, 4, 6, 8]
    >>> def statistic(x, y):
    ...     return pearsonr(x, y).statistic
    >>> res = permutation_test((x, y), statistic, vectorized=False,
    ...                        permutation_type='pairings',
    ...                        alternative='greater')
    >>> r, pvalue, null = res.statistic, res.pvalue, res.null_distribution

    In this case, some elements of the null distribution differ from the
    observed value of the correlation coefficient ``r`` due to numerical noise.
    We manually inspect the elements of the null distribution that are nearly
    the same as the observed value of the test statistic.

    >>> r
    0.8
    >>> unique = np.unique(null)
    >>> unique
    array([-1. , -0.8, -0.8, -0.6, -0.4, -0.2, -0.2,  0. ,  0.2,  0.2,  0.4,
            0.6,  0.8,  0.8,  1. ]) # may vary
    >>> unique[np.isclose(r, unique)].tolist()
    [0.7999999999999999, 0.8]

    If `permutation_test` were to perform the comparison naively, the
    elements of the null distribution with value ``0.7999999999999999`` would
    not be considered as extreme or more extreme as the observed value of the
    statistic, so the calculated p-value would be too small.

    >>> incorrect_pvalue = np.count_nonzero(null >= r) / len(null)
    >>> incorrect_pvalue
    0.1111111111111111  # may vary

    Instead, `permutation_test` treats elements of the null distribution that
    are within ``max(1e-14, abs(r)*1e-14)`` of the observed value of the
    statistic ``r`` to be equal to ``r``.

    >>> correct_pvalue = np.count_nonzero(null >= r - 1e-14) / len(null)
    >>> correct_pvalue
    0.16666666666666666
    >>> res.pvalue == correct_pvalue
    True

    This method of comparison is expected to be accurate in most practical
    situations, but the user is advised to assess this by inspecting the
    elements of the null distribution that are close to the observed value
    of the statistic. Also, consider the use of statistics that can be
    calculated using exact arithmetic (e.g. integer statistics).

    """
    ...

