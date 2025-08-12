# GDPR & Blockchain Privacy Demo

## Overview
This small demo illustrates the privacy risks of storing personal data on a public blockchain and a basic mitigation using hashing (off-chain vs on-chain considerations are discussed in the appendix).

## Files
- 'gdpr_blockchain_demo.py': Python script demonstrating plain vs hashed data on a simple blockchain.
- 'chain_output.json': Output JSON showing the blockchain after running the demo.

## How to run
1. Ensure you have Python 3 installed.
2. Navigate to the folder containing the files.
3. Run:
'''
python gdpr_blockchain_demo.py
'''
4. The script will create 'chain_output.json' and print the blockchain to stdout.

## Notes
- This demo uses synthetic data. Do not test with real personal data.
- Hashing is a mitigation technique but not a silver bullet for GDPR compliance; see appendix for a discussion.
