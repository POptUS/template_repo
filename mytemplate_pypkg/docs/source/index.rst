mytemplate python package
=========================

.. _ibcdfo_pypkg: https://github.com/POptUS/IBCDFO/tree/main/ibcdfo_pypkg

This package is a template python package for building in dedicated python
functionality as well as combining ``subA`` and ``subB`` tools, which we assume
share some important commonality, |via| symlinks.  A simpler but concrete
example of this package is the |poptus| python package `ibcdfo_pypkg`_.

Let's cite something random (:cite:t:`Golub13`) just so that we have a
non-empty bibliography with at least one cross-reference.

Let's also add in the definition

.. _MyDefinition:

.. proof:definition::

    A **whosiewhatsit** is an object distinct from a **thingamabob**.

and the theorem

.. _MyTheorem:

.. proof:theorem:: My Test Theorem

    The following should render in LaTeX

    * This should be an absolute value :math:`\abs{\xcomp{i}}`
    * This should be a norm :math:`\half\norm{\xvec}_2^2`
    * :math:`\JrhoHat = \Jrho(\pspHat; \dataset) \in \R^{\nd \times \np}`
    * :math:`\iterate{\psp}{i+1} = \iterate{\psp}{i} + \iterate{\step}{i}`

so that we can see what they look like and cross reference them later.  Please
refer to :numref:`Definition {number} <MyDefinition>` and :numref:`Theorem
{number} <MyTheorem>`.

.. toctree::
   :numbered:
   :maxdepth: 2
   :caption: Contents:

   get_started
   examples
   api
   developers_guide
   bibliography
