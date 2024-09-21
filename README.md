### Install and Set Up
First, make sure your system is up to date and install necessary packages:
```
sudo apt update
sudo apt upgrade -y
```
Clone the repository:
```
sudo git clone https://github.com/forgecode1337/AES-RSA-Armor.git
```
### Check Which Shell is Set as Default
Run the following command to check which shell you are using:
```
echo $SHELL
```
### Configure Aliases
If you are using Bash, edit the <code>.bashrc</code> file located in your home directory:
```
nano ~/.bashrc
```
If you are using Zsh, edit the <code>.zshrc</code> file:
```
nano ~/.zshrc
```
Scroll to the end of the file and add the aliases. Replace <code>/home/usr</code> with your actual home directory path. For example:
```
alias aes_script='python3 /home/usr/aes_script.py'
alias key_script='python3 /home/usr/key_script.py'
```
## Save and Exit
<p>For Nano:</p>
<ul>
    <li>Press <code>Ctrl + X</code> to exit.</li>
    <li>Press <code>Y</code> to confirm changes.</li>
    <li>Press <code>Enter</code> to save.</li>
</ul>

Reload the shell configuration file:
```
source ~/.bashrc
```
or for Zsh:
```
source ~/.zshrc
```
### Generate Keys
Run the key generation script:
```
key_script
```
### Example:
Copy the Base64-encoded AES Key and Encrypted AES Key from the output:
```
Base64-encoded AES Key: g51P3EgtoqqFfOAZBYfJgEQUufpRfKJ6+Cw9k2Ytzm8=
Base64-encoded Encrypted AES Key: No/mFV0csQgN2f8x9tYwnJmWjowRsUrfk/y0AcxHG4xen6My5O1/51ZZseOhYfhu5Au4SlLKx4T99rCvJrndq009CNwjITjcE9vha9DCrdgwLpJOU5HLj+lRKrhF6/uWAWLJ56LIwQ5Oq1L2DlAHbANVs6Vb2qj84F828pqNHu7AJdIHEwvkhfhPKBEP6HDezD94DrZazqy+UBujJ2mral2Bqld4KvFGNgWwiKDc/FiPjWoEq+Yv48GXPMP5OoofQycT9wEAvCtBfwhlVM+NlXegpsxuihSaBCB3k5Vcth0GD8lf9kazVnvYTxbeD19kAzZ7c/n70XkVnLrL3n/QUg==
```
### Using the Scripts
#### Encrypt a File
To encrypt a file, use the <code>aes_script</code> with the Base64-encoded AES Key and Encrypted AES Key you generated:
```
aes_script encrypt [original_filename] [new_filename] --key g51P3EgtoqqFfOAZBYfJgEQUufpRfKJ6+Cw9k2Ytzm8= --delete
```
Replace [original_filename] with the path to the file you want to encrypt.
Replace [new_filename] with the desired name for the encrypted file.

#### Decrypt a File
To decrypt the file you just encrypted, use:
```
aes_script decrypt [new_filename] [original_filename] No/mFV0csQgN2f8x9tYwnJmWjowRsUrfk/y0AcxHG4xen6My5O1/51ZZseOhYfhu5Au4SlLKx4T99rCvJrndq009CNwjITjcE9vha9DCrdgwLpJOU5HLj+lRKrhF6/uWAWLJ56LIwQ5Oq1L2DlAHbANVs6Vb2qj84F828pqNHu7AJdIHEwvkhfhPKBEP6HDezD94DrZazqy+UBujJ2mral2Bqld4KvFGNgWwiKDc/FiPjWoEq+Yv48GXPMP5OoofQycT9wEAvCtBfwhlVM+NlXegpsxuihSaBCB3k5Vcth0GD8lf9kazVnvYTxbeD19kAzZ7c/n70XkVnLrL3n/QUg== private.pem --delete
```
Replace [new_filename] with the name of the encrypted file you want to decrypt.
Replace [original_filename] with the name you want for the decrypted file.

### Summary
You have successfully set up the AES-RSA Armor repository, created aliases for easy access to your scripts, and learned how to encrypt and decrypt files using the provided scripts.

If you encounter any issues, refer to the README in the cloned repository for further details or check the issues tab on GitHub for community support.

#### Happy coding!
