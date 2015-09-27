Enter file contents here#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prints current date and time"""

import datetime

CURDATE = None

def get_current_date():
    """Returns current date and time.

    Var:
        None.

    Returns:
        Current date and time.

    Examples:
        >>>import task_01
        >>>print task_01.CURDATE
        None

        >>>task_01.get_current_date()
        datetime.date(20115, 1, 1)

        $ python -i task_01.py
        2015-01-01
    """

    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
