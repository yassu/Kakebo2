==========
Kakebo2
==========
A plugin is simple analyser of kakebo.

Installation
=============

    $ python3 setup.py install

Usage
======


    $ kakebo.py  [options] filename1 filename2 ...

Requirements
==============

* yaml

Format
=======
At first, please make file about information of Kakebo

Use Json or Yaml
------------------

If you use `json` or `yaml`, please use lsit data structure, whose first value
is initial money(int data) and even number of Kakebo's items are `date` format
string(%Y/%M/%D) and odd number of items are list of a content.
Here, "content" means a list of "comment" and income about that content.

Example for json format::

    [
        4984,
        "2014/03/28",
        [
            ["buy tea,milk", -327]
        ],
        "2014/03/29",
        [
            ["music player(transcend)", -4095],
            ["# go bank", 10000],
            ["shopping", -906],
            ["eat Ramen", -780],
            ["buy Cola", -120]
        ],
        "2014/03/30",
        [
            ["buy coffee", -110],
            ["buy pizza", -4000]
        ],
        "2014/03/31",
        [
            ["coffee", -110],
            ["biscket", -165],
            ["shopping", -1133],
            ["# go Bank", 31000],
            ["eat Ramen", -630],
            ["engine", -3682]
        ]
    ]

Use PLAIN-TEXT Format
-----------------------
If you use simple text format, please take `.txt` extension.

For indicating date, enter `=== %Y/%M/%D`.
And for indicating item, enter `{comment}:{income}:{rest-money}`.

Example for txt format::

    === 2014/03/28
        buy tea,milk:-327:4657
    === 2014/03/29
        music player(transcend):-4095:562
        # go bank:10000:10562
        shopping:-906:9656
        eat Ramen:-780:8876
        buy Cola:-120:8756
    === 2014/03/30
        buy coffee:-110:8646
        buy pizza:-4000:4646
    === 2014/03/31
        coffee:-110:4536
        biscket:-165:4371
        shopping:-1133:3238
        # go Bank:31000:34238
        eat Ramen:-630:33608
        engine:-3682:29926

Options
========

Please use one of `-g`, `--statics` or `-t` option.

* `-y {year}`, `--year {year}`: only use kakebo of `{year}` year for statics
* `-m {month}`, `--month {month}`: only use kakebo of `month` month for statics
* `-d {day}`, `--day {day}`: only use kakebo of `{day}` day for statics
* `-w {wday}`, `--wday {wday}`: only use Kakebo of `{wday}` day for statics
* `-g`, `--graph`: Show graph of Kakebo. This graph includes regression line of
  incomes per day. If a content which starts with `#`, skip this content for
  statics.
* `--statics`: Show basic statics for Kakebo. "basic statics" means mean,
  variance, regression line of incomes per one day.
  This is default as output.
* `-t`, `--text` : convert to text-format from Kakebo. I think it is useful when
  you hand out kakebo to other, who is not programmer.

License
========
Apache License 2.0
