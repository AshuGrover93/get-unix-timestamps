# get-unix-timestamps
Obtain previous months, quarters and years unix timestamps in python

# GET UNIX TIMESTAMPS PYTHON

The function will help you in obtaining as the desired start and end timestamps (GMT)
  - Monthly
  - Quartery
  - Yearly

# Use:

Pass the three paramerters to the function `getdate(data_ts, agg_type, no_times)`.

The first parameter `data_ts` is the timestamp prior to which you want the start and end timestamps.
The second parameter is the aggregation type: `month` or `quarter` or `yearly`.
The third parameter `no_times` signifies the number of months/quarters/years you want the timestamp for.

For instance if we run `print(getdates(1540439326000, 'year', 5))` the output obtained is a list consisting of 5 prior start and end timestamps of the year(2018) in timestamp passed (1540439326000 in this case):
`[{'start_dt5': 1483228800000.0, 'end_dt5': 1514764799999.0}, {'start_dt4': 1451606400000.0, 'end_dt4': 1483228799999.0}, {'start_dt3': 1420070400000.0, 'end_dt3': 1451606399999.0}, {'start_dt2': 1388534400000.0, 'end_dt2': 1420070399999.0}, {'start_dt1': 1356998400000.0, 'end_dt1': 1388534399999.0}]`

where `start_dt5` and `end_date5` is timestamp of 1st Jan'17 and 31st Dec'17 respectively, `start_dt4` and `end_date4` is timestamp of 1st Jan'16 and 31st Dec'16 respectively and so on till 2013 that is the `no_times` passed.



Similarly, if we run `print(getdates(1553883914000, 'month', 4))` the output is:
`[{'start_dt4': 1548979200000.0, 'end_dt4': 1551398399999.0}, {'start_dt3': 1546300800000.0, 'end_dt3': 1548979199999.0}, {'start_dt2': 1543622400000.0, 'end_dt2': 1546300799999.0}, {'start_dt1': 1541030400000.0, 'end_dt1': 1543622399999.0}]`

giving monthly start and end timestamps of 4 months prior to month of `1553883914000` that is March'19 in this case.
So, `start_dt4` is for 1st Feb'19 and `end_dt4` is for 28th Feb'19, `start_dt3` is for 1st Jan'19 and `end_dt3` is for 31st Jan'19, `start_dt2` is for 1st Dec'18 and `end_dt2` is for 31st Dec'18 and so on.

Note: All unix timestamps are in GMT timezone.

License
----

MIT
