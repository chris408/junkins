# Junkins

I created this script to automate my Jenkins server credential store decrypting.

### Files

- `junkins.py`: This is the script itself.
- `postdata`: This file contains the Jenkins generated post data.
- `plain_postdata`: This is the orignal Jenkins groovy script. 

### Customizing

1. To customize your groovy script you'll need to modify the `plain_postdata` file. 
2. Once you've modified it, navigate to a Jenkins system on /script, and paste in the new groovy script. 
3. Fire up Burp Suite to capture the post. 
4. Submit your modified script to the server by clicking "Run". 
5. Once you've captured the post in Burp Suite, copy this new data into the `postdata` file. 

### TODO

- Add CSRF 'Crumb' support.
- Add proxy server command line argument support.
- Add support to automate the creation of the `postdata` file.
- Add support to detect local users to steal API keys. 
    - Currently the code assumes the user 'admin' exists as a PoC.
- Add support for the addtional Jenkins credential types.
