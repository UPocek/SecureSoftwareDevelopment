# Z6

## Uros
### Task 4
- First I read the message and saw that some parts were repeating and didn't make sense, this led me to believe that this was encoded text
- Then I used Google's phrase match search term using quotes (for example "search_term") and found a Chinese blog that led me to Spam Mimic https://www.spammimic.com/decode.cgi
- I copied spam email content sent to me by my friend, decoded it, and saw the flag
- UNS{EM4IL_5P4M_AG4N?}

### Task 5
- I opened forgotten_passwords and started looking for answers
- First answer about FTN I found at http://www.ftn.uns.ac.rs/n1613077170/o-ftn-u that FTN was opened on <strong>18/05/1960</strong> which gave me correct hash
The second answer I found after a little bit of research on the FTN website. This information is not available on Wikipedia, but I found that the dean at that time was <strong>Dragutin</strong> Zelenović here http://www.ftn.uns.ac.rs/n508315396/istorijat-funkcije-dekan
The third answer I found searching through the archive of FTN website posts. Here http://www.ftn.uns.ac.rs/1426608662/arhiva-vesti I found that announcement about website was made on <strong>18/05/2005</strong>
The fourth answer I found on http://www.ftn.uns.ac.rs/n1613077170/o-ftn-u where every program's start date is mentioned, answer is <strong>1999</strong>
- Then I was able to unzip rar protected with a password on https://www.ezyzip.com/open-password-protected-rar-files.html
- UNS{V3RY_OLD_4RCH1V3}


## Tamara

### Task 6
- I figured out that flag must be hidden somewhere inside the image so I first tried opening the image in a text editor to see if the flag was appended to the end of the image as text, but it wasn't
- Then I opened the image as a byte array to see if I could find an image like that with the same premise that the flag is text, but that didn't help either, after careful research about Steganography I figured that secret could be an image embedded in an image
- Now the task is to find an online tool that isn't looking for hidden text but hidden image inside the image and I found it here https://incoherency.co.uk/image-steganography/#unhide, decoding image gave me a flag as an image
- UNS{PMF_STUD3NT5_LOV3_M4TH}

### Task 7
 - A Google search for The Queen of the Ocean first led me to cruise ship, but that didn't make much sense in the context of captured and tagged. So I added those keywords and found out that the Queen in this context is a great white shark.
 - I googled and found out that they gave her name Nakumi
 - I also found that this website https://www.ocearch.org/tracker/detail/nukumi has ping information for tagged sharks fo I searched for Nukumi and found that she was tagged on Apr 11, 2021, 3:03:07 PM so the flag is
 - RC15{Apr 11, 2021, 3:03:07 PM}

## Alex

### Task 8

```
NAVY{h4v3_y0u_3v3r_w4tched_!t?}
```

1. We have an image, so firstly trying to analyze it with steganography tools (https://www.aperisolve.com/16bce86599aa0610a443dcbffae319b8):
   However, neither hidden image or text (Zsteg for text was used) was found:
   ![Steg1](images/img.png)
   ![Steg3](images/img_1.png)
2. But we still have an email on the photo - let's google it
3. There is such a user on the GitHub
4. He has only one repo. Searching for word `NAVY` in it
5. Key: https://github.com/search?q=repo%3Asquidgameph1337%2Fsquidgame%20NAVY&type=code

### Task 9

```
UNS{45.1194813,19.2600817}
```

1. Sava Šumanović was leaving in Šid. I was to the museum there!
2. There is only a couple of street in the city. But let's search by shop name
3. ![img.png](images/img_2.png)
4. ![img.png](images/img11.png)

### Task 10

That's a tough one.

1. The coast seems to be more likely to be of an artificial water reservoir rather than a sea.
2. https://picarta.ai/ tells it's 
   ``` 
   1. Orgelet, France. GPS location around: 46.5•••••,5.5••••• Confidence: 37.74%
   ```
   But mountains in France are lower and roads are more advanced there.
3. Google Lence told it is Tara
4. Look over Montenegro / Serbian west on the Google Earth
5. Not Tara, but some lake near
   ![img_1.png](images/img_11.png)
6. Still can not find exactly that panorama view
