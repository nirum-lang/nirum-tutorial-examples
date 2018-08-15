Examples from [Nirum step-by-step tutorial][1]
==============================================

This repository contains examples from [*Step-by-step tutorial*][1] of Nirum.

You can run the server or unit tests using the below command:

    make run-counter-server
    make test-counter-server

Note that there are `NIRUM` and `PYVENV` variables and overridable through
`-e` option:

    NIRUM=nirum-linux-x86_64 PYVENV=pyvenv-3.5 make -e run-counter-server

Distributed under public domain.

[1]: https://nirum.org/docs/tutorial.html
