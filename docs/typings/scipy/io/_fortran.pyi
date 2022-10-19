"""
This type stub file was generated by pyright.
"""

"""
Module to read / write Fortran unformatted sequential files.

This is in the spirit of code written by Neil Martinsen-Burrell and Joe Zuntz.

"""
__all__ = ['FortranFile', 'FortranEOFError', 'FortranFormattingError']
class FortranEOFError(TypeError, OSError):
    """Indicates that the file ended properly.

    This error descends from TypeError because the code used to raise
    TypeError (and this was the only way to know that the file had
    ended) so users might have ``except TypeError:``.

    """
    ...


class FortranFormattingError(TypeError, OSError):
    """Indicates that the file ended mid-record.

    Descends from TypeError for backward compatibility.

    """
    ...


class FortranFile:
    """
    A file object for unformatted sequential files from Fortran code.

    Parameters
    ----------
    filename : file or str
        Open file object or filename.
    mode : {'r', 'w'}, optional
        Read-write mode, default is 'r'.
    header_dtype : dtype, optional
        Data type of the header. Size and endiness must match the input/output file.

    Notes
    -----
    These files are broken up into records of unspecified types. The size of
    each record is given at the start (although the size of this header is not
    standard) and the data is written onto disk without any formatting. Fortran
    compilers supporting the BACKSPACE statement will write a second copy of
    the size to facilitate backwards seeking.

    This class only supports files written with both sizes for the record.
    It also does not support the subrecords used in Intel and gfortran compilers
    for records which are greater than 2GB with a 4-byte header.

    An example of an unformatted sequential file in Fortran would be written as::

        OPEN(1, FILE=myfilename, FORM='unformatted')

        WRITE(1) myvariable

    Since this is a non-standard file format, whose contents depend on the
    compiler and the endianness of the machine, caution is advised. Files from
    gfortran 4.8.0 and gfortran 4.1.2 on x86_64 are known to work.

    Consider using Fortran direct-access files or files from the newer Stream
    I/O, which can be easily read by `numpy.fromfile`.

    Examples
    --------
    To create an unformatted sequential Fortran file:

    >>> from scipy.io import FortranFile
    >>> f = FortranFile('test.unf', 'w')
    >>> f.write_record(np.array([1,2,3,4,5], dtype=np.int32))
    >>> f.write_record(np.linspace(0,1,20).reshape((5,4)).T)
    >>> f.close()

    To read this file:

    >>> f = FortranFile('test.unf', 'r')
    >>> print(f.read_ints(np.int32))
    [1 2 3 4 5]
    >>> print(f.read_reals(float).reshape((5,4), order="F"))
    [[0.         0.05263158 0.10526316 0.15789474]
     [0.21052632 0.26315789 0.31578947 0.36842105]
     [0.42105263 0.47368421 0.52631579 0.57894737]
     [0.63157895 0.68421053 0.73684211 0.78947368]
     [0.84210526 0.89473684 0.94736842 1.        ]]
    >>> f.close()

    Or, in Fortran::

        integer :: a(5), i
        double precision :: b(5,4)
        open(1, file='test.unf', form='unformatted')
        read(1) a
        read(1) b
        close(1)
        write(*,*) a
        do i = 1, 5
            write(*,*) b(i,:)
        end do

    """
    def __init__(self, filename, mode=..., header_dtype=...) -> None:
        ...
    
    def write_record(self, *items): # -> None:
        """
        Write a record (including sizes) to the file.

        Parameters
        ----------
        *items : array_like
            The data arrays to write.

        Notes
        -----
        Writes data items to a file::

            write_record(a.T, b.T, c.T, ...)

            write(1) a, b, c, ...

        Note that data in multidimensional arrays is written in
        row-major order --- to make them read correctly by Fortran
        programs, you need to transpose the arrays yourself when
        writing them.

        """
        ...
    
    def read_record(self, *dtypes, **kwargs): # -> tuple[Unknown, ...]:
        """
        Reads a record of a given type from the file.

        Parameters
        ----------
        *dtypes : dtypes, optional
            Data type(s) specifying the size and endiness of the data.

        Returns
        -------
        data : ndarray
            A 1-D array object.

        Raises
        ------
        FortranEOFError
            To signal that no further records are available
        FortranFormattingError
            To signal that the end of the file was encountered
            part-way through a record

        Notes
        -----
        If the record contains a multidimensional array, you can specify
        the size in the dtype. For example::

            INTEGER var(5,4)

        can be read with::

            read_record('(4,5)i4').T

        Note that this function does **not** assume the file data is in Fortran
        column major order, so you need to (i) swap the order of dimensions
        when reading and (ii) transpose the resulting array.

        Alternatively, you can read the data as a 1-D array and handle the
        ordering yourself. For example::

            read_record('i4').reshape(5, 4, order='F')

        For records that contain several variables or mixed types (as opposed
        to single scalar or array types), give them as separate arguments::

            double precision :: a
            integer :: b
            write(1) a, b

            record = f.read_record('<f4', '<i4')
            a = record[0]  # first number
            b = record[1]  # second number

        and if any of the variables are arrays, the shape can be specified as
        the third item in the relevant dtype::

            double precision :: a
            integer :: b(3,4)
            write(1) a, b

            record = f.read_record('<f4', np.dtype(('<i4', (4, 3))))
            a = record[0]
            b = record[1].T

        NumPy also supports a short syntax for this kind of type::

            record = f.read_record('<f4', '(3,3)<i4')

        See Also
        --------
        read_reals
        read_ints

        """
        ...
    
    def read_ints(self, dtype=...): # -> tuple[Unknown, ...]:
        """
        Reads a record of a given type from the file, defaulting to an integer
        type (``INTEGER*4`` in Fortran).

        Parameters
        ----------
        dtype : dtype, optional
            Data type specifying the size and endiness of the data.

        Returns
        -------
        data : ndarray
            A 1-D array object.

        See Also
        --------
        read_reals
        read_record

        """
        ...
    
    def read_reals(self, dtype=...): # -> tuple[Unknown, ...]:
        """
        Reads a record of a given type from the file, defaulting to a floating
        point number (``real*8`` in Fortran).

        Parameters
        ----------
        dtype : dtype, optional
            Data type specifying the size and endiness of the data.

        Returns
        -------
        data : ndarray
            A 1-D array object.

        See Also
        --------
        read_ints
        read_record

        """
        ...
    
    def close(self): # -> None:
        """
        Closes the file. It is unsupported to call any other methods off this
        object after closing it. Note that this class supports the 'with'
        statement in modern versions of Python, to call this automatically

        """
        ...
    
    def __enter__(self): # -> Self@FortranFile:
        ...
    
    def __exit__(self, type, value, tb): # -> None:
        ...
    


