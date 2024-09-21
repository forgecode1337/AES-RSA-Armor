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
Change to the repository directory:
```
cd AES-RA-Armor
```
```
sudo chmod +x aes_script.py key_script.py
```
Check your current directory to confirm:
```
pwd
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
Scroll to the end of the file and add the aliases. Replace <code>usr</code> from <code>/home/usr/AES-RSA-Armor</code> with your actual home directory path. For example:
```
alias aes_script='python3 /home/usr/AES-RSA-Armonr/aes_script.py'
alias key_script='python3 /home/usr/AES-RSA-Armor/key_script.py'
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
```
sudo apt update
sudo apt upgrade -y
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

<div style="border-top: 1px solid #000; margin: 10px 0;"></div>

<h3>Summary</h3>
<p>You have successfully set up the AES-RSA Armor repository, created aliases for easy access to your scripts, and learned how to encrypt and decrypt files using the provided scripts.</p>

If you encounter any issues, refer to the README in the cloned repository for further details or check the issues tab on GitHub for community support.</p>

### Support Me

If you appreciate my work, consider buying me a coffee! ☕️

<a href="https://buymeacoffee.com/forgecode" target="_blank" style="text-decoration: none; font-size: 24px; font-weight: bold; background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #7fff00, #00ff00, #00ffff, #007fff, #0000ff, #7f00ff, #ff00ff); background-size: 400%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 3s linear infinite;">
    Buy Me a Coffee
</a>

