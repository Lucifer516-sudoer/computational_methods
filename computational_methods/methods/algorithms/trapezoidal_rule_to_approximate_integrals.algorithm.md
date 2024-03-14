# Trapezoidal Rule - TR

> Formula:
```shell
 b 
 /
 | f(x) dx = (h / 2) * [(y0 + yn) + 2(y1 + y2 + y3 + ... + yn-1)]
 |
 /
 a
 ```

        where, 
            h --> generally (a-b)/number_of_intervals


## Algorithm:
* Get the function i.e Integral
* get the number of intervals as h; if not given ask for the limit of the integral
* Now just create a table with the limits x -> y mapping i.e function input -> output
* Now using the table values
* calculate using the TR forumla
* > Print the result to user, with step by step outcomes