import numpy as np

from mayavi import mlab

from scipy.io import loadmat


def periodic_linspace(*args, **kwargs):
    """Same as np.linspace but removes the last point because periodicity
    implies that the first and last point are the same."""
    return np.linspace(*args, **kwargs)[:-1]


def wavenumbers(n, L):
    """Since these exist in the frequency domain their native form is shifted in
    the sense of they look as if they came through fft."""
    k = np.concatenate([np.arange(0, n / 2), np.arange(-n / 2, 0)])
    return (2 * np.pi / (2 * L)) * k


def isosurface(X, Y, Z, V, show=False):
    """Helper around the isosurface plotting so it looks more like matlab's
    isosurface. mlab.contour3d is built to work off of np.mgrid which returns
    the data in a different order than np.meshgrid but I want to use
    np.meshgrid so the transpose back is hidden in here."""

    def t(a):
        """Transpose to coerce np.meshgrid output match np.mgrid output. a must
        be a 3d-array."""
        return np.transpose(a, [1, 0, 2])

    fig = mlab.contour3d(t(X), t(Y), t(Z), t(V))
    if show:
        mlab.show()
    return fig


if __name__ == "__main__":
    Un = loadmat("Testdata")["Undata"]  # Un => ultasound noisy

    L = 15  # Spatial Domain
    n = 64  # Fourier Modes
    x = periodic_linspace(-L, L, n + 1)
    k = wavenumbers(n, L)
    ks = np.fft.fftshift(k)  # ks => k shifted

    X, Y, Z = np.meshgrid(x, x, x)
    Kx, Ky, Kz = np.meshgrid(ks, ks, ks)

    for row in Undata:
        row = row.reshape(n, n, n)
        isosurface(X, Y, Z, np.abs(row), show=True)
