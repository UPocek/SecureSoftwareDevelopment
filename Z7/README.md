## Uros & Tamara
### Zip Slip Vulnerability - CVE-2007-4559
- Vulnerability in this CVE comes from the way the `tarfile` native Python package handles tar file extraction.
- To execute this exploit you need to create a tar file that has a relative path file name e.g. `../../secret/test.txt`
- This is not easy to do on any OS but the command `tar -czvf evil.tar.gz ../../secret/test.txt` can do the trick
- Once you created the `evil.tar.gz` which looks like any regular .tar you can upload it to the server that uses the `tarfile` module
- For demonstration purposes, I created a Python Flask web server which codes you can access at ./app.py also to make it easy to demonstrate I left the development server in my Docker container
- Why am I mentioning this is because when you change the file contents in the mode server watches for those changes and starts over which means that if we use the bug in `tarfile` to override the app.py file we can create an endpoint that can execute any code we want on the server
- For demonstration, I just created evil.tar.gz if you upload to the frontend app I created which you can find at `localhost:7255` you will see that file test.txt is not uploaded to the archive folder, but on the secret folder which can be dangerous

## Alex