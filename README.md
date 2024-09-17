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
If you are using Bash, you should edit the .bashrc file, which is located in your home directory:
```
nano ~/.bashrc
```
If you are using Zsh, you should edit the .zshrc file, which is also located in your home directory:
```
nano ~/.zshrc
```
Scroll to the end of the file and add the aliases. Replace /home/usr with your actual home directory path. For example:
```
alias aes_script='python3 /home/usr/aes_script.py'
alias key_script='python3 /home/usr/key_script.py'
```
## Save and Exit
<ul> 
    <li>For Nano:</li>
    <ul>
       <li> Press Ctrl + X to exit.</li>
        <li>Press Y to confirm changes.</li>
        <li>Press Enter to save.</li>
    </ul>
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
key_script
```
```
#copy the Base64-encoded AES Key:
Base64-encoded AES Key: g51P3EgtoqqFfOAZBYfJgEQUufpRfKJ6+Cw9k2Ytzm8=
Base64-encoded Encrypted AES Key: No/mFV0csQgN2f8x9tYwnJmWjowRsUrfk/y0AcxHG4xen6My5O1/51ZZseOhYfhu5Au4SlLKx4T99rCvJrndq009CNwjITjcE9vha9DCrdgwLpJOU5HLj+lRKrhF6/uWAWLJ56LIwQ5Oq1L2DlAHbANVs6Vb2qj84F828pqNHu7AJdIHEwvkhfhPKBEP6HDezD94DrZazqy+UBujJ2mral2Bqld4KvFGNgWwiKDc/FiPjWoEq+Yv48GXPMP5OoofQycT9wEAvCtBfwhlVM+NlXegpsxuihSaBCB3k5Vcth0GD8lf9kazVnvYTxbeD19kAzZ7c/n70XkVnLrL3n/QUg==
```
Using the Scripts

Encrypt a File:

Copy the Base64-encoded AES Key and Encrypted AES Key from your key generation process. Use the following command to encrypt a file:
```
aes_script encrypt [original_filename] [new_filename] --key g51P3EgtoqqFfOAZBYfJgEQUufpRfKJ6+Cw9k2Ytzm8= --delete
```
```
aes_script decrypt [new_filename] [original_filename] No/mFV0csQgN2f8x9tYwnJmWjowRsUrfk/y0AcxHG4xen6My5O1/51ZZseOhYfhu5Au4SlLKx4T99rCvJrndq009CNwjITjcE9vha9DCrdgwLpJOU5HLj+lRKrhF6/uWAWLJ56LIwQ5Oq1L2DlAHbANVs6Vb2qj84F828pqNHu7AJdIHEwvkhfhPKBEP6HDezD94DrZazqy+UBujJ2mral2Bqld4KvFGNgWwiKDc/FiPjWoEq+Yv48GXPMP5OoofQycT9wEAvCtBfwhlVM+NlXegpsxuihSaBCB3k5Vcth0GD8lf9kazVnvYTxbeD19kAzZ7c/n70XkVnLrL3n/QUg== private.pem --delete
```
