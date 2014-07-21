`Kakebo2` is simple Analyser of kakebo.

## Usage

Please make a symbolic link where there is filename.

```
kakebo.py  [options] filename1, filename2, ...
```

## Requirement Modules
* `json`    \
    If you want to use json-format
* `yaml` \
    If you want to use yaml-format

## How to Use

Make symbolic link where is directory which there is kakebo file as following:

```
ln -s {dir}/kakebo.py ./kakebo
```

and type `kakobo` command in this directory.

## Format
At first, please make file about information of Kakebo.

### Use JSON or YAML

If you use `json` or `yaml`, please use list data structure, whose first value
is initial money(`int` data) and even number of Kakebo's items are `date` format
string(`%Y/%M/%D`) and odd number of items are list of a content.
Here, "content" is a list of "comment" and income about that content.

Example is kakebo.json:

``` 
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
```

### Use PLAIN-TEXT Format

If you use simple text format, please take `.txt` extension.

For indicating date, enter `=== %Y/%M/%D`.
And for indicating item, enter `{comment}:{income}:{rest money}`.

For example is `kakebo.txt`:

```
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
```

## Options

Please use one of `-g`, `--statics` or `-t` option.

* `-y {year}`, `--y {year}` \
    only use kakebo of `{year}` year for statistics
* `-m {month}`, `--m {month}` \
    only use kakebo of `{month}` year for statistics
* `-d {day}`, `--day {day}` \
    only use kakebo of `{day}` day for statistics
* `-w {wday}`, `--wday {day}` \
    only use kakebo of `{wday}` weekday for statistics
* `-g`, `--graph` \
    Show graph of Kakebo.
    This graph includes polygonal line and regressin line of incomes per day. \
    If a content which starts with `#`, skip this content for statistics.
* `--statics`   \
    Show basic statics for kakebo.    \
    "basic statics" means  mean, variance, regression line of incomes per one
    day.
    This is default as output.
* `-t`, `--text` \
    convert to text-format from Kakebo. \
    I think it is useful when you hand out kakebo to other, who is not
    programmer.
