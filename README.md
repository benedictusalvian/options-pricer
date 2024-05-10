# Black-Scholes Options Pricer &middot; [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/benedictusalvian/options-pricer/issues)

Black-Scholes Options Pricer is an options pricer and chain builder for Delta One Index ETFs calls and puts, automatically generating different strike prices across different time horizons.  

## Features

- Simply type in your Delta One Index symbol to build your options chain! (E.g. SPY, VOO, VT)
- The program will automatically obtain market price from [Alpha Vantage].
- Automatically generate different strike prices across different time horizons of expiry.

## Tech

Black-Scholes Options Pricer uses a number of open source projects to work properly:

- [requests] - Requests is an elegant and simple HTTP library for Python, built for human beings.
- [scipy] - SciPy provides algorithms for statistics for many, different classes of problems.

And of course Black-Scholes Options Pricer itself is a free and open-source software with a [public repository][options-pricer] 
on GitHub.

## Installation

Black-Scholes Options Pricer has been developed and tested to run on [Python 3.12](https://www.python.org/downloads/).

Install [Python](https://www.python.org/downloads/release/python-3120/) if you have not already.

To use or contribute to Black-Scholes Options Pricer, first clone the repository.

Then, install the dependencies by typing the following command on your terminal:

```sh
pip3 install requests scipy
```

Then, rename `config_example.py` to `config.py` and replace the API Key constant with your Alpha Vantage API Key. The Alpha Vantage API Key obtains the underlying market price for your chosen Delta One Index ETF. You may obtain your free API Key [here](https://www.alphavantage.co/support/#api-key).

If you do not wish to obtain an Alpha Vantage API Key, you may set the underlying market price manually by doing the following:

```sh
Comment this line
S = get_global_quote(index) # Underlying price of Delta One Index ETF

Uncomment this line
# S = round(float(input("Input price of your chosen index: ")))
```

## Examples

Now run the following command on the terminal to run Black-Scholes Options Builder:

```sh
python3 Black-Scholes.py
```

If you input "SPY" as your ETF symbol, the following results will be printed:

```sh
Input Delta One Index ETF: SPY

Option Chain for Delta One Index ETF SPY for underlying market price of 520 

3 months away                    6 months away                   9 months away                   12 months away                  
Calls   Strike  Puts             Calls  Strike  Puts             Calls  Strike  Puts             Calls  Strike  Puts             
55.56   470     0.35             61.71  470     1.35             67.79  470     2.32             73.66  470     3.16             
50.82   475     0.55             57.26  475     1.78             63.51  475     2.89             69.52  475     3.8              
46.16   480     0.83             52.91  480     2.32             59.35  480     3.56             65.47  480     4.53             
41.61   485     1.23             48.68  485     2.98             55.29  485     4.33             61.52  485     5.37             
37.21   490     1.77             44.59  490     3.78             51.36  490     5.24             57.69  490     6.31             
32.98   495     2.49             40.65  495     4.73             47.56  495     6.27             53.97  495     7.38             
28.95   500     3.41             36.88  500     5.86             43.9   500     7.45             50.37  500     8.56             
25.17   505     4.57             33.3   505     7.16             40.39  505     8.78             46.91  505     9.88             
21.64   510     5.99             29.9   510     8.66             37.04  510     10.26            43.58  510     11.33            
18.41   515     7.7              26.71  515     10.36            33.85  515     11.91            40.39  515     12.92            
15.47   520     9.71             23.73  520     12.27            30.84  520     13.73            37.34  520     14.65            
12.85   525     12.03            20.97  525     14.39            27.99  525     15.72            34.43  525     16.53            
10.54   530     14.66            18.43  530     16.74            25.32  530     17.88            31.68  530     18.56            
8.54    535     17.6             16.1   535     19.3             22.82  535     20.22            29.07  535     20.73            
6.82    540     20.84            13.98  540     22.07            20.5   540     22.73            26.61  540     23.06            
5.38    545     24.34            12.07  545     25.05            18.34  545     25.41            24.3   545     25.53            
4.19    550     28.09            10.36  550     28.23            16.36  550     28.26            22.13  550     28.14            
3.22    555     32.07            8.84   555     31.61            14.53  555     31.28            20.11  555     30.9             
2.44    560     36.23            7.5    560     35.15            12.87  560     34.45            18.22  560     33.8             
1.82    565     40.56            6.33   565     38.87            11.35  565     37.77            16.47  565     36.83            
1.34    570     45.02            5.31   570     42.74            9.98   570     41.23            14.86  570     39.99  
```


## Development

Want to contribute? Great!

Black-Scholes Options Pricer uses Python for developing.
Make changes in your file and create a pull request!

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [requests]: <https://requests.readthedocs.io/en/latest/>
   [scipy]: <https://scipy.org/>
   [options-pricer]: <https://github.com/benedictusalvian/options-pricer>
   [Alpha Vantage]: <https://www.alphavantage.co/>