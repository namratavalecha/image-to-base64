# Image To Base64 Conersion

This application consists of an API which intakes an image file in “Form data” and returns the base64
encoding of the image along with it’s MD5 hash.

### The core functionalities include:

1. Form data based API to intake image file.
2. File image to base64 conversion.
3. Converting the base64 (thus obtained) to an MD5 hash string.
4. AES encryption of the current timestamp to be added to the response.
5. Response of the API should be in JSON


## Base64

Base64 is used to encode binary data into a text based format so that the data can be transmit without changing the underlying bytes of the original data.
It is a method for converting data into encoded (two way hashed) string with proper printable characters only. It’s also like you can save an image to database directly, by first encoding it’s content base64 format. There are many online tools which convert (encode) strings, images and files to base64 encoded string and can also decode from base64 encoded string.

## MD5 Hash

The MD5 hashing algorithm is a one-way cryptographic function that accepts a message of any length as input and returns as output a fixed-length digest value to be used for authenticating the original message.
The MD5 message digest hashing algorithm processes data in 512-bit blocks, broken down into 16 words composed of 32 bits each. The output from MD5 is a 128-bit message digest value.

## AES Encryption

The Advanced Encryption Standard (AES) is a symmetric block cipher used to protect classified information. AES is implemented in software and hardware throughout the world to encrypt sensitive data.
The AES encryption algorithm defines numerous transformations that are to be performed on data stored in an array. The first step of the cipher is to put the data into an array -- after which, the cipher transformations are repeated over multiple encryption rounds.

### Screenshot:

![Screenshot from 2020-06-08 03-10-45](https://user-images.githubusercontent.com/40838784/83980749-c152a080-a935-11ea-91a3-c5243955ed00.png)