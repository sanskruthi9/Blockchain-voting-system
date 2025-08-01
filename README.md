# 🗳️ Blockchain-Based Voting System

A secure, transparent, and tamper-proof electronic voting system built using blockchain technology. This project demonstrates how cryptographic principles and decentralized infrastructure can ensure vote integrity and public trust.

---

## 📌 Project Overview

This application leverages **blockchain**, **SHA-256 hashing**, **digital signatures**, and **proof-of-work** to build a robust and secure voting platform. It features a Flask-based web interface for voters to cast votes, view blockchain data, mine new blocks, and validate the system.

### 🎯 Objectives
- Ensure vote integrity through cryptographic signatures and immutability.
- Increase voter trust by providing a transparent and verifiable voting process.
- Prevent vote tampering via decentralized consensus and proof-of-work.

---

## 🚀 Features

- 🔐 **Secure Voting**: All votes are digitally signed using private keys and stored immutably on the blockchain.
- 🌐 **Decentralization**: No central authority—data is stored in a distributed and tamper-proof ledger.
- 🧾 **Auditability**: Full blockchain ledger can be viewed and verified at any time.
- ⚡ **Real-Time Results**: Votes are counted instantly after block mining.
- 🔍 **Blockchain Validation**: Every block is verified using hash, proof-of-work, and signature integrity checks.

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask** – Web application framework
- **PyCryptodome / cryptography** – For key generation and digital signatures
- **SHA-256** – For hashing and linking blocks
- **HTML/CSS** – Frontend templates

---

## 🔄 Workflow

1. User accesses the voting interface and submits a vote.
2. The vote is digitally signed using a private key.
3. The vote is added to pending transactions.
4. A new block is mined using proof-of-work.
5. Mined blocks are added to the blockchain.
6. The blockchain can be validated at any time.
7. Real-time results can be viewed based on mined votes.

---

## 📋 Routes and Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Homepage with navigation |
| `/vote` | POST | Submit a new vote (voter_id, candidate_id) |
| `/mine` | GET | Mine pending transactions into a block |
| `/chain` | GET | View the entire blockchain |
| `/results` | GET | View current voting results |
| `/validate` | GET | Validate blockchain integrity |
| `/public_key` | GET | View system's public key for signature verification |

---

## 🔐 Cryptographic Components

### 🔗 Hashing (SHA-256)
- Ensures immutability and integrity of blocks.
- Each block’s hash depends on its data and the previous block’s hash.

### ✍️ Digital Signatures
- Votes are signed using the voter's private key.
- Signatures are verified using the public key to ensure authenticity.

### ⛏️ Proof of Work
- Prevents tampering by adding computational cost.
- New proof must satisfy: `hash(new_proof^2 - previous_proof^2)` starting with `"0000"`.

---

## 👩‍💻 Code Structure

### 📁 `interface.py`
- Handles the web interface using Flask.
- Routes for voting, mining, chain viewing, and result display.

### 📁 `blockchain.py`
- Manages blockchain operations:
  - `create_block`
  - `add_vote`
  - `proof_of_work`
  - `is_chain_valid`
  - `validate_votes`

### 📁 `crypto_utils.py`
- Implements:
  - `sign_vote`
  - `verify_vote`
  - `hash_block`
  - `get_public_key_pem`

---

## 📄 License

This project is for educational and demonstration purposes. Not intended for production use without security review.

---

## 📬 Contact

For questions, feel free to reach out via GitHub or during the course showcase.
