"""
This type stub file was generated by pyright.
"""

import numpy.typing as npt
from typing import Any, TYPE_CHECKING

"""
Collection of physical constants and conversion factors.

Most constants are in SI units, so you can do
print '10 mile per minute is', 10*mile/minute, 'm/s or', 10*mile/(minute*knot), 'knots'

The list is not meant to be comprehensive, but just convenient for everyday use.
"""
if TYPE_CHECKING:
    ...
__all__ = ['Avogadro', 'Boltzmann', 'Btu', 'Btu_IT', 'Btu_th', 'G', 'Julian_year', 'N_A', 'Planck', 'R', 'Rydberg', 'Stefan_Boltzmann', 'Wien', 'acre', 'alpha', 'angstrom', 'arcmin', 'arcminute', 'arcsec', 'arcsecond', 'astronomical_unit', 'atm', 'atmosphere', 'atomic_mass', 'atto', 'au', 'bar', 'barrel', 'bbl', 'blob', 'c', 'calorie', 'calorie_IT', 'calorie_th', 'carat', 'centi', 'convert_temperature', 'day', 'deci', 'degree', 'degree_Fahrenheit', 'deka', 'dyn', 'dyne', 'e', 'eV', 'electron_mass', 'electron_volt', 'elementary_charge', 'epsilon_0', 'erg', 'exa', 'exbi', 'femto', 'fermi', 'fine_structure', 'fluid_ounce', 'fluid_ounce_US', 'fluid_ounce_imp', 'foot', 'g', 'gallon', 'gallon_US', 'gallon_imp', 'gas_constant', 'gibi', 'giga', 'golden', 'golden_ratio', 'grain', 'gram', 'gravitational_constant', 'h', 'hbar', 'hectare', 'hecto', 'horsepower', 'hour', 'hp', 'inch', 'k', 'kgf', 'kibi', 'kilo', 'kilogram_force', 'kmh', 'knot', 'lambda2nu', 'lb', 'lbf', 'light_year', 'liter', 'litre', 'long_ton', 'm_e', 'm_n', 'm_p', 'm_u', 'mach', 'mebi', 'mega', 'metric_ton', 'micro', 'micron', 'mil', 'mile', 'milli', 'minute', 'mmHg', 'mph', 'mu_0', 'nano', 'nautical_mile', 'neutron_mass', 'nu2lambda', 'ounce', 'oz', 'parsec', 'pebi', 'peta', 'pi', 'pico', 'point', 'pound', 'pound_force', 'proton_mass', 'psi', 'pt', 'short_ton', 'sigma', 'slinch', 'slug', 'speed_of_light', 'speed_of_sound', 'stone', 'survey_foot', 'survey_mile', 'tebi', 'tera', 'ton_TNT', 'torr', 'troy_ounce', 'troy_pound', 'u', 'week', 'yard', 'year', 'yobi', 'yocto', 'yotta', 'zebi', 'zepto', 'zero_Celsius', 'zetta']
pi = ...
golden = ...
yotta = ...
zetta = ...
exa = ...
peta = ...
tera = ...
giga = ...
mega = ...
kilo = ...
hecto = ...
deka = ...
deci = ...
centi = ...
milli = ...
micro = ...
nano = ...
pico = ...
femto = ...
atto = ...
zepto = ...
yocto = ...
kibi = ...
mebi = ...
gibi = 2 ** 30
tebi = 2 ** 40
pebi = 2 ** 50
exbi = 2 ** 60
zebi = 2 ** 70
yobi = 2 ** 80
c = ...
mu_0 = ...
epsilon_0 = ...
h = ...
hbar = ...
G = ...
g = ...
e = ...
R = ...
alpha = ...
N_A = ...
k = ...
sigma = ...
Wien = ...
Rydberg = ...
gram = ...
metric_ton = ...
grain = ...
lb = ...
blob = ...
slug = ...
oz = ...
stone = ...
long_ton = ...
short_ton = ...
troy_ounce = ...
troy_pound = ...
carat = ...
m_e = ...
m_p = ...
m_n = ...
m_u = ...
degree = ...
arcmin = ...
arcsec = ...
minute = ...
hour = ...
day = ...
week = ...
year = ...
Julian_year = ...
inch = ...
foot = ...
yard = ...
mile = ...
mil = ...
pt = ...
survey_foot = ...
survey_mile = ...
nautical_mile = ...
fermi = ...
angstrom = ...
micron = ...
au = ...
light_year = ...
parsec = ...
atm = ...
bar = ...
torr = ...
psi = ...
hectare = ...
acre = ...
litre = ...
gallon = ...
fluid_ounce = ...
bbl = ...
gallon_imp = ...
fluid_ounce_imp = ...
kmh = ...
mph = ...
mach = ...
knot = ...
zero_Celsius = ...
degree_Fahrenheit = ...
eV = ...
calorie = ...
calorie_IT = ...
erg = ...
Btu_th = ...
Btu = ...
ton_TNT = ...
hp = ...
dyn = ...
lbf = ...
kgf = ...
def convert_temperature(val: npt.ArrayLike, old_scale: str, new_scale: str) -> Any:
    """
    Convert from a temperature scale to another one among Celsius, Kelvin,
    Fahrenheit, and Rankine scales.

    Parameters
    ----------
    val : array_like
        Value(s) of the temperature(s) to be converted expressed in the
        original scale.
    old_scale : str
        Specifies as a string the original scale from which the temperature
        value(s) will be converted. Supported scales are Celsius ('Celsius',
        'celsius', 'C' or 'c'), Kelvin ('Kelvin', 'kelvin', 'K', 'k'),
        Fahrenheit ('Fahrenheit', 'fahrenheit', 'F' or 'f'), and Rankine
        ('Rankine', 'rankine', 'R', 'r').
    new_scale : str
        Specifies as a string the new scale to which the temperature
        value(s) will be converted. Supported scales are Celsius ('Celsius',
        'celsius', 'C' or 'c'), Kelvin ('Kelvin', 'kelvin', 'K', 'k'),
        Fahrenheit ('Fahrenheit', 'fahrenheit', 'F' or 'f'), and Rankine
        ('Rankine', 'rankine', 'R', 'r').

    Returns
    -------
    res : float or array of floats
        Value(s) of the converted temperature(s) expressed in the new scale.

    Notes
    -----
    .. versionadded:: 0.18.0

    Examples
    --------
    >>> from scipy.constants import convert_temperature
    >>> convert_temperature(np.array([-40, 40]), 'Celsius', 'Kelvin')
    array([ 233.15,  313.15])

    """
    ...

def lambda2nu(lambda_: npt.ArrayLike) -> Any:
    """
    Convert wavelength to optical frequency

    Parameters
    ----------
    lambda_ : array_like
        Wavelength(s) to be converted.

    Returns
    -------
    nu : float or array of floats
        Equivalent optical frequency.

    Notes
    -----
    Computes ``nu = c / lambda`` where c = 299792458.0, i.e., the
    (vacuum) speed of light in meters/second.

    Examples
    --------
    >>> from scipy.constants import lambda2nu, speed_of_light
    >>> lambda2nu(np.array((1, speed_of_light)))
    array([  2.99792458e+08,   1.00000000e+00])

    """
    ...

def nu2lambda(nu: npt.ArrayLike) -> Any:
    """
    Convert optical frequency to wavelength.

    Parameters
    ----------
    nu : array_like
        Optical frequency to be converted.

    Returns
    -------
    lambda : float or array of floats
        Equivalent wavelength(s).

    Notes
    -----
    Computes ``lambda = c / nu`` where c = 299792458.0, i.e., the
    (vacuum) speed of light in meters/second.

    Examples
    --------
    >>> from scipy.constants import nu2lambda, speed_of_light
    >>> nu2lambda(np.array((1, speed_of_light)))
    array([  2.99792458e+08,   1.00000000e+00])

    """
    ...

