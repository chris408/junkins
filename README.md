![Junkins logo](https://chris408.com/junkins-logo.png)  
Jenkins logo: https://jenkins.io/ License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

### Junkins

I created this script to automate my Jenkins server credential store decryption. By default Jenkins credentials are encrypted, but the encryption key is stored locally on the server. This allows anyone with script interface access to decrypt any secret stored on the server. 

### Files

- `junkins.py`: This is the script itself.
- `plain_postdata`: This file contains the Jenkins groovy script.

### Required

Posting the groovy script requires the 'requests' Python library.

### Docker instructions

Optionally, if you'd like to run junkins in a docker container, use the following commands:

```bash
$ git clone https://github.com/chris408/junkins
$ cd junkins
$ docker build -t junkins ./
$ docker run -it junkins http://jenkins-server/scriptText/
``` 

### TODO

- [ ] Add CSRF 'Crumb' support.
- [ ] Add proxy server command line argument support.
- [x] Add support to automate the creation of the `plain_postdata` file.
- [x] Add Dockerfile

### Example output:

```bash
$ python junkins.py http://jenkins-server/scriptText/
Credential store dump:

username: testuser
password: testpassword

username: testuser_key
privatekey:
-----BEGIN RSA PRlVATE KEY-----
MIIEpAIBAAKCAQEAyLN2P5iv1gc7y3O0h1QsBlCpj0W+HQFJsfQC3b7m6j28ZHS7
QfUDGwya1Wx8dlCvTckwwzX+Bg26G7F6C9GQmSXgYF+dlsKgSnUp/60AcXdzaSyE
u5rqExFOdzd6kd2gbE1wwK0lg6iFObdiuJM3B5WYDSYc9KeopP0ve17nszrpEuNq
G8GXqeZu9Fq9QgibDhAQ3I/N0EDqf4dHv5PhLSinP2zmmyKSrHMmUIW0rpxUaU1o
f7FR1X8U/BTeBPyodAGnE2PHkdzCGYfOTl/PqNcATGHejYxwMaUKDaliNql9duuL
vNs9djI8PEEMYmuoKZ/HN9rMGFrG+mt7RgD0nwIDAQABAoIBAD9sJsP2FirGYmjq
iXPyb28Xcl2qJme4DnfDqlw0hXgkRjJgiQRQzshvdUZYYARrftpP567okvuKvvMd
ZHnzoYQj6gHKdVw86LZezATVwLwaiUgFH3TBgZLA91DJIVyS8q0G08ivbplqWZ9h
ijrVmqA077XIA4J0sOBieey8ku+Z8FaarWdB/7g1AQslYT+Y3b0j6AWeIar82gXQ
rAF8NCugUPwSBnfUbvQtbLCaLP8uV2VqXppWhVgOQ29ynAeUgjGqxprL279/ZI0B
vRljoSp8ikQT+5jOW4RDEY0o2xGmh54R4QoG7Ob9DVRx/8HwiO25/1ls/jcy8GYs
sZGr6WECgYEA966kc2F24UUUdFcYdx4ecn7qZkxkwynm6p9Xg7FxvLRSNKnJU1xH
d/4JdrogsYxAY+EOvvvk85rCA9/Y1ZPn9WW4nPBl0pjaEyEQN1VUBqlznv6Bk3JL
00//CsPP4JMUTfn7bn90WYqlvuje0jqQdlIruj/ePca2xHs7Rn0+MrcCgYEAz3Dq
fMXrMquqYgz/qsXekmU/Q6Zd7dWdQa2rk96QoYURuWjHtm1fSPQ5XiCB95J1Xyry
DB+iWBEDFjs8XF8s2yDp+pEf2DQug/+IvukEVjwozbQ/k84ehEZo1h94cZAuQCsQ
UFFBILakvN5OcmAFlTKRj67b5vI5CoSQdBf6RVkCgYAh1fjfTkxIQACoWBGejD3K
lG3/JaaKRtol6TiyY/ZOui+UxDEdsziMOuceEhVPTAKr4l36Vz0Sz3x8zQK5Qqho
jMnonqq6V2lLPbQSaxS8iD+kU85tzypuproHxXJLkqwubt0bXkwNw3QbHYL7I0cC
8vzIR9tbgx8Kvm79lTR/BwKBgQCuKWBF16mLRkNrxPwWdcBTavv9oT01RGaeUOA/
6tnFMkLaRtV+HT+lsZ5En8hegjFW8Gh9s0WK6OWNkbgw2ZuAcpbfT17MF6uCGVXG
6z4/5IxhgFbskl5esfqs44ks119tcnpk5INoos+W3pJARswJIobBeo6XzIAFi5z4
S3VNKQKBgQCmm9wva5lY6nynj7iAlg0z44xZ2wcEARmEXnSbUjaBJ0s+VjyCnE1V
t34ay3A3Et8ZO6cx57NlWPZ9sYqZ6J+9IcfshGRWb3W5tFWZ7LXmmOhX1+KVmIjY
dYfxSwlUmnNIye2s9FA1wCxQYvfD/D4+YGjBuFsnUPwlhhUqC6QSEg==
-----END RSA PRlVATE KEY-----


username: testuser_key_withpassphrase
passphrase: testpassphrase

privatekey:
-----BEGIN RSA PRlVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,ECF34585F755D68F9111EEFABA777921

B8BJrH0tIFJQS26Q7DGluZwfzPB17YDl5pNvHMxoNITtmJn3xtNZQ+t68Qz61Qu1
R/MyKhCQFo3Oc8Z5TXDH6ZuUQWpQA7Uy7D4qdchCQdTi/nqnIfQ2jTMweSLsa0/f
XcKimsh23ldGnT9vu7b21PDms2RFJlEJNFPH6lqSYU0LScyZF/m3EOspQKqus3Gd
JjEB6Aw3VrlVj0Fl8MRpbVsOReILLby6+UgpoHScSrOtp4wHLL5sLhqEhg4X6azn
JqDjhcSMKUklPQS2B1dVSgSYderNuR6C8nV5D7vRkUvHZZth47PTtXQbKi7tXbpj
o/4s9N0tpaqfQIDFvYHuVncDbatENj8EAKiW/VqfQAIbh9ibPYFTu1/Gy9iv5HoL
1qujx7gxX1qt88fF4kwLffBi4V850qpR/SxdLh/2tOU6DbyybEf+W4XAEZG+ruKL
PaGjw3EYG34KYFELp0UxC5++vRkB9aaNx1htaFDGhEnYRAzWtd4Ew/Jgxp0y1BRz
JxjQIYMazDvz/h+MVoQIR5ThOEb8iXxnSiDtVcvJiBRMFXIuUmmYnkdA/77nzWNW
pZK5xyjLnRbcAvrFfT6vBixRGIOUODZCcI6aWeY+wgpHxgHXvIHk7D3nuAXTKJ1p
L2Jx8p28qIeMNv3wyuTV1qs2CTabiMDN2fOWRCHYa53vmN1BWV6g8xG52ycJEHEc
8xzNcv5uKriEoBxMWQccKoCHsYbssedXKkvgXswHvbYHHMRX85hc5qwrMbp+/GKo
Rk1+hNIDBJ2jzYiQd34NwQmDiiB0afcETMTtosIjY0fLnz0axpt3rfXM6QaEe2RT
JCAmpsR00Nc0H17ECqt2DP88nmkqKpjY2LWt8yqQzPZipV9TAsFuAxsna46ObTB/
N32+xhq9IKrZVLd2ogeyH+uH8aESmM//xVRNKRAaFFgBgs/idvVrnbhjRxcTFx30
mG+aYDviUH9GOsFkyCXAJ2PHPDIF5ExQAEtZUCQHDcu+JZWuh/nSzgXYLKyeywZU
Jjs9QEEIJeykOaLFdjAwZ98K6oWIvr5WA+QeCGmINP3ycMImEcTl23Ky+5EGHkPc
vwu8jbHdHrF2uxYHCYJfJrMAHxPL9QMP5oxsJ1GWq4VlQI4A6BDyh+jvJrjKoFQx
FfTKupjl9PykvslzACgyV6Zmg8wY+xL0urH2udj4lkXTk7yX9SGf7qxFcuVCcxDs
2dycISkD53TkejBic72zuk6OQcVIdqLaMlXAnWSCFvJTew2rXTHqPTw88sAeZI6M
Nfr0XO7NseW0vdtg/Gdwo4YwzOhF0pR52Xr1mTGyhX5p4/FkRbVyDAvBwvpCd7Ep
vDVcMi+vpS2UVSpbJ5Kb083B6QGHpdAPTP1ye+HhRyYSBna4lcVz4KaDxkefZa/G
lP1pL1BmeOZo9DexOiCqgi8uv/I4YDqIHilL9wuxqZWZUeNCZ+IFV4iOHQcBgKVr
gT2YSW6cm7oTbWBb8rxMoLlHwMAUNM8siO64HhwB8EHEyFWaxY3J+i5V0gZyqUOS
p/NsjfyK5g5XoPXaVUv8uPOGQPL/nM1Nt8EwYB2DEbhCBifUKWK9gL4kRvbgFQcY
-----END RSA PRlVATE KEY-----


secret text:
githuboauthtoken
```
