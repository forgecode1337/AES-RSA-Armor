### <b>Install and Set Up</b>
<b>Update Your System and Install Necessary Packages:</b>
```
sudo apt update
sudo apt upgrade -y
```
<b>Clone the Repository:</b>
```
sudo git clone https://github.com/forgecode1337/AES-RSA-Armor.git
```
<b>Change to the Repository Directory:</b>
```
cd AES-RSA-Armor
```
<b>Make Scripts Executable:</b> Ensure the script files can be executed:
```
sudo chmod +x aes_script.py key_script.py
```
<b>Check Your Current Directory to Confirm:</b>
```
pwd
```
### <b>Check Which Shell is Set as Default</b>
Run the following command to check your current shell:
```
echo $SHELL
```
### <b>Configure Aliases</b>
<b>For Bash:</b> Edit the <code>.bashrc</code> file located in your home directory:
```
sudo nano ~/.bashrc
```
<b>For Zsh:</b> Edit the <code>.zshrc</code> file:
```
sudo nano ~/.zshrc
```
<b>Add the Aliases:</b> Scroll to the end of the file and add the following lines. Replace <code>usr</code> in <code>/home/usr/AES-RSA-Armor</code> with your actual home directory path:
```
alias aes_script='python3 /home/usr/AES-RSA-Armor/aes_script.py'
alias key_script='python3 /home/usr/AES-RSA-Armor/key_script.py'
```
## <b>Save and Exit</b>
<p>For Nano:</p>
<ul>
    <li>Press <code>Ctrl + X</code> to exit.</li>
    <li>Press <code>Y</code> to confirm changes.</li>
    <li>Press <code>Enter</code> to save.</li>
</ul>

### <b>Reload the shell configuration file:</b>
For Bash:
```
source ~/.bashrc
```
For Zsh:
```
source ~/.zshrc
```
### <b>Generate Keys</b>
Run the key generation script:
```
key_script
```
### <b>Example:</b>
Copy the Base64-encoded AES Key and Encrypted AES Key from the output:
```
Base64-encoded AES Key: g51P3EgtoqqFfOAZBYfJgEQUufpRfKJ6+Cw9k2Ytzm8=
Base64-encoded Encrypted AES Key: No/mFV0csQgN2f8x9tYwnJmWjowRsUrfk/y0AcxHG4xen6My5O1/51ZZseOhYfhu5Au4SlLKx4T99rCvJrndq009CNwjITjcE9vha9DCrdgwLpJOU5HLj+lRKrhF6/uWAWLJ56LIwQ5Oq1L2DlAHbANVs6Vb2qj84F828pqNHu7AJdIHEwvkhfhPKBEP6HDezD94DrZazqy+UBujJ2mral2Bqld4KvFGNgWwiKDc/FiPjWoEq+Yv48GXPMP5OoofQycT9wEAvCtBfwhlVM+NlXegpsxuihSaBCB3k5Vcth0GD8lf9kazVnvYTxbeD19kAzZ7c/n70XkVnLrL3n/QUg==
```
### <b>Using the Scripts</b>
#### <b>Encrypt a File</b>
To encrypt a file, use the <code>aes_script</code> with the Base64-encoded AES Key a you generated:
```
aes_script encrypt [original_filename] [new_filename] --key [Base64-encoded AES Key] --delete
```
<li>Replace <code>[original_filename]</code> with the path to the file you want to encrypt.</li>
<li>Replace <code>[new_filename]</code> with the desired name for the encrypted file.</li>

#### <b>Decrypt a File</b>
To decrypt the file you just encrypted, use the Base64-encoded Encrypted AES Key, which is the AES key encrypted with RSA:
```
aes_script decrypt [new_filename] [original_filename] [Base64-encoded Encrypted AES Key] private.pem --delete
```
<li>Replace <code>[new_filename]</code> with the name of the encrypted file you want to decrypt.</li>
<li>Replace <code>[original_filename]</code> with the name you want for the decrypted file.</li>

<div style="border-top: 1px solid #000; margin: 10px 0;"></div>

### <b>Summary</b>
<p>You have successfully set up the AES-RSA Armor repository, created aliases for easy access to your scripts, and learned how to encrypt and decrypt files using the provided scripts.

If you encounter any issues, refer to the README in the cloned repository for further details or check the issues tab on GitHub for community support.</p>

### <b>Support Me</b>

If you appreciate my work, consider buying me a coffee! ☕️

<a href="https://buymeacoffee.com/forgecode" target="_blank" style="text-decoration: none; font-size: 24px; font-weight: bold; background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #7fff00, #00ff00, #00ffff, #007fff, #0000ff, #7f00ff, #ff00ff); background-size: 400%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 3s linear infinite;">
    ⭐⭐⭐ Buy Me a Coffee ⭐⭐⭐
</a>
