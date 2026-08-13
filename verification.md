# Numerical verification

The following verifies the estimator results numerically for a Gaussian distribution with a fixed mean and variance ($\mu = 0.3$, $\sigma = 1.2$), and a fixed observation ($y = 1.0$). We take 10,000 replicates of `n_samples` from the Gaussian and calculate the average value of the plug-in and fair estimators, and their biases against the exact CRPS of the distribution.

This verifies the [bias of the plug-in estimator](proofs/plugin-crps-is-biased.md) and the [unbiasedness of fCRPS](proofs/fcrps-is-unbiased.md) against the [Gaussian closed form](proofs/gaussian-crps.md).

|   n_samples |    exact |   plugin |     fair |   plugin_error |   exact_plugin_bias |   fair_error |   exact_fair_bias |
|------------:|---------:|---------:|---------:|---------------:|--------------------:|-------------:|------------------:|
|           2 | 0.438869 | 0.770898 | 0.436371 |      0.33203   |           0.338514  | -0.00249742  |                 0 |
|           3 | 0.438869 | 0.662483 | 0.441356 |      0.223615  |           0.225676  |  0.00248689  |                 0 |
|           5 | 0.438869 | 0.573736 | 0.43601  |      0.134868  |           0.135406  | -0.00285887  |                 0 |
|          10 | 0.438869 | 0.506307 | 0.437776 |      0.067438  |           0.0677028 | -0.00109254  |                 0 |
|          20 | 0.438869 | 0.471392 | 0.439089 |      0.0325234 |           0.0338514 |  0.000220118 |                 0 |
|          50 | 0.438869 | 0.452286 | 0.438299 |      0.0134176 |           0.0135406 | -0.000569949 |                 0 |

Regenerate: `python scripts/verify_estimators.py`
