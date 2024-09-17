#!/usr/bin/env python3
import argparse
import base64
import os
import shutil
import stat
import time
import logging
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

LOCK_FILE = 'process.lock'
LOG_FILE = 'process.log'

# Set up logging
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_key(key_file):
    try:
        with open(key_file, 'rb') as f:
            return RSA.import_key(f.read())
    except Exception as e:
        logging.error(f"Failed to load key from {key_file}: {e}")
        raise

def decrypt_aes_key(encrypted_aes_key, rsa_private_key):
    try:
        rsa_key = load_key(rsa_private_key)
        cipher_rsa = PKCS1_OAEP.new(rsa_key)
        encrypted_aes_key = base64.b64decode(encrypted_aes_key)
        return cipher_rsa.decrypt(encrypted_aes_key)
    except Exception as e:
        logging.error(f"Failed to decrypt AES key: {e}")
        raise

def encrypt_file(file_path, output_path, aes_key):
    try:
        cipher = AES.new(aes_key, AES.MODE_EAX)
        with open(file_path, 'rb') as f:
            plaintext = f.read()
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        with open(output_path, 'wb') as f:
            f.write(cipher.nonce)
            f.write(tag)
            f.write(ciphertext)
        logging.info(f"File {file_path} encrypted and saved to {output_path}")
    except Exception as e:
        logging.error(f"Failed to encrypt file {file_path}: {e}")
        raise

def decrypt_file(file_path, output_path, aes_key):
    try:
        with open(file_path, 'rb') as f:
            nonce = f.read(16)
            tag = f.read(16)
            ciphertext = f.read()
        cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        with open(output_path, 'wb') as f:
            f.write(plaintext)
        logging.info(f"File {file_path} decrypted and saved to {output_path}")
    except Exception as e:
        logging.error(f"Failed to decrypt file {file_path}: {e}")
        raise

def make_read_only(path):
    """Recursively make directory and files read-only."""
    try:
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.chmod(file_path, stat.S_IREAD)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.chmod(dir_path, stat.S_IREAD | stat.S_IEXEC)
        logging.info(f"Made {path} read-only")
    except Exception as e:
        logging.error(f"Failed to make {path} read-only: {e}")
        raise

def make_writable(path):
    """Recursively make directory and files writable."""
    try:
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.chmod(file_path, stat.S_IWRITE | stat.S_IREAD)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.chmod(dir_path, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
        logging.info(f"Made {path} writable")
    except Exception as e:
        logging.error(f"Failed to make {path} writable: {e}")
        raise

def create_lock_file():
    """Create a lock file to indicate processing is ongoing."""
    try:
        with open(LOCK_FILE, 'w') as f:
            f.write('Encryption/Decryption in progress.')
        logging.info("Lock file created")
    except Exception as e:
        logging.error(f"Failed to create lock file: {e}")
        raise

def remove_lock_file():
    """Remove the lock file to indicate processing is complete."""
    try:
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
        logging.info("Lock file removed")
    except Exception as e:
        logging.error(f"Failed to remove lock file: {e}")
        raise

def process_directory(directory, output_directory, aes_key, is_encryption):
    """Process files in a directory."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    processed_files = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            input_path = os.path.join(root, file)
            relative_path = os.path.relpath(input_path, directory)
            output_path = os.path.join(output_directory, relative_path)
            output_folder = os.path.dirname(output_path)

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            try:
                if is_encryption:
                    encrypt_file(input_path, output_path, aes_key)
                else:
                    decrypt_file(input_path, output_path, aes_key)
                processed_files.add(input_path)
            except Exception as e:
                logging.error(f"Error processing file {input_path}: {e}")

    return bool(processed_files)

def delete_directory(directory):
    """Delete a directory and its contents."""
    try:
        if os.path.isdir(directory):
            shutil.rmtree(directory)
            logging.info(f"Directory {directory} deleted")
        else:
            logging.info(f"Path {directory} is not a directory")
    except Exception as e:
        logging.error(f"Failed to delete directory {directory}: {e}")
        raise

def monitor_directory(directory, output_directory, aes_key, private_key, is_encryption):
    """Monitor a directory and process files."""
    logging.info(f"Monitoring directory {directory}")
    processed_files = set()
    while True:
        if os.path.exists(LOCK_FILE):
            logging.info("Processing is ongoing. Please wait...")
            time.sleep(10)
            continue
        
        files_processed = False
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    input_path = os.path.join(root, file)
                    relative_path = os.path.relpath(input_path, directory)
                    output_path = os.path.join(output_directory, relative_path)
                    output_folder = os.path.dirname(output_path)

                    if not os.path.exists(output_folder):
                        os.makedirs(output_folder)

                    if is_encryption:
                        if input_path not in processed_files:
                            encrypt_file(input_path, output_path, aes_key)
                            processed_files.add(input_path)
                            files_processed = True
                    else:
                        if input_path not in processed_files:
                            decrypt_file(input_path, output_path, aes_key)
                            processed_files.add(input_path)
                            files_processed = True

            if not files_processed:
                break

        except Exception as e:
            logging.error(f"Error while monitoring directory {directory}: {e}")
        
        time.sleep(10)  # Wait for 10 seconds before re-checking

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files and directories.')
    subparsers = parser.add_subparsers(dest='command')
    
    # Encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a file or directory.')
    encrypt_parser.add_argument('input_path', help='Path to the input file or directory.')
    encrypt_parser.add_argument('output_path', help='Path to the output file or directory.')
    encrypt_parser.add_argument('--key', required=True, help='Base64-encoded AES key.')
    encrypt_parser.add_argument('--delete', action='store_true', help='Delete the input file or directory after encryption.')

    # Decrypt command
    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt a file or directory.')
    decrypt_parser.add_argument('input_path', help='Path to the input file or directory.')
    decrypt_parser.add_argument('output_path', help='Path to the output file or directory.')
    decrypt_parser.add_argument('encrypted_aes_key', help='Base64-encoded encrypted AES key.')
    decrypt_parser.add_argument('private_key', help='Path to the RSA private key.')
    decrypt_parser.add_argument('--delete', action='store_true', help='Delete the input file or directory after decryption.')

    args = parser.parse_args()

    if args.command == 'encrypt':
        if os.path.exists(LOCK_FILE):
            logging.info("Encryption or decryption is already in progress. Please wait.")
            print("Processing is ongoing. Please wait...")
            return
        
        create_lock_file()
        try:
            aes_key = base64.b64decode(args.key)
            if os.path.isfile(args.input_path):
                if os.path.exists(args.input_path):
                    encrypt_file(args.input_path, args.output_path, aes_key)
                    make_read_only(args.output_path)
                    print(f'File encrypted and saved to {args.output_path}')
                else:
                    print(f'Input path {args.input_path} does not exist.')
            elif os.path.isdir(args.input_path):
                success = process_directory(args.input_path, args.output_path, aes_key, is_encryption=True)
                if success:
                    make_read_only(args.output_path)
                    print(f'Files encrypted and saved to {args.output_path}')
                else:
                    print(f'No files found to encrypt in {args.input_path}')
            if args.delete:
                remove_lock_file()
                if os.path.isdir(args.input_path):
                    delete_directory(args.input_path)
                else:
                    os.remove(args.input_path)
        except Exception as e:
            logging.error(f"An error occurred during encryption: {e}")
            print(f"An error occurred: {e}")
        finally:
            remove_lock_file()

    elif args.command == 'decrypt':
        if os.path.exists(LOCK_FILE):
            logging.info("Encryption or decryption is already in progress. Please wait.")
            print("Processing is ongoing. Please wait...")
            return
        
        create_lock_file()
        try:
            aes_key = decrypt_aes_key(args.encrypted_aes_key, args.private_key)
            if os.path.isfile(args.input_path):
                if os.path.exists(args.input_path):
                    decrypt_file(args.input_path, args.output_path, aes_key)
                    make_writable(args.output_path)
                    print(f'File decrypted and saved to {args.output_path}')
                else:
                    print(f'Input path {args.input_path} does not exist.')
            elif os.path.isdir(args.input_path):
                success = process_directory(args.input_path, args.output_path, aes_key, is_encryption=False)
                if success:
                    make_writable(args.output_path)
                    print(f'Files decrypted and saved to {args.output_path}')
                else:
                    print(f'No files found to decrypt in {args.input_path}')
            if args.delete:
                remove_lock_file()
                if os.path.isdir(args.input_path):
                    delete_directory(args.input_path)
                else:
                    os.remove(args.input_path)
        except Exception as e:
            logging.error(f"An error occurred during decryption: {e}")
            print(f"An error occurred: {e}")
        finally:
            remove_lock_file()

if __name__ == "__main__":
    main()