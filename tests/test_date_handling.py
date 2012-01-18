# -*- coding: utf-8 -*-

from datetime import datetime as dt

from nose.tools import assert_equals

from github2.core import (datetime_to_ghdate, datetime_to_commitdate,
                          datetime_to_isodate, string_to_datetime)


# Commented test cases are in PST, and aren't correctly handled with the
# naïve datetime objects used in the current code base

def test_ghdate_to_datetime():
    assert_equals(string_to_datetime('2011/05/22 00:24:15 -0700'),
                  dt(2011, 5, 22, 0, 24, 15))

    assert_equals(string_to_datetime('2009/04/18 13:04:09 -0700'),
                  dt(2009, 4, 18, 13, 4, 9))
    #assert_equals(string_to_datetime('2009/11/12 21:15:17 -0800'),
    #              dt(2009, 11, 12, 21, 15, 17))
    #assert_equals(string_to_datetime('2009/11/12 21:16:20 -0800'),
    #              dt(2009, 11, 12, 21, 16, 20))
    assert_equals(string_to_datetime('2010/04/17 17:24:29 -0700'),
                  dt(2010, 4, 17, 17, 24, 29))
    assert_equals(string_to_datetime('2010/05/18 06:10:36 -0700'),
                  dt(2010, 5, 18, 6, 10, 36))
    assert_equals(string_to_datetime('2010/05/25 21:59:37 -0700'),
                  dt(2010, 5, 25, 21, 59, 37))
    assert_equals(string_to_datetime('2010/05/26 17:08:41 -0700'),
                  dt(2010, 5, 26, 17, 8, 41))
    assert_equals(string_to_datetime('2010/06/20 06:13:37 -0700'),
                  dt(2010, 6, 20, 6, 13, 37))
    assert_equals(string_to_datetime('2010/07/28 12:56:51 -0700'),
                  dt(2010, 7, 28, 12, 56, 51))
    assert_equals(string_to_datetime('2010/09/20 21:32:49 -0700'),
                  dt(2010, 9, 20, 21, 32, 49))


def test_datetime_to_ghdate():
    assert_equals(datetime_to_ghdate(dt(2011, 5, 22, 0, 24, 15)),
                  '2011/05/22 00:24:15 -0700')

    assert_equals(datetime_to_ghdate(dt(2009, 4, 18, 20, 4, 9)),
                  '2009/04/18 20:04:09 -0700')
    #assert_equals(datetime_to_ghdate(dt(2009, 11, 13, 4, 15, 17)),
    #              '2009/11/13 04:15:17 -0800')
    #assert_equals(datetime_to_ghdate(dt(2009, 11, 13, 4, 16, 20)),
    #              '2009/11/13 04:16:20 -0800')
    assert_equals(datetime_to_ghdate(dt(2010, 4, 18, 0, 24, 29)),
                  '2010/04/18 00:24:29 -0700')
    assert_equals(datetime_to_ghdate(dt(2010, 5, 18, 13, 10, 36)),
                  '2010/05/18 13:10:36 -0700')
    assert_equals(datetime_to_ghdate(dt(2010, 5, 26, 5, 59, 37)),
                  '2010/05/26 05:59:37 -0700')
    assert_equals(datetime_to_ghdate(dt(2010, 5, 27, 0, 8, 41)),
                  '2010/05/27 00:08:41 -0700')
    assert_equals(datetime_to_ghdate(dt(2010, 6, 20, 13, 13, 37)),
                  '2010/06/20 13:13:37 -0700')
    assert_equals(datetime_to_ghdate(dt(2010, 7, 28, 19, 56, 51)),
                  '2010/07/28 19:56:51 -0700')
    assert_equals(datetime_to_ghdate(dt(2010, 9, 21, 4, 32, 49)),
                  '2010/09/21 04:32:49 -0700')


def test_commitdate_to_datetime():
    assert_equals(string_to_datetime('2011-05-22T00:24:15-07:00'),
                  dt(2011, 5, 22, 0, 24, 15))

    assert_equals(string_to_datetime('2011-04-09T10:07:30-07:00'),
                  dt(2011, 4, 9, 10, 7, 30))
    #assert_equals(string_to_datetime('2011-02-19T07:16:11-08:00'),
    #              dt(2011, 2, 19, 7, 16, 11))
    #assert_equals(string_to_datetime('2010-12-21T12:34:27-08:00'),
    #              dt(2010, 12, 21, 12, 34, 27))
    assert_equals(string_to_datetime('2011-04-09T10:20:05-07:00'),
                  dt(2011, 4, 9, 10, 20, 5))
    assert_equals(string_to_datetime('2011-04-09T10:05:58-07:00'),
                  dt(2011, 4, 9, 10, 5, 58))
    assert_equals(string_to_datetime('2011-04-09T09:53:00-07:00'),
                  dt(2011, 4, 9, 9, 53, 0))
    assert_equals(string_to_datetime('2011-04-09T10:00:21-07:00'),
                  dt(2011, 4, 9, 10, 0, 21))
    #assert_equals(string_to_datetime('2010-12-16T15:10:59-08:00'),
    #              dt(2010, 12, 16, 15, 10, 59))
    assert_equals(string_to_datetime('2011-04-09T09:53:00-07:00'),
                  dt(2011, 4, 9, 9, 53, 0))
    assert_equals(string_to_datetime('2011-04-09T09:53:00-07:00'),
                  dt(2011, 4, 9, 9, 53, 0))


def test_datetime_to_commitdate():
    assert_equals(datetime_to_commitdate(dt(2011, 5, 22, 0, 24, 15)),
                  '2011-05-22T00:24:15-07:00')

    assert_equals(datetime_to_commitdate(dt(2011, 4, 9, 10, 7, 30)),
                  '2011-04-09T10:07:30-07:00')
    #assert_equals(datetime_to_commitdate(dt(2011, 2, 19, 7, 16, 11)),
    #              '2011-02-19T07:16:11-08:00')
    #assert_equals(datetime_to_commitdate(dt(2010, 12, 21, 12, 34, 27)),
    #              '2010-12-21T12:34:27-08:00')
    assert_equals(datetime_to_commitdate(dt(2011, 4, 9, 10, 20, 5)),
                  '2011-04-09T10:20:05-07:00')
    assert_equals(datetime_to_commitdate(dt(2011, 4, 9, 10, 5, 58)),
                  '2011-04-09T10:05:58-07:00')
    assert_equals(datetime_to_commitdate(dt(2011, 4, 9, 9, 53, 0)),
                  '2011-04-09T09:53:00-07:00')
    assert_equals(datetime_to_commitdate(dt(2011, 4, 9, 10, 0, 21)),
                  '2011-04-09T10:00:21-07:00')
    #assert_equals(datetime_to_commitdate(dt(2010, 12, 16, 15, 10, 59)),
    #              '2010-12-16T15:10:59-08:00')
    assert_equals(datetime_to_commitdate(dt(2011, 4, 9, 9, 53, 0)),
                  '2011-04-09T09:53:00-07:00')
    assert_equals(datetime_to_commitdate(dt(2011, 4, 9, 9, 53, 0)),
                  '2011-04-09T09:53:00-07:00')


def test_isodate_to_datetime():
    assert_equals(string_to_datetime('2011-05-22T00:24:15Z'),
                  dt(2011, 5, 22, 0, 24, 15))
    assert_equals(string_to_datetime('2011-04-09T10:07:30Z'),
                  dt(2011, 4, 9, 10, 7, 30))
    assert_equals(string_to_datetime('2011-02-19T07:16:11Z'),
                  dt(2011, 2, 19, 7, 16, 11))
    assert_equals(string_to_datetime('2010-12-21T12:34:27Z'),
                  dt(2010, 12, 21, 12, 34, 27))
    assert_equals(string_to_datetime('2011-04-09T10:20:05Z'),
                  dt(2011, 4, 9, 10, 20, 5))
    assert_equals(string_to_datetime('2011-04-09T10:05:58Z'),
                  dt(2011, 4, 9, 10, 5, 58))
    assert_equals(string_to_datetime('2011-04-09T09:53:00Z'),
                  dt(2011, 4, 9, 9, 53, 0))
    assert_equals(string_to_datetime('2011-04-09T10:00:21Z'),
                  dt(2011, 4, 9, 10, 0, 21))
    assert_equals(string_to_datetime('2010-12-16T15:10:59Z'),
                  dt(2010, 12, 16, 15, 10, 59))
    assert_equals(string_to_datetime('2011-04-09T09:53:00Z'),
                  dt(2011, 4, 9, 9, 53, 0))
    assert_equals(string_to_datetime('2011-04-09T09:53:00Z'),
                  dt(2011, 4, 9, 9, 53, 0))


def test_datetime_to_isodate():
    assert_equals(datetime_to_isodate(dt(2011, 5, 22, 0, 24, 15)),
                  '2011-05-22T00:24:15Z')
    assert_equals(datetime_to_isodate(dt(2011, 4, 9, 10, 7, 30)),
                  '2011-04-09T10:07:30Z')
    assert_equals(datetime_to_isodate(dt(2011, 2, 19, 7, 16, 11)),
                  '2011-02-19T07:16:11Z')
    assert_equals(datetime_to_isodate(dt(2010, 12, 21, 12, 34, 27)),
                  '2010-12-21T12:34:27Z')
    assert_equals(datetime_to_isodate(dt(2011, 4, 9, 10, 20, 5)),
                  '2011-04-09T10:20:05Z')
    assert_equals(datetime_to_isodate(dt(2011, 4, 9, 10, 5, 58)),
                  '2011-04-09T10:05:58Z')
    assert_equals(datetime_to_isodate(dt(2011, 4, 9, 9, 53, 0)),
                  '2011-04-09T09:53:00Z')
    assert_equals(datetime_to_isodate(dt(2011, 4, 9, 10, 0, 21)),
                  '2011-04-09T10:00:21Z')
    assert_equals(datetime_to_isodate(dt(2010, 12, 16, 15, 10, 59)),
                  '2010-12-16T15:10:59Z')
    assert_equals(datetime_to_isodate(dt(2011, 4, 9, 9, 53, 0)),
                  '2011-04-09T09:53:00Z')
    assert_equals(datetime_to_isodate(dt(2011, 4, 9, 9, 53, 0)),
                  '2011-04-09T09:53:00Z')
